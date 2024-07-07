import { useRef } from "react";
import styles from "./TodoForm.module.css"


function TodoForm({createTodo}) {
    const newTodo = useRef();
    const todoSubmit = (e) => {
        e.preventDefault();
        createTodo(newTodo.current.value);
        newTodo.current.value = "";
    }


    return (
        <div>
            <form className={styles.formWrapper} onSubmit={todoSubmit}>
                <label htmlFor="getTodo">할 일 추가 : </label>
                <input type="text" id="getTodo" ref={newTodo} />
                <input className={styles.button} type="submit" value="+" />
            </form>
        </div>
    );
}

export default TodoForm;