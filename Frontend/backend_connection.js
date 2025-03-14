import axios from "axios";

const API_BASE_URL = "http://localhost:5000";

// Get home message
export const getHome = async () => {
  const response = await axios.get(`${API_BASE_URL}/`);
  return response.data();
};

// Add a new user
export const addUser = async (userData) => {
  try{
    const response = await axios.post(`${API_BASE_URL}/users`, userData);
    return response.data();
  }catch(error){
    console.error("Error adding user:", error.response?.data || error.message);
    return null;
  }
};

// Get a user by email
export const getUser = async (correo) => {
    try {
      const response = await axios.get(`${API_BASE_URL}/users/${correo}`);
      return response.data;
    } catch (error) {
      console.error("Error fetching user:", error.response?.data || error.message);
      return null;
    }
  };
  
  // Update user data
  export const updateUser = async (correo, updatedData) => {
    try {
      const response = await axios.put(`${API_BASE_URL}/users/${correo}`, updatedData);
      return response.data;
    } catch (error) {
      console.error("Error updating user:", error.response?.data || error.message);
      return null;
    }
  };
  
  // Delete a user
  export const deleteUser = async (correo) => {
    try {
      const response = await axios.delete(`${API_BASE_URL}/users/${correo}`);
      return response.data;
    } catch (error) {
      console.error("Error deleting user:", error.response?.data || error.message);
      return null;
    }
};
