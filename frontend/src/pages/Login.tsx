import React, {
  SyntheticEvent,
  useState,
  useRef,
  useEffect,
  useContext,
} from "react";

import AuthContext from "../contexts/AuthContext";

import axios from "../api/axios";
const LOGIN_URL = "/api/token/";

type Props = {};

function Login() {
  const { auth, setAuth } = useContext(AuthContext);
  const usernameRef: any = useRef();
  const errRef: any = useRef();
  const [username, setUsername] = useState("");
  const [password, setPassword] = useState("");
  const [errMsg, setErrMsg] = useState("");

  useEffect(() => {
    usernameRef?.current?.focus();
  }, []);

  useEffect(() => {
    setErrMsg("");
  }, [username, password]);

  const submit = async (e: SyntheticEvent) => {
    e.preventDefault();

    try {
      const response = await axios.post(
        LOGIN_URL,
        JSON.stringify({ username, password }),
        {
          headers: { "Content-Type": "application/json" },
          // withCredentials: true,
        }
      );
      const accessToken = response?.data?.access;
      const refreshToken = response?.data?.refresh;
      console.log(auth);
      setAuth({ username, accessToken, refreshToken });
      console.log(auth);
      setUsername("");
      setPassword("");
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
