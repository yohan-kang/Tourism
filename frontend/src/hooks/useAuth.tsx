import React, { useContext } from "react";
import AuthContext from "../contexts/AuthContext";

type Props = {};

const useAuth = () => {
  return useContext(AuthContext);
};

export default useAuth;
