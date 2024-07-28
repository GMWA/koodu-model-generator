<template>
  <q-page class="row items-center justify-evenly">
    <q-card class="q-ma-md" style="max-width: 400px">
      <q-card-section>
        <q-card-title class="text-h6">Welcome to Quasar Vite</q-card-title>
        <q-card-subtitle class="text-subtitle1"
          >This is the Index Page</q-card-subtitle
        >
      </q-card-section>
      <q-card-section>
        <q-btn
          color="primary"
          label="Go to Auth Page"
          @click="() => $router.push({ name: 'LoginPage' })"
        />
      </q-card-section>
    </q-card>
  </q-page>
</template>

<script setup lang="ts">
defineOptions({
  name: 'IndexPage',
});
</script>
