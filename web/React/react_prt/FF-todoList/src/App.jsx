import { useState, useEffect, useRef } from 'react'

import TodoForm from './components/TodoForm/TodoForm'
import TodoList from './components/TodoList/TodoList'
import styles from './App.module.css'


function App() {
  const [todos, setTodos] = useState([])
  const isOnMounted = useRef(true)

  useEffect(() => {
    const storedTodos = localStorage.getItem('todos')
    if (storedTodos) {
        const parsedTodos = JSON.parse(storedTodos)
        console.log(parsedTodos)
        setTodos(parsedTodos)
    }
    // isOnMounted.current = false
  }, [])

  useEffect(() => {
    if (isOnMounted.current) {
        isOnMounted.current = false
    } else {
        localStorage.setItem('todos', JSON.stringify(todos))
    }
  }, [todos])
  
  const createTodo = (newTodoText) => {
    const newTodo = {
      text: newTodoText,
      created_at: new Date().toLocaleString().slice(6),
    }
    setTodos([...todos, newTodo])
  }
  const deleteTodo = (deleteIndex) => {
    setTodos(todos.filter((_, index) => index !== deleteIndex))
  }
  
  return (
    <div>
      <header className={styles.header}>
        <h1>나의 Todo List</h1>
      </header>
      <main className={styles.main}>
        <div>
          <TodoForm 
            createTodo = {createTodo}
          />
        </div>
        <div>
          <TodoList
            todos={todos}
            deleteTodo={deleteTodo}
          />
        </div>
      </main>
    </div>
  )
}

export default App;
