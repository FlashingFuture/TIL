import TodoItem from "./TodoItem/TodoItem";


function TodoList({ todos, deleteTodo }) {
    return (
        <div>
            {todos.map((todo, index) => (
                <TodoItem 
                    todo={todo} 
                    deleteTodo={deleteTodo} 
                    key={index}
                    index={index}
                />
            ))}
        </div>
    );
}

export default TodoList;