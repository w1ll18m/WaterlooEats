import PageRoutes from './routes/PageRoutes.js';
import NavBar from './routes/NavBar.js';
import { BrowserRouter, Routes, Route } from 'react-router-dom';
import { AuthProvider } from './providers/AuthProvider.js';

function App() {
  return (
    <AuthProvider>
      <BrowserRouter>
        <NavBar/>
        <PageRoutes/>
      </BrowserRouter>
    </AuthProvider>
  );
}

export default App;
