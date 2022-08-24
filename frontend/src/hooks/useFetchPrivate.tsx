import React from "react";
import IFetch from "../interfaces/IFetch";
import useAxiosPrivate from "./useAxiosPrivate";

function useFetchPrivate(): IFetch {
  return useAxiosPrivate();
}

export default useFetchPrivate;
