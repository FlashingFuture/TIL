import styles from './TodoItem.module.css';


function TodoItem({ todo, index, deleteTodo }) {
    return (
        <div className={styles.card}>
            <div>
                <button className={styles.button} onClick={() => deleteTodo(index)}>x</button>
            </div>
            <div>
                <p>{todo.created_at}</p>
                <p>{todo.text}</p>
            </div>
        </div>
    )
}

export default TodoItem;