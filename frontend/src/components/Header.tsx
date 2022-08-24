import React, { useContext, useEffect, useState } from "react";
import { Link, useNavigate } from "react-router-dom";
import AuthContext from "../contexts/AuthContext";
import useAuth from "../hooks/useAuth";
import useLogout from "../hooks/useLogout";
type Props = {};

export default function Header({}: Props) {
  const { auth, setAuth } = useContext(AuthContext);
  const navigate = useNavigate();
  const logout = useLogout();
  // const { auth, setAuth } = useAuth();
  const [username, setUsername] = useState("");

  const signOut = async () => {
    await logout();
    navigate("/login");
  };

  useEffect(() => {
    console.log(auth);
    setUsername(auth?.username || "");
  }, [auth]);
  return (
    <>
      <h1>{username ? `Hello ${username}` : `You are not logged in`}</h1>
      <div>
        <Link to="/">Home</Link>
        <span> | </span>
        <Link to="/login">Login</Link>
        <span> | </span>
        <Link to="/boards">BoardList</Link>
        <span> | </span>
        <button onClick={signOut}>Sign Out</button>
      </div>
    </>
  );
}
