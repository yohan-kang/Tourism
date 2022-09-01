import axios, { useAxiosPrivate } from "../api/axios";

interface IFetchGet {
  (url: string, config?: any): any;
}

interface IFetchPost {
  (url: string, data: any, config?: any): any;
}
interface IFetchPut {
  (url: string, data: any, config?: any): any;
}

export interface IFetch {
  get: IFetchGet;
  post: IFetchPost;
  put: IFetchPut;
}

class Fetch implements IFetch {
  fetch: IFetch;
  constructor(fetchApi: IFetch) {
    this.fetch = fetchApi;
  }

  get(url: string, config?: any): any {
    return this.fetch.get(url, config);
  }

  post(url: string, data: any, config?: any): any {
    return this.fetch.post(url, data, config);
  }

  put(url: string, data: any, config?: any): any {
    return this.fetch.put(url, data, config);
  }
}

const myFetch: IFetch = new Fetch(axios);

export default myFetch;

export function useFetchPrivate(): IFetch {
  return useAxiosPrivate();
}
