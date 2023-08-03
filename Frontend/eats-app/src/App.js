import ResterauntPage from './pages/ResterauntPage/ResterauntPage.js';
import LoginPage from './pages/LoginPage/LoginPage.js';
import { BrowserRouter, Routes, Route } from 'react-router-dom';

function App() {
  return (
    <BrowserRouter>
      <Routes>
        <Route path="/resteraunts" element={<ResterauntPage/>}/>
        <Route path="/login" element={<LoginPage/>}/>
      </Routes>
    </BrowserRouter>
  );
}

export default App;
