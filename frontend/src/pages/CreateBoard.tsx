import React, { SyntheticEvent, useEffect, useRef, useState } from "react";
import { useLocation, useNavigate } from "react-router-dom";
import useAuth from "../hooks/useAuth";
import useFetchPrivate from "../hooks/useFetchPrivate";
import IFetch from "../interfaces/IFetch";
import Form, { InputType } from "../components/Form";
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

  const inputs: Array<InputType> = [
    {
      key: "title",
      name: "title",
      type: "text",
      label: "Title",
      config: {
        required: true,
        disabled: false,
      },
      value: title,
      handleChange: setTitle,
    },
    {
      key: "content",
      name: "content",
      type: "textarea",
      label: "Content",
      config: {
        required: true,
        disabled: false,
        rows: 5,
      },
      value: content,
      handleChange: setContent,
    },
  ];
  useEffect(() => {
    setErrMsg("");
  }, [title, content]);

  const submit = async (e: SyntheticEvent) => {
    e.preventDefault();

    try {
      const response = await fetchPrivate.post(
        "/boards/",
        JSON.stringify({ title, content }),
        {
          headers: { "Content-Type": "application/json" },
          withCredentials: true,
        }
      );
      setTitle("");
      setContent("");
      navigate(from, { replace: true });
    } catch (err: any) {
      if (!err?.response) {
        setErrMsg("No Server Response");
      } else if (err.response?.status === 400) {
        console.log(err);
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
        <Form
          submit={submit}
          inputs={inputs}
          button="Create"
          handleChange={null}
          data={{ title, content }}
        />
      </div>
    </div>
  );
};

export default CreateBoard;
