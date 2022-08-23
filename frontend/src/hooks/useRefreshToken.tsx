import React, { useContext } from "react";
import axios from "../api/axios";
import useAuth from "./useAuth";
type Props = {};

const useRefreshToken = () => {
  const { setAuth }: any = useAuth();
  const refresh = async (refreshToken: string) => {
    const response = await axios.post(
      "/api/token/refresh/",
      JSON.stringify({ refresh: refreshToken }),
      {
        headers: { "Content-Type": "application/json" },
        // withCredentials: true,
      }
    );

    setAuth((prev: any) => {
      console.log(JSON.stringify(prev));
      console.log(response?.data);
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
