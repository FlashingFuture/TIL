import React from "react";
import Comment from "./Comment";

const comments = [
  { name: "정기영", comment: "리액트 댓글 구현"},
  { name: "정정기영", comment: "map 활용"}
]

function CommentList(props) {
  return (
    <div>
      {comments.map((comment) => {
        return (
          <Comment name={comment.name} comment={comment.comment} />
        )
      })}
    </div>
  );
}

export default CommentList;