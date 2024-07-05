import { useState } from 'react'
import TodoForm from './components/TodoForm/TodoForm'
import TodoList from './components/TodoList/TodoList'

function App() {
  const [todos, setTodos] = useState([])
  const addTodo = (newTodo) => {
    setTodos([...todos, newTodo])
    console.log(todos)
  }
  
  return (
    <>
      <div>
        <h1>나의 Todo List</h1>
      </div>
      <div>
        <TodoForm 
          todos={todos}
          addTodo = {addTodo}
        />
      </div>
      <div>
        <TodoList
          todos={todos}
        />
      </div>
    </>
  )
}

export default App
