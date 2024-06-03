<template>
  <div>
    <h1>Auth Page</h1>
    <div v-if="true">
      <input v-model="email" type="text" placeholder="Email" />
      <input v-model="password" type="password" placeholder="Password" />
      <button @click="login" :disabled="loading">Login</button>
      <p v-if="error">{{ error }}</p>
  </div>
  <div v-else>
    <p>Welcome, {{ 'Alex' }}</p>
    <button @click="logout">Logout</button>
  </div>

  </div>
</template>


<script setup lang="ts">
import { ref } from 'vue'
// import { useUserStore } from '../../stores/userStore'

// const store = useUserStore()

const email = ref('')
const password = ref('')
const error = ref('')
const loading = ref(false)

const login = async () => {
  loading.value = true
  try {
    //await store.dispatch('auth/login', { email: email.value, password: password.value })
  } catch (e) {
    // error.value = e.message
  } finally {
    loading.value = false
  }
}

const logout = async () => {
  //await store.dispatch('auth/logout')
}
</script>
