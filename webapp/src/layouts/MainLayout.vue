<template>
  <q-layout view="hHh lpR fFf">
    <q-page-container>
      <router-view />
      <q-page-sticky position="bottom-right" :offset="[30, 80]">
        <q-menu v-model="menu" style="width: 200px">
          <q-list>
            <q-item
              class="menu-item"
              clickable
              v-close-popup
              to="/users/profile"
            >
              <q-icon
                class="menu-icon"
                name="person"
                size="2rem"
                color="primary"
              />
              <q-item-section class="menu-label">Profile</q-item-section>
            </q-item>
            <q-item
              class="menu-item"
              clickable
              v-close-popup
              to="/users/settings"
            >
              <q-icon
                class="menu-icon"
                name="settings"
                size="2rem"
                color="secondary"
              />
              <q-item-section class="menu-label">Settings</q-item-section>
            </q-item>
            <q-item class="menu-item" clickable v-close-popup @click="logout">
              <q-icon
                class="menu-icon"
                name="exit_to_app"
                size="2rem"
                color="red"
              />
              <q-item-section class="menu-label">Logout</q-item-section>
            </q-item>
          </q-list>
        </q-menu>
      </q-page-sticky>
      <q-page-sticky position="bottom-right" :offset="[18, 18]">
        <q-fab icon="person" @click="menu = !menu" color="primary" />
      </q-page-sticky>
    </q-page-container>
  </q-layout>
</template>

<script setup lang="ts">
import { ref } from 'vue';
import { useRouter } from 'vue-router';
import { useUserStore } from '../stores/userStore';

const authStore = useUserStore();
const router = useRouter();

const menu = ref(false);

const logout = async () => {
  await authStore.logout();
  router.push('/auth/login');
};
</script>

<style scoped lang="scss">
.menu-item {
  display: flex;
  align-items: center;
}
.menu-icon {
  margin-right: 10px;
}

.menu-label {
  font-size: 1.2rem;
}
</style>
