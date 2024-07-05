import styles from './TodoItem.module.css';


function TodoItem({todo}) {
    console.log("TodoItem 렌더링")
    return (
        <div className={styles.card}>
            <p>등록 시간 : </p>
            <p>{todo}</p>
        </div>
    )
}

export default TodoItem;