<template>
  <div class="pcontainer">
    <div class="row bcontainer">
      <div class="col colum dcontainer">
        <h3 class="text-primary">Login</h3>
        <div class="login-card">
          <q-form @submit="login" @reset="reset" class="w-full">
            <q-input outlined v-model="email" label="Email" type="email" class="w-full q-ma-md" />
            <q-input outlined v-model="password" :rules="[val => val.length > 0 || 'Please enter your password']"
              :type="isPwd ? 'password' : 'text'" label="Password" class="w-full q-ma-md">
              <template v-slot:append>
                <q-icon :name="isPwd ? 'visibility_off' : 'visibility'" class="cursor-pointer"
                  @click="isPwd = !isPwd" />
              </template>
            </q-input>
            <div class="w-full flex flex-row items-center q-pb-md q-ma-md">
              <div class="flex col justify-start">
                <q-checkbox class="text-primary" v-model="remember" label="Remember me" />
              </div>
              <div class="flex flex-col-reverse justify-end">
                <router-link class="text-primary" to="/auth/forgot-password">Forgot password?</router-link>
              </div>
            </div>
            <q-btn class="w-full q-pa-md q-ma-md" label="Login" type="submit" color="primary" :disabled="loading">
              <template v-slot:loading>
                <q-spinner-bars color="white" />
              </template>
            </q-btn>
            <p v-if="error">{{ error }}</p>
          </q-form>
        </div>
        <p>Already have an account? <router-link class="text-primary" to="/auth/registration">Register</router-link></p>
      </div>
      <div class="col colum bg-primary" style="min-width: 400px;">
      </div>
    </div>
  </div>
</template>


<script setup lang="ts">
import { ref } from 'vue'
import { useRouter } from 'vue-router';
import { useUserStore } from '../../stores/userStore'

const authStore = useUserStore();
const router = useRouter();

const email = ref('');
const password = ref('');
const error = ref('');
const isPwd = ref(true);
const loading = ref(false);
const remember = ref(false);

/*const links = [
  { title: 'About Us', url: '/about' },
  { title: 'Contact Us', url: '/contact' },
  { title: 'Privacy Policy', url: '/privacy' },
  { title: 'Terms of Service', url: '/terms' }
]*/

const login = async () => {
  loading.value = true
  try {
    const tokenInfos = await authStore.login(email.value, password.value);
    if (!tokenInfos) {
      console.log('error')
      throw new Error('Invalid credentials')
    }
    // fetch user data
    const user = await authStore.fetchUser();
    if (!user) {
      throw new Error('User not found')
    }
    // redirect to home page
    router.push('/projects')
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

/*const validatePassword = (val: string) => {
  // at least 8 characters, 1 upper case letter, 1 lowercase letter, 1 number and 1 special character
  return /^(?=.*\d)(?=.*[a-z])(?=.*[A-Z])(?=.*[a-zA-Z]).{8,}$/.test(val)
}*/
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
</style>
