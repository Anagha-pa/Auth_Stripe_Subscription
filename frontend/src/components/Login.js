import React from 'react'
import  { useState } from 'react'
import axios from 'axios';

const Login = () => {
    const[email,setEmail] =useState("");
    const[password,setPassword] = useState("");

    const handleSubmit = async (e) => {
        e.preventDefault();
        try{
          
          const response = await axios.post('http://127.0.0.1:8000/api/account/login/', {
            
              "email":email,
              "password":password,
            
      
          });
            console.log(response  );
          if(response.status===201){
            try{
              navigator("/user-dashboard")
    
            }catch(error){
              console.log(error.response);
            }
        }
    } catch (error) {
        console.error("Error in handleSubmit:", error);
      }
    };




  return (
    <div className="flex flex-col items-center justify-center h-screen">
        

      <div className=" max-w-sm" style={{width:"800px"}}>

        <form className="mb-8" onSubmit={handleSubmit}>
            
            
            <div className="mb-5">
              <label
                className="block mb-2 text-sm font-medium text-gray-900"
              >
                Email
              </label>
              <input
                type="email"
                id="email"
                className="bg-gray-50 border border-gray-300 text-gray-900 text-sm rounded-lg focus:ring-blue-500 focus:border-blue-500 block w-full p-2.5 dark:bg-gray-700 dark:border-gray-600 dark:placeholder-gray-400 dark:text-white dark:focus:ring-blue-500 dark:focus:border-blue-500"
                placeholder=""
                value={email}
                onChange={(e) => setEmail(e.target.value)}
                required
              />
            </div>

            <div className="mb-5">
            <label
              className="block mb-2 text-sm font-medium text-gray-900"
            >
              Password
            </label>
            <input
              type="password"
              id="Password"
              className="bg-gray-50 border border-gray-300 text-gray-900 text-sm rounded-lg focus:ring-blue-500 focus:border-blue-500 block w-full p-2.5 dark:bg-gray-700 dark:border-gray-600 dark:placeholder-gray-400 dark:text-white dark:focus:ring-blue-500 dark:focus:border-blue-500"
              placeholder=""
              value={password}
              onChange={(e) => setPassword(e.target.value)}
              required
            />
          </div>

          <button type="button" class="text-white bg-blue-700 hover:bg-blue-800 focus:ring-4 focus:ring-blue-300 font-medium rounded-lg text-sm px-5 py-2.5 me-2 mb-2 dark:bg-blue-600 dark:hover:bg-blue-700 focus:outline-none dark:focus:ring-blue-800">Submit</button>



          </form>
          </div>
          </div>

  )
}
export default  Login;
