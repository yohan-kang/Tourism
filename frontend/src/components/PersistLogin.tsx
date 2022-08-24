import React, { useState, useEffect, useContext } from "react";
import { Outlet } from "react-router-dom";
import useRefreshToken from "../hooks/useRefreshToken";
import useAuth from "../hooks/useAuth";
import AuthContext from "../contexts/AuthContext";
export default function PersistLogin() {
  const [isLoading, setIsLoading] = useState(true);
  const refresh = useRefreshToken();
  const { auth } = useAuth();
  // const { auth } = useContext(AuthContext);

  useEffect(() => {
    console.log("PersistLogin1:");
    console.log(auth);
    const verifyRefreshToken = async () => {
      console.log("verifyRefreshToken");
      console.log(auth);
      try {
        await refresh();
      } catch (err) {
        console.error(err);
      } finally {
        setIsLoading(false);
      }
    };

    !auth?.accessToken ? verifyRefreshToken() : setIsLoading(false);
  }, [isLoading]);

  return <>{isLoading ? <p>Loading...</p> : <Outlet />}</>;
}
