export default interface IBoards {
  boards: Array<IBoard>;
}

export interface IImage {
  image_name: string;
  image_url: string;
}

export interface IBoard {
  id: number;
  title: string;
  writer: string;
  content: string;
  created_at?: string;
  updated_at?: string;
  img_list: Array<IImage>;
}

export const boardColumns = ["title", "writer"];
