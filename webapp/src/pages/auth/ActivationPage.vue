<template>
  <div class="pcontainer">
    <q-dialog
      v-model="showErrorDialog"
      persistent
      transition-show="scale"
      transition-hide="scale"
    >
      <q-card class="bg-red text-white" style="width: 600px">
        <q-card-section>
          <div class="text-h6">Error</div>
        </q-card-section>

        <q-card-section class="q-pt-none">
          An error occurred while activating your account. Either the link is
          invalid or expired.
        </q-card-section>

        <q-card-actions align="right" class="bg-white text-teal">
          <q-btn flat to="/auth/login" label="OK" v-close-popup />
        </q-card-actions>
      </q-card>
    </q-dialog>

    <q-dialog
      v-model="showActivatedDialog"
      persistent
      transition-show="scale"
      transition-hide="scale"
    >
      <q-card class="bg-primary text-white" style="width: 600px">
        <q-card-section>
          <div class="text-h6">Success</div>
        </q-card-section>

        <q-card-section class="q-pt-none">
          Your account has been activated successfully. You can now login with
          your credentials and start using the app.
        </q-card-section>

        <q-card-actions align="right" class="bg-white text-teal">
          <q-btn flat to="/auth/login" label="OK" v-close-popup />
        </q-card-actions>
      </q-card>
    </q-dialog>
  </div>
</template>

<script setup lang="ts">
import { onMounted, Ref, ref } from 'vue';
import { useRoute } from 'vue-router';
import { useUserStore } from '../../stores/userStore';

const userStore = useUserStore();
const route = useRoute();

const showErrorDialog: Ref<boolean> = ref(false);
const showActivatedDialog: Ref<boolean> = ref(false);
const isValToken: Ref<boolean> = ref(false);
const activationToken: Ref<string> = ref('');

onMounted(async () => {
  activationToken.value = route.params.token as string;
  if (!activationToken.value) {
    isValToken.value = false;
  }
  const verified_token = await userStore.verifyToken(activationToken.value);
  if (verified_token.valid) {
    isValToken.value = true;
  } else {
    showErrorDialog.value = true;
    return;
  }
  // activate the user
  const user = await userStore.activationLink(activationToken.value);
  if (user) {
    showActivatedDialog.value = true;
  } else {
    showErrorDialog.value = false;
  }
});
</script>
