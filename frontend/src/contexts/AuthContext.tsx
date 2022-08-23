import React, { createContext, useState } from "react";

type Props = {
  children: any;
};

interface IAuth {
  username: string;
  accessToken: string;
  refreshToken: string;
}

interface IContext {
  auth: any;
  setAuth: any;
}

const AuthContext: React.Context<IContext> = createContext<IContext>({
  auth: {},
  setAuth: null,
});

export function AuthProvider({ children }: Props) {
  const [auth, setAuth] = useState({});
  return (
    <AuthContext.Provider value={{ auth, setAuth }}>
      {children}
    </AuthContext.Provider>
  );
}

export default AuthContext;
