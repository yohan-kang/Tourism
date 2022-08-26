import React, { useEffect, useRef, useState } from "react";
import { Link, useNavigate } from "react-router-dom";
import useAuth from "../hooks/useAuth";
import useLogout from "../hooks/useLogout";

export default function Header() {
  const navigate = useNavigate();
  const logout = useLogout();
  const { auth } = useAuth();
  const [username, setUsername] = useState("");
  const navbarLinksRef: any = useRef(null);

  const signOut = async () => {
    await logout();
    navigate("/login");
  };

  const toggleHandle = () => {
    navbarLinksRef.current.classList.toggle("active");
  };

  useEffect(() => {
    setUsername(username || "");
  }, []);
  return (
    <>
      <nav className="navbar">
        <div className="tourism-title">Tourism</div>
        <div className="username">
          {auth?.username ? `Hello ${auth.username}` : `You are not logged in`}
        </div>
        <button className="toggle-button" onClick={toggleHandle}>
          <span className="bar"></span>
          <span className="bar"></span>
          <span className="bar"></span>
        </button>
        <div className="navbar-links" ref={navbarLinksRef}>
          <ul>
            <li>
              <Link to="/">Home</Link>
            </li>
            <li>
              <Link to="/boards">BoardList</Link>
            </li>
            <li>
              <button onClick={signOut} className="signout-button">
                Sign Out
              </button>
            </li>
          </ul>
        </div>
      </nav>
    </>
  );
}
