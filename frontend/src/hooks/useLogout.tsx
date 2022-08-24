import React from "react";
import useAuth from "./useAuth";
import useAxiosPrivate from "./useAxiosPrivate";

function useLogout() {
  const { auth, setAuth } = useAuth();
  const axiosPrivate = useAxiosPrivate();
  const logout = async () => {
    try {
      await axiosPrivate.post(
        "/api/logout/",
        JSON.stringify({
          // access: auth.accessToken,
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
