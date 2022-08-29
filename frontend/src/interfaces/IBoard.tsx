export default interface IBoards {
  boards: Array<IBoard>;
}

export interface IBoard {
  id: number;
  title: string;
  writer: string;
  content: string;
  created_at?: string;
  updated_at?: string;
}

export const boardColumns = ["title", "writer"];
