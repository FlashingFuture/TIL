import { NavLink } from "react-router-dom";

function MainNavigation() {
    return (
        <>
            <header>
                <NavLink to="/" end>홈</NavLink> | &nbsp;
                <NavLink to="/products">물건 목록</NavLink>
            </header>
        </>
    );
}

export default MainNavigation;