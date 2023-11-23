import { configureStore } from "@reduxjs/toolkit";
import userReducer from "./UserSlice";
import jwtDecode from "jwt-decode";

export default configureStore({
  reducer: {
    user: userReducer,
  },
});

