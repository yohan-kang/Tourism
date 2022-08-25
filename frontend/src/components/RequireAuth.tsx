import React from "react";
import { Navigate, Outlet, useLocation } from "react-router-dom";
import useAuth from "../hooks/useAuth";
import hasPermission from "../utils/permissions";
type Props = {
  allowedRoles: Array<string>;
};

function RequireAuth({ allowedRoles }: Props) {
  const { auth } = useAuth();
  const location = useLocation();

  return hasPermission(auth.accessToken, allowedRoles) ? (
    <Outlet />
  ) : auth?.username ? (
    <Navigate to="/" state={{ from: location }} replace />
  ) : (
    <Navigate to="/login" state={{ from: location }} replace />
  );
}

export default RequireAuth;
