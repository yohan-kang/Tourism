import React,{useContext} from 'react'
import { Link } from 'react-router-dom'
import AuthContext from '../context/AuthContext'

const Header = () => {
  let {user,logoutUser} = useContext(AuthContext)
  return (
    <div>
        <Link to="/">HOME</Link>
        <span> | </span>
        {user ? (
            <p onClick={logoutUser}>Logout</p>
        ): (
            <Link to="/login">Login</Link>
        )}

        {user && <p>Hello {user.username} </p>}
    </div>
  )
}
export default Header

// function  Header () {
//   let {name} = useContext(AuthContext)
//   return (
//     <div>
//         <Link to="/">HOME</Link>
//         <span> | </span>
//         <Link to="/login">Login</Link>
//         <p>Hello {name} </p>
//     </div>
//   )
// }
// export default Header