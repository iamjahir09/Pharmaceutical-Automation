<template>
  <div class="auth-page">
    <h1>Sign Up</h1>
    <form @submit.prevent="handleSignup">
      <div>
        <label for="name">Name:</label>
        <input type="text" id="name" placeholder="Enter your name" v-model="name" />
      </div>
      <div>
        <label for="email">Email:</label>
        <input type="email" id="email" placeholder="Enter your email" v-model="email" />
      </div>
      <div>
        <label for="password">Password:</label>
        <input type="password" id="password" placeholder="Enter your password" v-model="password" />
      </div>
      <button type="submit" class="btn btn-primary">Sign Up</button>
    </form>
  </div>
</template>

<script>
export default {
  name: "SignupPage",
  data() {
    return {
      name: "",
      email: "",
      password: "",
    };
  },
  methods: {
    handleSignup() {
      // Placeholder logic for signup
      if (this.name && this.email && this.password) {
        alert("Signup successful!");
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
