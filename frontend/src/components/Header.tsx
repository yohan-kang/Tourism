import React from "react";
import { Link } from "react-router-dom";

type Props = {};

export default function Header({}: Props) {
  return (
    <div>
      <Link to="/">Home</Link>
      <span> | </span>
      <Link to="/login">Login</Link>
      <span> | </span>
      <Link to="/boards">BoardList</Link>
    </div>
  );
}
