import styles from './TodoItem.module.css';
// import PropTypes from 'prop-types'


function TodoItem({ todo, index, deleteTodo, }) {
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
// TodoItem.propTypes = {
//     todo: PropTypes.object.isRequired,
//     index: PropTypes.number.isRequired,
//     deleteTodo: PropTypes.func.isRequired,
// }

export default TodoItem;