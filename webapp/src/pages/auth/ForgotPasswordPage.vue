<template>
  <div class="pcontainer">
    <div class="row bcontainer">
      <div class="col colum dcontainer">
        <h3 class="text-primary">Forgot Password</h3>
        <div class="login-card">
          <q-form @submit="login" @reset="reset" class="w-full">
            <q-input outlined v-model="email" label="Email" type="email" class="w-full q-ma-md" />
            <div class="w-full flex flex-row items-center q-pb-md q-ma-md">
              <div class="flex col justify-start">

              </div>
              <div class="flex flex-col-reverse justify-end">
                <router-link class="text-primary" to="/login">Or login hier</router-link>
              </div>
            </div>
            <q-btn class="w-full q-pa-md q-ma-md" label="Reset Password" type="submit" color="primary" :disabled="loading">
              <template v-slot:loading>
                <q-spinner-bars color="white" />
              </template>
            </q-btn>
            <p v-if="error">{{ error }}</p>
          </q-form>
        </div>
        <p>Already have an account? <router-link class="text-primary" to="/registration">Register</router-link></p>
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
const error = ref('');
const loading = ref(false);

/*const links = [
  { title: 'About Us', url: '/about' },
  { title: 'Contact Us', url: '/contact' },
  { title: 'Privacy Policy', url: '/privacy' },
  { title: 'Terms of Service', url: '/terms' }
]*/

const login = async () => {
  loading.value = true
  try {
    await authStore.forgotPassword(email.value)
    router.push('/login')
  } catch (e) {
    // error.value = e.message
  } finally {
    loading.value = false
  }
}

const reset = () => {
  email.value = ''
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
