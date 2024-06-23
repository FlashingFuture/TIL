import React from "react";

const Clock = (props) => {
  return (
    <div>
      <h1>Hello, React!</h1>
      <h3>Local Time : {new Date().toLocaleTimeString()}</h3>
    </div>
  );
}

export default Clock;