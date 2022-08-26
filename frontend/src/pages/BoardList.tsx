import React, { useState, useEffect } from "react";
import { Link, useLocation, useNavigate } from "react-router-dom";
import IFetch from "../interfaces/IFetch";
import useFetchPrivate from "../hooks/useFetchPrivate";
import IBoards, { boardColumns, IBoard } from "../interfaces/IBoard";

function BoardList() {
  const [boards, setBoards] = useState<IBoards["boards"]>([]);
  const fetchPrivate: IFetch = useFetchPrivate();

  const navigate = useNavigate();
  const location = useLocation();

  useEffect(() => {
    let isMounted = true;

    const getBoards = async () => {
      try {
        const response = await fetchPrivate.get("/boards/writer2/");
        isMounted && setBoards(response.data);
      } catch (error) {
        console.error(error);
        navigate("/login", { state: { from: location }, replace: true });
      }
    };

    getBoards();

    return () => {
      isMounted = false;
    };
  }, []);

  return (
    <>
      <div className="container">
        <h1 className="boardlist-title">BoardList</h1>
        <table className="boardlist-table">
          {boardColumns?.length ? (
            <thead>
              <tr>
                {boardColumns.map((column, id) => {
                  return <th key={id}>{column}</th>;
                })}
              </tr>
            </thead>
          ) : null}
          {boards?.length ? (
            <tbody>
              {boards.map((board: any, id) => {
                return (
                  <tr
                    key={board.id}
                    onClick={() => {
                      navigate(`/boards/${board.id}`);
                    }}
                  >
                    {/* <Link to={`/boards/${row.id}`}> */}
                    {boardColumns.map((column: string, id) => {
                      return <td key={id}>{board[column]}</td>;
                    })}
                  </tr>
                );
              })}
            </tbody>
          ) : null}
        </table>
      </div>
    </>
  );
}

export default BoardList;
