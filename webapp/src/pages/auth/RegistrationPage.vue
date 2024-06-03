<template>
  <div>
    <h1>Registration Page</h1>
    <div>
      <input v-model="email" type="text" placeholder="Email" />
      <input v-model="password" type="password" placeholder="Password" />
      <button @click="register" :disabled="loading">Register</button>
      <p v-if="error">{{ error }}</p>
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

const register = async () => {
  loading.value = true
  try {
    //await store.dispatch('auth/register', { email: email.value, password: password.value })
  } catch (e) {
    // error.value = e.message
  } finally {
    loading.value = false
  }
}
</script>
