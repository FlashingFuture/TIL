import { Link, useNavigate } from "react-router-dom";

function HomePage() {
    const navigate = useNavigate();

    function navigateHandler() {
        navigate('/products');
    }


    return (
        <>
            <h1>홈피에요</h1>
            <Link to="/products">물건 목록</Link>
            <p>
                <button onClick={navigateHandler}>튼</button>
            </p>
        </>
    );
}

export default HomePage;