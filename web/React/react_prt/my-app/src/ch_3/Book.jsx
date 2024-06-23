import React from "react";

function Book(props) {
  return (
    <div>
      <h1>{`도서명 : ${props.name}`}</h1>
      <h3>{`페이지 수 : ${props.numOfPage}`}</h3>
    </div>
  );

}

export default Book;