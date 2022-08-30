import React from "react";

export interface InputType {
  key: string | number;
  name: string;
  type: string;
  label: string;
  config?: {
    required?: boolean;
    disabled?: boolean;
    rows?: number;
  };
  value: any;
  handleChange?: any;
  src?: string;
}

type Props = {
  submit: any;
  handleChange: any;
  inputs: Array<InputType>;
  button: string;
  data: any;
};

function Form({ submit, handleChange, inputs, button, data }: Props) {
  return (
    <form onSubmit={submit} className="form">
      {inputs.map((input: InputType) => {
        return (
          <div key={input.key ?? null} className="input-group">
            <label>{input.label ?? null}</label>
            {input.type === "textarea" ? (
              <textarea
                name={input.name || ""}
                value={data?.[input.name] || ""}
                onChange={
                  input.handleChange
                    ? (e) => input.handleChange(e?.target?.value)
                    : (e) =>
                        handleChange((prev: any) => {
                          const next: any = { ...prev };
                          next[input.name] = e?.target?.value;
                          return next;
                        })
                }
                {...(input.config ? input.config : null)}
              />
            ) : (
              <input
                type={input.type || ""}
                name={input.name || ""}
                value={
                  input.type === "datetime-local"
                    ? data?.[input.name]?.substring(
                        0,
                        data?.[input.name] ? data?.[input.name]?.length - 9 : 1
                      ) || ""
                    : data?.[input.name] || ""
                }
                onChange={
                  input.handleChange
                    ? (e) => input.handleChange(e?.target?.value)
                    : (e) =>
                        handleChange((prev: any) => {
                          const next: any = { ...prev };
                          next[input.name] = e?.target?.value;
                          return next;
                        })
                }
                {...input.config}
              />
            )}
          </div>
        );
      })}
      <button type="submit" className="button">
        {button}
      </button>
    </form>
  );
}

export default Form;
