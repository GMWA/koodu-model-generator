<template>
  <div class="pcontainer">
    <div class="row bcontainer">
      <div class="col colum dcontainer">
        <h5>Login hier to quickly to manage your projects</h5>
        <div class="login-card">
          <q-form @submit="login" @reset="reset" class="w-full">
            <q-input outlined v-model="email" label="Email" type="email" class="w-full q-ma-md" />
            <q-input outlined v-model="password" label="Password" type="password" class="w-full q-ma-md"
              :rules="[val => val && val.length == 0 || 'Please enter your password', validatePassword]" />
            <div class="w-full flex flex-row items-center q-pb-md q-ma-md">
              <div class="flex col justify-start">
                <q-checkbox class="" v-model="remember" label="Remember me" />
              </div>
              <div class="flex flex-col-reverse justify-end">
                <router-link class="" to="/forgot-password">Forgot password?</router-link>
              </div>
            </div>
            <q-btn class="w-full q-pa-md q-ma-md" label="Login" type="submit" color="primary" :disabled="loading" />
            <p v-if="error">{{ error }}</p>
          </q-form>
        </div>
        <p>Already have an account? <router-link to="/registration">Register</router-link></p>
      </div>
      <div class="col colum q-gutter-md" style="min-width: 400px;">
      </div>
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
const loading = ref(false);
const remember = ref(false)

/*const links = [
  { title: 'About Us', url: '/about' },
  { title: 'Contact Us', url: '/contact' },
  { title: 'Privacy Policy', url: '/privacy' },
  { title: 'Terms of Service', url: '/terms' }
]*/

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

const reset = () => {
  email.value = ''
  password.value = ''
}

const validatePassword = (val: string) => {
  // at least 8 characters, 1 upper case letter, 1 lowercase letter, 1 number and 1 special character
  return /^(?=.*\d)(?=.*[a-z])(?=.*[A-Z])(?=.*[a-zA-Z]).{8,}$/.test(val)
}
</script>

<style scoped lang="scss">
.dcontainer {
  display: flex;
  flex-direction: column;
  justify-content: center;
  align-items: center;
  padding: 20px;
  background-color: #f5f5f5;
}

.login-card {
  min-width: 600px;
  padding: 20px;

}

.w-full {
  width: 100%;
}

.item {
  border: 2px solid red;
}
</style>
