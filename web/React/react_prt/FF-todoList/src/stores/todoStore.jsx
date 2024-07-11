import { create } from 'zustand'

const useTodoStore = create((set) => ({
    todos: [],
    createTodo: (newTodo) => set(
        (state) => ({ todos: state.todos.push(newTodo)})
    ),
    deleteTodo: (deleteIndex) => set(
        (state) => ({ todos: state.todos.filter((todo) => {
            todo.index !== deleteIndex
        })})
    )
}));

export default useTodoStore;
