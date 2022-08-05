import { Route, Redirect } from 'react-router-dom'

const PrivateRoute = ({children, ...rest}) => {
  const authenticated = false
  console.log('Private route works')
  return(
      // <Route {...rest}>{children}</Route>
      <Route {...rest}>{!authenticated ? <Redirect to="/login"/> :  children}</Route>
  )

}

export default PrivateRoute

// function PrivateRoute({children, ...rest}) {
//   console.log('Private route works')
//   return (
//     <Route {...rest}>{children}</Route>
//   )
// }
