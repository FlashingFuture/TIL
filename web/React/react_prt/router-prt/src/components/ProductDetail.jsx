import { useParams } from "react-router-dom";


function ProductDetailPage() {
    const params = useParams();

    params.productId;

    return (
    <>
        <h3>상세정보</h3>
        <p>{params.productId}</p>
    </>
    );
}

export default ProductDetailPage;