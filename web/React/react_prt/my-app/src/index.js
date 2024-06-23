import React from 'react';
import { createRoot } from 'react-dom/client';
import './index.css';
import App from './App';
import reportWebVitals from './reportWebVitals';

import Library from './ch_3/Library';
import Clock from './ch_4/clock';
import CommentList from './ch_5/CommentList';
import UpdateScreen from './state_event/UpdateScreen';

const root = createRoot(document.getElementById("root"));

root.render(
  <React.StrictMode>
    <UpdateScreen />
  </React.StrictMode>
);

// If you want to start measuring performance in your app, pass a function
// to log results (for example: reportWebVitals(console.log))
// or send to an analytics endpoint. Learn more: https://bit.ly/CRA-vitals
reportWebVitals();
