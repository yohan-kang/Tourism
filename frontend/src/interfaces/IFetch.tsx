interface IFetchGet {
  (url: string, config?: any): any;
}

interface IFetchPost {
  (url: string, data: any, config?: any): any;
}
interface IFetchPut {
  (url: string, data: any, config?: any): any;
}

export default interface IFetch {
  get: IFetchGet;
  post: IFetchPost;
  put: IFetchPut;
}
