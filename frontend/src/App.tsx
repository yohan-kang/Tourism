import React from "react";
import logo from "./logo.svg";
import "./App.css";
import { Route, Routes } from "react-router-dom";
import Home from "./pages/Home";
import Login from "./pages/Login";
import Header from "./components/Header";
import BoardList from "./pages/BoardList";
import PersistLogin from "./components/PersistLogin";

function App() {
  return (
    <>
      <Header />
      <Routes>
        <Route element={<PersistLogin />}>
          <Route path="/" element={<Home />} />
          <Route path="/login" element={<Login />} />
          <Route path="/boards" element={<BoardList />} />
        </Route>
      </Routes>
    </>
  );
}

export default App;
