import React from 'react';
import ReactDOM from 'react-dom/client';
import App from './App';
import { Auth0Provider } from "@auth0/auth0-react"
import { ToastContainer } from 'react-toastify';
import 'react-toastify/dist/ReactToastify.css';
import 'bootstrap/dist/css/bootstrap.css'

const domain = process.env.REACT_APP_AUTH0_DOMAIN
const client_id = process.env.REACT_APP_AUTH0_CLIENT_ID

// redirectURI is url that auth0 should redirect after authentication
// onRedirectCallback is the function that should be called after authentication

const root = ReactDOM.createRoot(document.getElementById('root'));
root.render(
  <React.StrictMode>
    <Auth0Provider domain={domain} clientId={client_id} redirectUri="http://localhost:3000/auth0/authorization-handler">
      <App />
    </Auth0Provider>
    <ToastContainer />
  </React.StrictMode>
);