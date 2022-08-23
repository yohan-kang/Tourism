import React, { useContext, useEffect, useState } from "react";
import { Link } from "react-router-dom";
import AuthContext from "../contexts/AuthContext";
type Props = {};

export default function Header({}: Props) {
  const { auth, setAuth } = useContext(AuthContext);
  const [username, setUsername] = useState("");

  useEffect(() => {
    setUsername(localStorage.getItem("username") || "");
  }, [auth.username]);
  return (
    <>
      <h1>{username ? `Hello ${username}` : `You are not logged in`}</h1>
      <div>
        <Link to="/">Home</Link>
        <span> | </span>
        <Link to="/login">Login</Link>
        <span> | </span>
        <Link to="/boards">BoardList</Link>
      </div>
    </>
  );
}
