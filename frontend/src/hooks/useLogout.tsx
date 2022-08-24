import React from "react";
import axios from "../api/axios";
import useAuth from "./useAuth";
import useAxiosPrivate from "./useAxiosPrivate";

function useLogout() {
  const { auth, setAuth } = useAuth();
  const axiosPrivate = useAxiosPrivate();
  const logout = async () => {
    setAuth({});
    try {
      await axiosPrivate.post(
        "/api/logout/",
        JSON.stringify({ refresh_token: auth.refreshToken }),
        {
          withCredentials: true,
        }
      );
      // localStorage.setItem("refresh_token", "");
    } catch (error) {
      console.error(error);
    }
  };

  return logout;
}

export default useLogout;
