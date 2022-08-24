import { SyntheticEvent, useState, useRef, useEffect } from "react";
import { useLocation, useNavigate } from "react-router-dom";
import useAuth from "../hooks/useAuth";
import myFetch from "../utils/myFetch";

const LOGIN_URL = "/api/token/";

function Login() {
  const { auth, setAuth } = useAuth();
  const usernameRef: any = useRef();
  const errRef: any = useRef();
  const [username, setUsername] = useState("");
  const [password, setPassword] = useState("");
  const [errMsg, setErrMsg] = useState("");

  const navigate = useNavigate();
  const location: any = useLocation();
  const from = location.state?.from?.pathname || "/";

  useEffect(() => {
    if (auth?.username) navigate(from, { replace: true });
  }, []);

  useEffect(() => {
    usernameRef?.current?.focus();
  }, []);

  useEffect(() => {
    setErrMsg("");
  }, [username, password]);

  const submit = async (e: SyntheticEvent) => {
    e.preventDefault();

    try {
      const response = await myFetch.post(
        LOGIN_URL,
        JSON.stringify({ username, password }),
        {
          headers: { "Content-Type": "application/json" },
          withCredentials: true,
        }
      );
      const accessToken = response?.data?.access;
      const refreshToken = response?.data?.refresh;
      setAuth({ username, accessToken, refreshToken });
      localStorage.setItem("refresh_token", refreshToken);
      setUsername("");
      setPassword("");
      navigate(from, { replace: true });
    } catch (err: any) {
      if (!err?.response) {
        setErrMsg("No Server Response");
      } else if (err.response?.status === 400) {
        setErrMsg("Missing Username or Password");
      } else if (err.response?.status === 401) {
        setErrMsg("Unauthorized");
      } else {
        setErrMsg("Login Failed");
      }

      errRef?.current?.focus();
    }
  };

  return (
    <div>
      <h1>Sign In</h1>
      <p
        ref={errRef}
        className={errMsg ? "errmsg" : "offscreen"}
        aria-live="assertive"
      >
        {errMsg}
      </p>
      <form onSubmit={submit}>
        <label htmlFor="username">Username: </label>
        <input
          type="text"
          name="username"
          id="username"
          ref={usernameRef}
          value={username}
          autoComplete="off"
          onChange={(e) => setUsername(e.target.value)}
          placeholder="Enter Username"
          required
        />
        <br />
        <label htmlFor="password">Password: </label>
        <input
          type="password"
          name="password"
          id="password"
          value={password}
          onChange={(e) => setPassword(e.target.value)}
          placeholder="Enter Password"
          required
        />
        <br />
        <input type="submit" value="Login" />
      </form>
    </div>
  );
}

export default Login;
