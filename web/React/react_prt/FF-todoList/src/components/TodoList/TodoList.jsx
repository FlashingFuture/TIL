import TodoItem from "./TodoItem/TodoItem";


function TodoList({todos}) {
    todos.map(todo => {
        console.log(todo)
        return <TodoItem todo={todo} key={0} />
    })
}

export default TodoList;