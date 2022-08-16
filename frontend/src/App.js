
import './App.css';
import { BrowserRouter as Router,Route } from 'react-router-dom';
// import moduleName from './'
import PrivateRoute from './utils/PrivateRoute'

import {AuthProvider} from './context/AuthContext'
import Routes from './routes'
import HomePage from './pages/HomePage';
import LoginPage from './pages/LoginPage';
import Header from './components/Header'

const App = () => <Routes/>;
export default App
