import React, { useContext } from "react";
import axios from "../api/axios";
import useAuth from "./useAuth";

const useRefreshToken = () => {
  const { auth, setAuth } = useAuth();
  const refresh = async () => {
    console.log("refresh : ");
    console.log(auth);
    const response = await axios.post(
      "/api/token/refresh/",
      JSON.stringify({ refresh: localStorage.getItem("refresh_token") }),
      {
        headers: { "Content-Type": "application/json" },
        // withCredentials: true,
      }
    );

    console.log("response1111111:");
    console.log(response);

    setAuth((prev: any) => {
      console.log("refresh.setAuth : ");
      console.log(JSON.stringify(prev));
      console.log("response:");
      console.log(response?.data);
      localStorage.setItem("refresh_token", response.data.refresh);
      return {
        ...prev,
        accessToken: response.data.access,
        refreshToken: response.data.refresh,
      };
    });
    return response.data.access;
  };

  return refresh;
};

export default useRefreshToken;
