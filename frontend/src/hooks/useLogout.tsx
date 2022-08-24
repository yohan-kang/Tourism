import React from "react";
import IFetch from "../interfaces/IFetch";
import useAuth from "./useAuth";
import useFetchPrivate from "./useFetchPrivate";

function useLogout() {
  const { auth, setAuth } = useAuth();
  const fetch: IFetch = useFetchPrivate();
  const logout = async () => {
    try {
      await fetch.post(
        "/api/logout/",
        JSON.stringify({
          refresh: auth.refreshToken,
        }),
        {
          withCredentials: true,
        }
      );
      setAuth({});
      localStorage.removeItem("refresh_token");
    } catch (error) {
      console.error(error);
    }
  };

  return logout;
}

export default useLogout;
