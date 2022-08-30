import React from "react";
import { Navigate } from "react-router-dom";
import useAuth from "../hooks/useAuth";

export default function Home() {
  const { auth } = useAuth();
  return (
    <>
      {auth?.username ? (
        <div className="main-container">
          <div className="container small-container">
            <h1 className="title">Home</h1>
          </div>
        </div>
      ) : (
        <Navigate to="/login" />
      )}
    </>
  );
}
