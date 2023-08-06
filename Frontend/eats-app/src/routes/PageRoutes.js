import ResterauntPage from '../pages/ResterauntPage/ResterauntPage.js';
import LoginPage from '../pages/LoginPage/LoginPage.js';
import SignupPage from '../pages/SignupPage/SignupPage.js';
import { Routes, Route } from 'react-router-dom';
import ProtectedRoute from './ProtectedRoute.js';

const PageRoutes = () => {
    return(
        <Routes>
          <Route path="/resteraunts" element={<ResterauntPage/>}/>
          <Route path="/login" element={<LoginPage/>}/>
          <Route path="/sign-up" element={<SignupPage/>}/>
        </Routes>
    )
}

export default PageRoutes