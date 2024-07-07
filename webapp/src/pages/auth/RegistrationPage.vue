<template>
  <div class="pcontainer">
    <div class="row bcontainer">
      <div class="col colum bg-primary" style="min-width: 400px;">
      </div>
      <div class="col colum dcontainer">
        <h3>Registration</h3>
        <div class="register-card">
          <q-form @submit="register" @reset="reset" class="w-full">
            <div class="row w-full q-pb-md">
              <q-input outlined v-model="user.firstname" label="Firstname" type="text" class="col w-full q-ma-md" />
              <q-input outlined v-model="user.lastname" label="Lastname" type="text" class="col w-full q-ma-md" />
            </div>
            <div class="row w-full q-pb-md">
              <q-input outlined v-model="user.email" label="Email" type="email" class="col w-full q-ma-md" />
              <q-input outlined v-model="user.username" label="Username" type="text" class="col w-full q-ma-md" />
            </div>
            <div class="row w-full q-pb-md">
              <q-input outlined v-model="user.password" label="Password" type="password" class="col w-full q-ma-md" />
              <q-input outlined v-model="user.password_confirmation" label="Password Confirmation" type="password"
                class="col w-full q-ma-md" />
            </div>
            <div class="row w-full q-pb-md">
              <q-input outlined v-model="user.phone" label="Phone" type="text" class="col w-full q-ma-md" />
              <div class="col w-full q-ma-md"></div>
            </div>
            <q-btn class="w-full q-pa-md q-ma-md" label="Register" type="submit" color="primary" :disabled="loading" />
            <p v-if="error">{{ error }}</p>
          </q-form>
        </div>
        <p>Already have an account? <router-link to="/auth/login">login</router-link></p>
      </div>
    </div>
  </div>
</template>

<script setup lang="ts">
import { ref, Ref } from 'vue';
import { ICreateUser } from '../../interfaces';
import { useUserStore } from '../../stores/userStore';
import { useRouter } from 'vue-router';

const userStore = useUserStore();
const router = useRouter();

const user: Ref<ICreateUser> = ref({
  email: '',
  username: '',
  password: '',
  password_confirmation: '',
  firstname: '',
  lastname: '',
  phone: '',
  is_admin: false
});
const error = ref('')

const loading = ref(false)

const register = async () => {
  loading.value = true
  try {
    const resp = await userStore.register(user.value)
    if (resp) {
      router.push('/auth/login')
    }
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
    is_admin: false
  }
  error.value = ''
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

.register-card {
  min-width: 800px;
  padding: 20px;
}

.w-full {
  width: 100%;
}

.item {
  border: 2px solid red;
}
</style>
