import { Route, Redirect } from 'react-router-dom'
import { useContext } from 'react'
import AuthContext from '../context/AuthContext'

const PrivateRoute = ({children, ...rest}) => {
  // const authenticated = false
  let {user} = useContext(AuthContext)
  // console.log('Private route works')
  return(
      // <Route {...rest}>{children}</Route>
      <Route {...rest}>{!user ? <Redirect to="/login"/> :  children}</Route>
      // <Route {...rest}>{!user ? <Redirect to="/login" /> :  children}</Route>
  )

}

export default PrivateRoute

// function PrivateRoute({children, ...rest}) {
//   console.log('Private route works')
//   return (
//     <Route {...rest}>{children}</Route>
//   )
// }
