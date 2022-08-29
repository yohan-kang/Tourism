import React, { SyntheticEvent, useEffect, useState } from "react";
import { useLocation, useNavigate, useParams } from "react-router-dom";
import useFetchPrivate from "../hooks/useFetchPrivate";
import { IBoard } from "../interfaces/IBoard";

function BoardDetail() {
  const { id } = useParams();
  const fetchPrivate = useFetchPrivate();
  const [board, setBoard] = useState<IBoard>();
  const navigate = useNavigate();
  const location: any = useLocation();
  const [errMsg, setErrMsg] = useState("");
  const from = location.state?.from?.pathname || "/boards";
  useEffect(() => {
    let isMounted = true;
    const getBoard = async () => {
      try {
        const response = await fetchPrivate.get(`/boards/writer2/${id}/`);
        isMounted && setBoard(response.data);
        // setTitle(response.data.title);
        // setContent(response.data.content);
      } catch (error) {
        navigate("/boards", { state: { from: location }, replace: true });
      }
    };

    getBoard();
  }, []);

  const submit = async (e: SyntheticEvent) => {
    e.preventDefault();

    try {
      const response = await fetchPrivate.put(
        `/boards/writer2/${board?.id}/`,
        JSON.stringify(board),
        {
          headers: { "Content-Type": "application/json" },
          withCredentials: true,
        }
      );
      console.log("response");
      console.log(response);
      navigate(from, { replace: true });
    } catch (err: any) {
      if (!err?.response) {
        setErrMsg("No Server Response");
      } else if (err.response?.status === 400) {
        setErrMsg("Missing Title or Content");
      } else if (err.response?.status === 401) {
        setErrMsg("Invalid Title or Content");
      } else {
        setErrMsg("Creation Failed");
      }

      // errRef?.current?.focus();
    }
  };

  return (
    <>
      <div className="main-container">
        <div className="container small-container">
          <h1 className="board-detail-title">Board Detail</h1>
          <form onSubmit={submit} className="board-form">
            <div className="board-input-group">
              <label>Title</label>
              <input
                name="title"
                type="text"
                value={board?.title || ""}
                onChange={(e) =>
                  setBoard((prev: any) => {
                    return { ...prev, title: e?.target?.value };
                  })
                }
                required
              />
            </div>
            <div className="board-input-group">
              <label>Content</label>
              <textarea
                rows={5}
                name="content"
                value={board?.content || ""}
                onChange={(e) =>
                  setBoard((prev: any) => {
                    return { ...prev, content: e?.target?.value };
                  })
                }
                required
              />
            </div>
            <div className="board-input-group">
              <label>Created At</label>
              <input
                type="datetime-local"
                name="created_at"
                value={
                  board?.created_at?.substring(
                    0,
                    board?.created_at ? board?.created_at?.length - 9 : 1
                  ) || ""
                }
                disabled
              />
            </div>
            <div className="board-input-group">
              <label>Updated At</label>
              <input
                type="datetime-local"
                name="updated_at"
                value={
                  board?.updated_at?.substring(
                    0,
                    board?.updated_at ? board?.updated_at?.length - 9 : 1
                  ) || ""
                }
                disabled
              />
            </div>
            <button type="submit" className="button">
              Update
            </button>
          </form>
        </div>
      </div>
    </>
  );
}

export default BoardDetail;
