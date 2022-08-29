import React from "react";
import { Navigate } from "react-router-dom";
import useAuth from "../hooks/useAuth";

export default function Home() {
  const { auth } = useAuth();
  return (
    <>
      {auth?.username ? (
        <div className="main-container">
          <h1>Home</h1>
        </div>
      ) : (
        <Navigate to="/login" />
      )}
    </>
  );
}
