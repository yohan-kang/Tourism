import React, { useEffect, useState } from "react";
import { useLocation, useNavigate, useParams } from "react-router-dom";
import useFetchPrivate from "../hooks/useFetchPrivate";
import { IBoard } from "../interfaces/IBoard";

function BoardDetail() {
  const { id } = useParams();
  const fetchPrivate = useFetchPrivate();
  const [board, setBoard] = useState<IBoard>();
  const navigate = useNavigate();
  const location = useLocation();
  useEffect(() => {
    let isMounted = true;
    const getBoard = async () => {
      try {
        const response = await fetchPrivate.get(`/boards/writer2/${id}/`);
        isMounted && setBoard(response.data);
      } catch (error) {
        navigate("/boards", { state: { from: location }, replace: true });
      }
    };

    getBoard();
  }, []);
  return (
    <>
      <h1>Title : {board?.title}</h1>
      <h2>Writer : {board?.writer}</h2>
      <p>{board?.content}</p>
    </>
  );
}

export default BoardDetail;
