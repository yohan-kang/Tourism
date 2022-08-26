export default interface IBoards {
  boards: Array<IBoard>;
}

export interface IBoard {
  id: number;
  title: string;
  writer: string;
  content: string;
}

export const boardColumns = ["title", "writer"];
