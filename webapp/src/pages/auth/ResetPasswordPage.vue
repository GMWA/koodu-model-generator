<template>
  <div class="pcontainer">
    <div class="row bcontainer">
      <div class="col colum bg-primary" style="min-width: 400px;">
      </div>
      <div v-if="isValToken" class="col colum dcontainer">
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
            <q-input outlined v-model="data.password_confirmation"
              :rules="[val => val.length > 0 || 'Please enter your password']"
              :type="isPwdConfirmation ? 'password' : 'text'" label="New Password Confirmation" class="w-full q-ma-md">
              <template v-slot:append>
                <q-icon :name="isPwdConfirmation ? 'visibility_off' : 'visibility'" class="cursor-pointer"
                  @click="isPwdConfirmation = !isPwdConfirmation" />
              </template>
            </q-input>
            <q-btn class="w-full q-pa-md q-ma-md" label="Reset Password" type="submit" color="primary"
              :disabled="loading">
              <template v-slot:loading>
                <q-spinner-bars color="white" />
              </template>
            </q-btn>
            <p v-if="error">{{ error }}</p>
          </q-form>
        </div>
      </div>
      <div v-else class="col colum dcontainer">
        <div class="register-card">
          <h3>The Activation link is not valid or has expired create a new link</h3>
          <q-btn class="w-full q-pa-md q-ma-md" to="/auth/forgot-password" label="forgot Password" type="submit"
            color="primary" />
        </div>
      </div>
    </div>
    <q-dialog v-model="alert" persistent transition-show="scale" transition-hide="scale">
      <q-card class="bg-primary text-white" style="width: 300px">
        <q-card-section>
          <div class="text-h6">Success</div>
        </q-card-section>

        <q-card-section class="q-pt-none">
          Password reset successfully.
          You can now login with your new password.
        </q-card-section>

        <q-card-actions align="right" class="bg-white text-teal">
          <q-btn flat to="/login" label="OK" v-close-popup />
        </q-card-actions>
      </q-card>
    </q-dialog>
  </div>
</template>

<script setup lang="ts">
import { ref, Ref, onMounted } from 'vue';
import { IResetPassword } from '../../interfaces';
import { useUserStore } from '../../stores/userStore';
import { useRoute } from 'vue-router';

const userStore = useUserStore();
const route = useRoute();

const data: Ref<IResetPassword> = ref({
  token: '',
  password: '',
  password_confirmation: ''
});
const isValToken: Ref<boolean> = ref(false);
const activationToken: Ref<string> = ref('');
const isPwd: Ref<boolean> = ref(true);
const isPwdConfirmation: Ref<boolean> = ref(true);
const error: Ref<string> = ref('')
const loading: Ref<boolean> = ref(false)
const alert: Ref<boolean> = ref(false)

const resetPassword = async () => {
  loading.value = true
  try {
    await userStore.resetPassword(data.value)
    alert.value = true
  } catch (e) {
    error.value = 'Invalid token or password mismatch'
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

onMounted(async () => {
  activationToken.value = route.params.token as string;
  if (!activationToken.value) {
    isValToken.value = false;
  }
  const verified_token = await userStore.verifyToken(activationToken.value);
  if (verified_token.valid) {
    isValToken.value = true;
    data.value.token = activationToken.value;
  } else {
    console.log('Token is invalid')
  }
})
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
