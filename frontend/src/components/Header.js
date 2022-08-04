import React from 'react'
import { Link } from 'react-router-dom'

// const Header = () => {
//   return (
//     <div>
//         <Link to="/">HOME</Link>
//         <span> | </span>
//         <Link to="/login">Login</Link>
//     </div>
//   )
// }

function  Header () {
  return (
    <div>
        <Link to="/">HOME</Link>
        <span> | </span>
        <Link to="/login">Login</Link>
    </div>
  )
}
export default Header