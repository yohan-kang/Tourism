import React from "react";
import logo from "./logo.svg";
import "./App.css";
import { Route, Routes } from "react-router-dom";
import Home from "./pages/Home";
import Login from "./pages/Login";
import Header from "./components/Header";
import BoardList from "./pages/BoardList";
import PersistLogin from "./components/PersistLogin";
import Layout from "./components/Layout";
import RequireAuth from "./components/RequireAuth";

function App() {
  return (
    <>
      <Routes>
        <Route path="/" element={<Layout />}>
          <Route path="login" element={<Login />} />
          <Route element={<PersistLogin />}>
            {/* <Route element={<RequireAuth />}> */}
            <Route path="/" element={<Home />} />
            <Route path="boards" element={<BoardList />} />
            {/* </Route> */}
          </Route>
        </Route>
      </Routes>
    </>
  );
}

export default App;
