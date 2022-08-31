import React, { useState, useEffect } from "react";
import { Link, useLocation, useNavigate } from "react-router-dom";
import IBoards from "../interfaces/IBoard";
import { IFetch, useFetchPrivate } from "../utils/myFetch";

function BoardList() {
  const [boards, setBoards] = useState<IBoards["boards"]>([]);
  const fetchPrivate: IFetch = useFetchPrivate();
  const navigate = useNavigate();
  const location = useLocation();

  useEffect(() => {
    let isMounted = true;

    const getBoards = async () => {
      try {
        const response = await fetchPrivate.get("/boards/");
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
      <div className="main-container">
        <div className="container large-container">
          <h1 className="boardlist-title">BoardList</h1>
          <div className="boardlist-toolbar">
            <button className="button">Filter</button>
            <Link to="newBoard">
              <button className="button">Add Board</button>
            </Link>
          </div>
          <table className="boardlist-table">
            <thead>
              <tr>
                <th>Title</th>
                <th>Created At</th>
                <th>Updated At</th>
              </tr>
            </thead>
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
                      <td>{board.title}</td>
                      <td>{board.created_at}</td>
                      <td>{board.updated_at}</td>
                    </tr>
                  );
                })}
              </tbody>
            ) : null}
          </table>
        </div>
      </div>
    </>
  );
}

export default BoardList;
