import { Link } from "react-router-dom";

function Products() {
    return (
        <>
            <p>물건들이에요</p>
            <ul>
                <li><Link to="/products/1">1</Link></li>
                <li><Link to="/products/2">2</Link></li>
                <li><Link to="/products/3">3</Link></li>
            </ul>
        </>
    );
}

export default Products;