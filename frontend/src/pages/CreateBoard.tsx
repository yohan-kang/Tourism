import React, { SyntheticEvent, useEffect, useRef, useState } from "react";
import { useLocation, useNavigate } from "react-router-dom";
import useAuth from "../hooks/useAuth";
import useFetchPrivate from "../hooks/useFetchPrivate";
import IFetch from "../interfaces/IFetch";
type Props = {};

const CreateBoard = (props: Props) => {
  const { auth, setAuth } = useAuth();
  const fetchPrivate: IFetch = useFetchPrivate();
  const titleRef: any = useRef();
  const contentRef: any = useRef();
  const errRef: any = useRef();
  const [title, setTitle] = useState("");
  const [content, setContent] = useState("");
  const [errMsg, setErrMsg] = useState("");
  const navigate = useNavigate();
  const location: any = useLocation();
  const from = location.state?.from?.pathname || "/boards";

  useEffect(() => {
    setErrMsg("");
  }, [title, content]);

  const submit = async (e: SyntheticEvent) => {
    e.preventDefault();

    try {
      const response = await fetchPrivate.post(
        "/boards/writer2/",
        JSON.stringify({ title, content }),
        {
          headers: { "Content-Type": "application/json" },
          withCredentials: true,
        }
      );
      console.log("response");
      console.log(response);
      setTitle("");
      setContent("");
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

      errRef?.current?.focus();
    }
  };

  return (
    <div className="main-container">
      <div className="container small-container">
        <h1>Create board</h1>
        <p ref={errRef} className="board-errmsg">
          {errMsg}
        </p>
        <form onSubmit={submit} className="board-form">
          <div className="board-input-group">
            <label>Title</label>
            <input
              name="title"
              type="text"
              value={title}
              onChange={(e) => setTitle(e.target.value)}
              required
            />
          </div>
          <div className="board-input-group">
            <label>Content</label>
            <textarea
              name="content"
              rows={5}
              value={content}
              onChange={(e) => setContent(e.target.value)}
              required
            />
          </div>
          <button type="submit" className="button">
            Create
          </button>
        </form>
      </div>
    </div>
  );
};

export default CreateBoard;
