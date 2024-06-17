<template>
  <div class="pcontainer">
    <div class="row bcontainer">
      <div class="col colum dcontainer">
        <h1 class="text-primary">Koodu</h1>
        <p>Login hier to quickly to manage your projects</p>
      </div>
      <div class="col colum q-gutter-md" style="min-width: 400px;">
        <h3>Login</h3>
        <q-form @submit="register" @reset="reset" class="q-gutter-md w-full">
          <q-input v-model="user.email" label="Email" type="email" class="w-full" />
          <q-input v-model="user.username" label="Username" type="text" class="w-full" />
          <q-input v-model="user.password" label="Password" type="password" class="w-full" />
          <q-input v-model="user.password_confirmation" label="Confirm Password" type="password" class="w-full" />
          <q-input v-model="user.firstname" label="Firstname" type="text" class="w-full" />
          <q-input v-model="user.lastname" label="Lastname" type="text" class="w-full" />
          <q-input v-model="user.phone" label="Phone" type="text" class="w-full" />
          <q-btn class="w-full" label="Register" type="submit" color="primary" :disabled="loading"/>
          <p v-if="error">{{ error }}</p>
        </q-form>
        <p>Already have an account? <router-link to="/login">Register</router-link></p>
      </div>
    </div>
  </div>
</template>

<script setup lang="ts">
import { ref } from 'vue';
import { ICreateUser } from '../../interfaces';
import { useUserStore } from '../../stores/userStore';
import { useRouter } from 'vue-router';

const store = useUserStore();
const router = useRouter();

const user = ref<ICreateUser>({
  email: '',
  username: '',
  password: '',
  password_confirmation: '',
  firstname: '',
  lastname: '',
  phone: '',
  is_admin: false,
  thirdparty: ''
});
const error = ref('')

const loading = ref(false)

const register = async () => {
  loading.value = true
  try {
    await store.register(user.value)
    router.push('/login')
  } catch (e) {
    // error.value = e.message
  } finally {
    loading.value = false
  }
}

const reset = () => {
  user.value = {
    email: '',
    username: '',
    password: '',
    password_confirmation: '',
    firstname: '',
    lastname: '',
    phone: '',
    is_admin: false,
    thirdparty: ''
  }
  error.value = ''
}
</script>

<style scoped lang="scss">
.dcontainer {
  background-color: beige;
}
</style>
