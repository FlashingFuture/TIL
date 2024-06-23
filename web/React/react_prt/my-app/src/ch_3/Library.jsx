import React from "react";
import Book from "./Book";

function Library(props) {
  return (
    <div>
      <Book name="음성인식 기반 스마트 선반 시스템" numOfPage={27}/>
    </div>
  )
}

export default Library;