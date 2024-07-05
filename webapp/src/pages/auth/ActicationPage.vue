<template>
  <div>
    Activation Page
  </div>
</template>

<script setup lang="ts">
import { onMounted, Ref, ref } from 'vue'
import { useRouter, useRoute } from 'vue-router';
import { useUserStore } from '../../stores/userStore'

const authStore = useUserStore();
const router = useRouter();
const route = useRoute();

const token: Ref<string> = ref('');

onMounted(() => {
  token.value = route.query.token as string;
  if (!token.value) {
    router.push('/login');
  }
  // call the endpoint to activate the account
  const user = authStore.activateAccount(token.value);
  if (!user) {
    router.push('/login');
  }
})
</script>
