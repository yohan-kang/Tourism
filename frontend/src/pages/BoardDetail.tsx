import React, { SyntheticEvent, useEffect, useState } from "react";
import { useLocation, useNavigate, useParams } from "react-router-dom";
import Form, { InputType } from "../components/Form";
import { IBoard, IImage } from "../interfaces/IBoard";
import { useFetchPrivate } from "../utils/myFetch";

function BoardDetail() {
  const { id } = useParams();
  const fetchPrivate = useFetchPrivate();
  const [board, setBoard] = useState<IBoard>();
  const navigate = useNavigate();
  const location: any = useLocation();
  const [errMsg, setErrMsg] = useState("");
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
      value: board?.title || null,
    },
    {
      key: "writer",
      name: "writer",
      type: "text",
      label: "Writer",
      config: {
        required: false,
        disabled: true,
      },
      value: board?.writer || null,
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
      value: board?.content || null,
    },
    {
      key: "created_at",
      name: "created_at",
      type: "datetime-local",
      label: "Created at",
      config: {
        required: false,
        disabled: true,
      },
      value:
        board?.created_at?.substring(
          0,
          board?.created_at ? board?.created_at?.length - 9 : 1
        ) || "",
    },
    {
      key: "updated_at",
      name: "updated_at",
      type: "datetime-local",
      label: "Updated at",
      config: {
        required: false,
        disabled: true,
      },
      value:
        board?.updated_at?.substring(
          0,
          board?.updated_at ? board?.updated_at?.length - 9 : 1
        ) || "",
    },
  ];
  useEffect(() => {
    let isMounted = true;
    const getBoard = async () => {
      try {
        const response = await fetchPrivate.get(`/boards/${id}/`);
        isMounted && setBoard(response.data);
        // setTitle(response.data.title);
        // setContent(response.data.content);
      } catch (error) {
        navigate("/boards", { state: { from: location }, replace: true });
      }

      // for (const i in board?.img_list) {
      //   inputs.push({
      //     key: `img_${i}`,
      //     name: `${board?.img_list[0].image_name}`,
      //     type: "img",
      //     label: "Image",
      //     src: `http://localhost:8000${board?.img_list[0].image_url || null}}`,
      //     value: null,
      //   });
      // }
    };

    getBoard();
  }, []);

  const submit = async (e: SyntheticEvent) => {
    e.preventDefault();

    try {
      const response = await fetchPrivate.put(
        `/boards/${board?.id}/`,
        JSON.stringify(board),
        {
          headers: { "Content-Type": "application/json" },
          withCredentials: true,
        }
      );
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
          <div></div>
          <Form
            submit={submit}
            handleChange={setBoard}
            inputs={inputs || null}
            data={board}
            button="Update"
          />
        </div>
        <div className="container large-container">
          <div className="grid-container">
            {board?.img_list.map((img: IImage, id: number) => {
              return (
                <div key={id} className="grid-item">
                  <img
                    src={`http://localhost:8000${img.image_url}`}
                    alt={img.image_name}
                  />
                </div>
              );
            })}
          </div>
        </div>
      </div>
    </>
  );
}

export default BoardDetail;
