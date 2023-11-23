import { createSlice } from '@reduxjs/toolkit';
import jwt_decode from 'jwt-decode';

export const UserSlice = createSlice({
  name: 'user',
  initialState: {
    user: null,
    token: localStorage.getItem('token') || null,
    is_auth: false,
  },
  reducers: {
    setToken: (state, action) => {
      state.token = action.payload;
      state.is_auth = action.payload !== null;
    },

    login: (state, action) => {
      state.user = action.payload;
    },
    logout: (state) => {
      state.user = null;
      state.token = null;
      state.is_auth = false;
      localStorage.removeItem('token');
    },
    register: (state, action) => {
      state.user = action.payload;
    },
  },
});

export const { login, logout, register, setToken } = UserSlice.actions;
export const selectUser = (state) => state.user.user;


export default UserSlice.reducer;
