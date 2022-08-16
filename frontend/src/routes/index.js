import React from 'react';
import HomePage from '../pages/HomePage.js'
import LoginPage from '../pages/LoginPage.js'
import { BrowserRouter as Router,Route } from 'react-router-dom';
// import moduleName from './'
import PrivateRoute from '../utils/PrivateRoute'
import {AuthProvider} from '../context/AuthContext'
import Header from '../components/Header'

const Routes = () => (
  <Router>
    <AuthProvider>
      <Header />
      <PrivateRoute component={HomePage} path="/"/>
      <Route component={LoginPage} path="/login"/>
    </AuthProvider>
  </Router>
)
export default Routes
