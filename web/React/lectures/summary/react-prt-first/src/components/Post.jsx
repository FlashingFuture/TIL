const names = ['Tae-ho', 'Jeon']

function Post() {
    const chooseName = Math.random() > 0.5 ? names[0] : names[1];


    return <div>
        <p>{chooseName}</p>
        <p>Better use React.js</p>
    </div>;
}

export default Post;