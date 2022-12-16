<script setup lang="ts">
import ThirdPartyEmailPassword from "supertokens-web-js/recipe/thirdpartyemailpassword";
import { onMounted } from "vue";

onMounted(async () => {
  try {
    const response = await ThirdPartyEmailPassword.thirdPartySignInAndUp({});
    if (response.status !== "OK") {
      return window.location.assign("/auth?error=signin");
    }
    window.location.assign("/");
  } catch (_) {
    window.location.assign("/auth?error=signin");
  }
});
</script>

<template>
  <div>
    <svg class="animate-spin h-5 w-5 mr-3 ..." viewBox="0 0 24 24">
      <!-- ... -->
    </svg>
  </div>
</template>

<style scoped></style>
