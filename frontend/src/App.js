import { BrowserRouter as Router, Route, Routes } from 'react-router-dom';
import Subscription from './components/Subscription';
import Logout from './components/Logout';
import UserDashboard from './components/UserDashboard';
import Register from './components/Register';
import Login from './components/Login';
import PrivateRoutes from "./Utils/PrivateRoutes";



function App() {
  return (

    <Router>
    <div>
      <Routes>

        <Route element={<PrivateRoutes/>} >

          <Route exact path="/" element={<Subscription/>} />
          <Route path="/Logout" element={<Logout/>}  />
          <Route path="/UserDashboard" element={<UserDashboard/>}  />

        </Route>

          <Route path="/Register" element={<Register/>}  />
          <Route path="/Login" element={<Login/>}  />

      </Routes>
      
    </div>
    </Router>
  );
}

export default App;
