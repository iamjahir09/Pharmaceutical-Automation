<template>
  <div class="auth-page">
    <h1>Login</h1>
    <form @submit.prevent="handleLogin">
      <div>
        <label for="email">Email:</label>
        <input type="email" id="email" placeholder="Enter your email" v-model="email" />
      </div>
      <div>
        <label for="password">Password:</label>
        <input type="password" id="password" placeholder="Enter your password" v-model="password" />
      </div>
      <button type="submit" class="btn btn-primary">Login</button>
    </form>
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
/* Add your styles here */
</style>
