import React from 'react'
import { useDispatch,useSelector } from 'react-redux';
import {logout,selectUser} from '../Features/UserSlice';
import { useNavigate } from 'react-router-dom';
import { useEffect } from 'react';

const Logout = () => {
    const user = useSelector(selectUser);
    const dispatch = useDispatch();
    const navigate = useNavigate()
    
    useEffect(() => {
  
      dispatch(logout());  //dispath the logout action
      navigate('/login')
      
      
    
      
    }, [])
    
     
    return null
  
  };
  
  export default Logout; 
