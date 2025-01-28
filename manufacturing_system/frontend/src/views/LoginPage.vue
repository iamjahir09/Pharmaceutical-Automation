<template>
  <div class="container">
    <div class="login-form">
      <h1 class="title">Login</h1>
      <form @submit.prevent="handleLogin">
        <div class="input-group">
          <label for="email">Email:</label>
          <input 
            type="email" 
            id="email" 
            placeholder="Enter your email" 
            v-model="email" 
          />
        </div>
        <div class="input-group">
          <label for="password">Password:</label>
          <input 
            type="password" 
            id="password" 
            placeholder="Enter your password" 
            v-model="password" 
          />
        </div>
        <button type="submit" class="submit-btn">Login</button>
        <div class="register-link">
          Don't have an account? <a href="/signup">Sign up</a>
        </div>
      </form>
    </div>
  </div>
</template>

<script>
export default {
  name: "LoginPage",
  data() {
    return {
      email: "",
      password: "",
    };
  },
  methods: {
    handleLogin() {
      // Placeholder logic for login
      if (this.email && this.password) {
        alert("Login successful!");
        this.$router.push("/main-app"); // Redirect to the main page
      } else {
        alert("Please fill out all fields.");
      }
    },
  },
};
</script>

<style scoped>
/* Glassmorphism CSS for Login Form */
body {
  font-family: Arial, sans-serif;
  background: linear-gradient(135deg, rgba(255, 0, 150, 0.8), rgba(128, 0, 255, 0.9), rgba(0, 0, 0, 1));
  background-size: cover;
  height: 100vh;
  display: flex;
  justify-content: center;
  align-items: center;
  margin: 0;
}

.container {
  width: 100%;
  height: 100vh;
  display: flex;
  justify-content: center;
  align-items: center;
}

.login-form {
  width: 350px;
  padding: 20px;
  background: rgba(255, 255, 255, 0.15); /* Light translucent white */
  border-radius: 20px;
  backdrop-filter: blur(10px); /* Glass blur effect */
  box-shadow: 0 4px 20px rgba(0, 0, 0, 0.2);
  color: white;
}

.title {
  text-align: center;
  margin-bottom: 20px;
  color: white;
  font-size: 24px;
  font-weight: bold;
  text-shadow: 0 0 5px rgba(0, 0, 0, 0.1); /* Text shadow effect */
}

.input-group {
  margin-bottom: 20px;
}

.input-group label {
  display: block;
  margin-bottom: 10px;
  color: rgba(255, 255, 255, 0.8); /* Medium gray text color */
  font-size: 16px;
}

.input-group input {
  width: 93%;
  height: 40px;
  padding: 10px;
  border: 1px solid rgba(255, 255, 255, 0.4); /* Light translucent border */
  border-radius: 5px;
  background-color: rgba(255, 255, 255, 0.2); /* Translucent white background */
  color: white;
  box-shadow: 0 0 5px rgba(0, 0, 0, 0.1); /* Shadow effect */
}

.input-group input:focus {
  border-color: rgba(50, 150, 250, 0.8); /* Blue border color on focus */
  box-shadow: 0 0 10px rgba(50, 150, 250, 0.5); /* Blue shadow effect on focus */
  outline: none;
}

.submit-btn {
  width: 100px;
  height: 40px;
  background-color: rgba(50, 150, 250, 0.8); /* Blue background color */
  color: white;
  border: none;
  border-radius: 5px;
  cursor: pointer;
  font-size: 16px;
  font-weight: bold;
  text-shadow: 0 0 5px rgba(0, 0, 0, 0.1); /* Text shadow effect */
  display: block;
  margin: 0 auto;
}

.submit-btn:hover {
  background-color: rgba(30, 120, 200, 0.9); /* Darker blue background color on hover */
}

.register-link {
  text-align: center;
  margin-top: 20px;
  color: white;
  font-size: 14px;
}

.register-link a {
  color: rgba(50, 150, 250, 0.8); /* Blue text color */
  text-decoration: none;
}

.register-link a:hover {
  color: rgba(30, 120, 200, 0.9); /* Darker blue text color on hover */
}
</style>
