<template>
  <div class="pcontainer">
    <div class="row bcontainer">
      <div class="col colum bg-primary" style="min-width: 400px;">
      </div>
      <div class="col colum dcontainer">
        <h3>Reset Password</h3>
        <div class="register-card">
          <q-form @submit="resetPassword" @reset="reset" class="w-full">
            <q-input outlined v-model="data.password" :rules="[val => val.length > 0 || 'Please enter your password']"
              :type="isPwd ? 'password' : 'text'" label="New Password" class="w-full q-ma-md">
              <template v-slot:append>
                <q-icon :name="isPwd ? 'visibility_off' : 'visibility'" class="cursor-pointer"
                  @click="isPwd = !isPwd" />
              </template>
            </q-input>
            <q-input outlined v-model="data.password_confirmation" :rules="[val => val.length > 0 || 'Please enter your password']"
              :type="isPwdConfirmation ? 'password' : 'text'" label="New Password Confirmation" class="w-full q-ma-md">
              <template v-slot:append>
                <q-icon :name="isPwdConfirmation ? 'visibility_off' : 'visibility'" class="cursor-pointer"
                  @click="isPwdConfirmation = !isPwdConfirmation" />
              </template>
            </q-input>
            <q-btn class="w-full q-pa-md q-ma-md" label="Login" type="submit" color="primary" :disabled="loading">
              <template v-slot:loading>
                <q-spinner-bars color="white" />
              </template>
            </q-btn>
            <p v-if="error">{{ error }}</p>
          </q-form>
        </div>
        <p>Already have an account? <router-link to="/login">login</router-link></p>
      </div>
    </div>
  </div>
</template>

<script setup lang="ts">
import { ref, Ref } from 'vue';
import { IResetPassword } from '../../interfaces';
import { useUserStore } from '../../stores/userStore';
import { useRouter } from 'vue-router';

const userStore = useUserStore();
const router = useRouter();

const data: Ref<IResetPassword> = ref({
  token: '',
  password: '',
  password_confirmation: ''
});
const isPwd = ref(true);
const isPwdConfirmation = ref(true);
const error = ref('')
const loading = ref(false)

const resetPassword = async () => {
  loading.value = true
  try {
    await userStore.resetPassword(data.value)
    router.push('/login')
  } catch (e) {
    error.value = e.message
  } finally {
    loading.value = false
  }
}

const reset = () => {
  data.value = {
    token: '',
    password: '',
    password_confirmation: ''
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
