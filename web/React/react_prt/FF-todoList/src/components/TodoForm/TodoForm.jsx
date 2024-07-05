import { useRef } from "react";


function TodoForm({addTodo}) {
    const newTodo = useRef();
    const todoSubmit = (e) => {
        e.preventDefault();
        addTodo(newTodo.current.value);
        newTodo.current.value = "";
    }


    return (
        <div>
            <form onSubmit={todoSubmit}>
                <label htmlFor="getTodo">할 일 추가: </label>
                <input type="text" id="getTodo" ref={newTodo} />
                <input type="submit" value="할 일 추가" />
            </form>
        </div>
    );
}

export default TodoForm;