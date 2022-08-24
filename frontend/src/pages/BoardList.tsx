import React, { useState, useEffect } from "react";
import { Link, useLocation, useNavigate } from "react-router-dom";
import IFetch from "../interfaces/IFetch";
import useFetchPrivate from "../hooks/useFetchPrivate";
import IBoards from "../interfaces/IBoard";

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
      <div>
        <h1>BoardList</h1>
        <article>
          {boards?.length ? (
            <ul>
              {boards.map((board, i) => {
                return (
                  <li key={i}>
                    <Link to={`/boards/${board.id}`}>
                      {board?.title} - {board?.writer}
                    </Link>
                  </li>
                );
              })}
            </ul>
          ) : (
            <p>No boards to display</p>
          )}
          <br />
        </article>
      </div>
    </>
  );
}

export default BoardList;
