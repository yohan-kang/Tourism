import React, { useState, useEffect } from "react";
import useAxiosPrivate from "../hooks/useAxiosPrivate";
import { useLocation, useNavigate } from "react-router-dom";
import Header from "../components/Header";

interface IBoard {
  boards: {
    title: string;
  }[];
}

function BoardList() {
  const [boards, setBoards] = useState<IBoard["boards"]>([]);
  const axiosPrivate = useAxiosPrivate();

  const navigate = useNavigate();
  const location = useLocation();

  useEffect(() => {
    let isMounted = true;

    const getBoards = async () => {
      try {
        const response = await axiosPrivate.get("/boards/writer2/", {});
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
                return <li key={i}>{board?.title}</li>;
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
