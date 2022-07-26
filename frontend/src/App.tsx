import React from "react";
import "./App.css";
import { Route, Routes } from "react-router-dom";
import Home from "./pages/Home";
import Login from "./pages/Login";
import BoardList from "./pages/BoardList";
import PersistLogin from "./components/PersistLogin";
import Layout from "./components/Layout";
import RequireAuth from "./components/RequireAuth";
import BoardDetail from "./pages/BoardDetail";
import { PERMISSIONS } from "./utils/permissions";
import CreateBoard from "./pages/CreateBoard";
function App() {
  return (
    <>
      <Routes>
        <Route path="login" element={<Login />} />
        <Route element={<PersistLogin />}>
          <Route path="/" element={<Layout />}>
            <Route path="/" element={<Home />} />
            <Route
              element={<RequireAuth allowedRoles={[PERMISSIONS.Board_view]} />}
            >
              <Route path="boards" element={<BoardList />} />

              <Route
                element={
                  <RequireAuth allowedRoles={[PERMISSIONS.Board_create]} />
                }
              >
                <Route path="boards/newBoard" element={<CreateBoard />} />
              </Route>
              <Route path="boards/:id" element={<BoardDetail />} />
            </Route>
          </Route>
        </Route>
      </Routes>
    </>
  );
}

export default App;
