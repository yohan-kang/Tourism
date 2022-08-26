import IFetch from "../interfaces/IFetch";
import axios from "../api/axios";

export class Fetch implements IFetch {
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
}

const myFetch: IFetch = new Fetch(axios);

export default myFetch;
