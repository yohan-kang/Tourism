import React, { useEffect, useState } from "react";
import { Link, useNavigate } from "react-router-dom";
import useAuth from "../hooks/useAuth";
import useLogout from "../hooks/useLogout";

export default function Header() {
  const navigate = useNavigate();
  const logout = useLogout();
  const { auth } = useAuth();
  const [username, setUsername] = useState("");

  const signOut = async () => {
    await logout();
    navigate("/login");
  };

  useEffect(() => {
    setUsername(username || "");
  }, []);
  return (
    <>
      <h1>
        {auth?.username ? `Hello ${auth.username}` : `You are not logged in`}
      </h1>
      <div>
        <Link to="/">Home</Link>
        <span> | </span>
        <Link to="/boards">BoardList</Link>
        <span> | </span>
        {auth?.username ? (
          <button onClick={signOut}>Sign Out</button>
        ) : (
          <Link to="/login">Login</Link>
        )}
      </div>
    </>
  );
}
