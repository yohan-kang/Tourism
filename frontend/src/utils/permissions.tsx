import React from "react";
import IToken from "../interfaces/IToken";
import jwt_decode from "jwt-decode"; // import dependency

const hasPermission = (accessToken: string, allowedRoles: Array<string>) => {
  const decoded: IToken = jwt_decode(accessToken);
  return decoded?.permissions?.find((role: string) =>
    allowedRoles?.includes(role)
  );
};

export default hasPermission;

export const PERMISSIONS = {
  Board_view: "board.view_board",
  Board_create: "board.add_board",
};
