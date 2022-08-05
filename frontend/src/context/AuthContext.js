import { createContext, useState, userEffect } from 'react'
import jwt_decode from 'jwt-decode'
import { useHistory } from 'react-router-dom'

const AuthContext = createContext()

export default AuthContext;

export const AuthProvider = ({children}) => {
  
  // LocalStorge.getItem('authTokens')
  let [authTokens, setAuthTokens] =useState(null)
  let [user, setUser] = useState(null)

  const history = useHistory()

  let loginUser = async (e )=> {
      e.preventDefault()
      let response = await fetch('http://127.0.0.1:8000/api/token/', {
        method : 'POST',
        headers:{
            'Content-Type':'application/json'
        },
        body:JSON.stringify({'username':e.target.username.value,'password':e.target.password.value})
      })
      let data = await response.json()
      // console.log('data:',data)
      // console.log('response:',response)
      if(response.status === 200){
          setAuthTokens(data)
          setUser(jwt_decode(data.access))
          localStorage.setItem('authTokens',JSON.stringify(data))
          history.push('/')
      }else {
        alert('something wnt wrong!')
      }
    }
  let contextData = {
      user:user,
      loginUser:loginUser
  }

  return (
    // <AuthContext.Provider value={{'name':'yohan'}} >
      <AuthContext.Provider value={contextData} >
          {children}
      </AuthContext.Provider>
  )
}