import React, { createContext, useState } from "react";

type Props = {
  children: any;
};

const AuthContext: any = createContext({});

export function AuthProvider({ children }: Props) {
  const [auth, setAuth] = useState({});
  return (
    <AuthContext.Provider value={{ auth, setAuth }}>
      {children}
    </AuthContext.Provider>
  );
}

export default AuthContext;
