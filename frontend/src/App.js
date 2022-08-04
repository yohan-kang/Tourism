
import './App.css';
import { BrowserRouter as Router, Routes,Route } from 'react-router-dom';
// import moduleName from './'
import HomePage from './pages/HomePage';
import LoginPage from './pages/LoginPage';
import Header from './components/Header'


function App() {
  return (
    <div className="App">
      <Router>
        {/* <Routes component={HomePage} path="/"/>
        <Routes component={LoginPage} path="/login"/> */}
        <Header />
        <Routes>
          <Route path="/" element={<HomePage />} />
          <Route path="/login" element={<LoginPage />} />
        </Routes>
      </Router>
    </div>
  );
}

export default App;
