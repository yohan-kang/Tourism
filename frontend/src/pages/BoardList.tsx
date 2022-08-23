import React, { useState, useEffect, useContext } from "react";
import axios from "../api/axios";
import useRefreshToken from "../hooks/useRefreshToken";
import AuthContext from "../contexts/AuthContext";

type Props = {};

interface IBoard {
  boards: {
    title: string;
  }[];
}

function BoardList({}: Props) {
  const [boards, setBoards] = useState<IBoard["boards"]>([]);
  const refresh = useRefreshToken();
  const { auth, setAuth } = useContext(AuthContext);

  useEffect(() => {
    let isMounted = true;
    const controller = new AbortController();

    const getBoards = async () => {
      console.log("getBoard");
      try {
        const response = await axios.get("/boards/writer2/", {
          signal: controller.signal,
          headers: {
            "Content-Type": "application/json",
            Authorization: `Bearer ${auth.accessToken}`,
          },
        });
        console.log(response.data);
        if (isMounted) setBoards(response.data);
      } catch (error) {
        console.error(error);
      }
    };

    getBoards();

    return () => {
      isMounted = false;
      controller.abort();
    };
  }, [auth.accessToken]);

  return (
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
        <button onClick={() => refresh(auth.refreshToken)}>Refresh</button>
        <br />
      </article>
    </div>
  );
}

export default BoardList;
