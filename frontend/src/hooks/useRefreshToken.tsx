import React, { useContext } from "react";
import axios from "../api/axios";
import useAuth from "./useAuth";
import AuthContext from "../contexts/AuthContext";
import jwt_decode from "jwt-decode"; // import dependency

interface IToken {
  username: string;
}
const useRefreshToken = () => {
  const { setAuth } = useContext(AuthContext);
  // const { auth, setAuth } = useAuth();
  const refresh = async () => {
    const response = await axios.post(
      "/api/token/refresh/",
      JSON.stringify({ refresh: localStorage.getItem("refresh_token") }),
      {
        headers: { "Content-Type": "application/json" },
        withCredentials: true,
      }
    );

    setAuth((prev: any) => {
      localStorage.setItem("refresh_token", response.data.refresh);
      const decoded: IToken = jwt_decode(response.data.access);
      return {
        ...prev,
        accessToken: response.data.access,
        refreshToken: response.data.refresh,
        username: decoded.username,
      };
    });
    return response.data.access;
  };

  return refresh;
};

export default useRefreshToken;
