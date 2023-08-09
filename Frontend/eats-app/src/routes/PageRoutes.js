import ResterauntPage from '../pages/ResterauntPage/ResterauntPage.js';
import LoginPage from '../pages/LoginPage/LoginPage.js';
import LegacySignupPage from '../pages/SignupPage/LegacySignupPage.js';
import SignupPage from '../pages/SignupPage/SignupPage.js';
import Auth0RedirectHandler from './Auth0Redirect.js';
import { Routes, Route } from 'react-router-dom';
import ProtectedRoute from './ProtectedRoute.js';

const PageRoutes = () => {
    return(
        <Routes>
          <Route path="/resteraunts" element={<ResterauntPage/>}/>
          <Route path="/login" element={<LoginPage/>}/>
          <Route path="/sign-up" element={<LegacySignupPage/>}/>
          <Route path="/complete-sign-up" element={<SignupPage/>}/>
          <Route path="/auth0/authorization-handler" element={<Auth0RedirectHandler/>}/>
        </Routes>
    )
}

export default PageRoutes