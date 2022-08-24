interface IFetchGet {
  (url: string, config?: {}): any;
}

interface IFetchPost {
  (url: string, data: any, config?: any): any;
}

export default interface IFetch {
  get: IFetchGet;
  post: IFetchPost;
}
