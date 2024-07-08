import { Outlet } from "react-router-dom";

import MainNavigation from "../components/MainNavigation";

function RootLayout() {
    return (
        <>
            <MainNavigation />
            <Outlet></Outlet>
        </>
    );
}

export default RootLayout;