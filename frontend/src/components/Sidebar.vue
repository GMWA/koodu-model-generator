<script setup lang="ts">
import Session from "supertokens-web-js/recipe/session";
import ThirdPartyEmailPassword from "supertokens-web-js/recipe/thirdpartyemailpassword";
import { ref, Ref, onMounted } from "vue";
import { API_DOMAIN } from "@/configs";
const is_expanded: Ref<boolean> = ref(
  localStorage.getItem("is_expanded") === "true" ? true : false
);
const ToggleMenu = () => {
  is_expanded.value = !is_expanded.value;
  localStorage.setItem("is_expanded", `${is_expanded.value}`);
};

const session = ref(false);
const userId = ref("");

onMounted(async () => {
  await checkForSession();
});

const checkForSession = async () => {
  if (!(await Session.doesSessionExist())) {
    // since a session does not exist, we send the user to the login page.
    return window.location.assign("/auth");
  }
  const userID = await Session.getUserId();
  // this will render the UI
  session.value = true;
  userId.value = userID;
};

const signOut = async () => {
  await ThirdPartyEmailPassword.signOut();
  window.location.assign("/");
};
</script>

<template>
  <aside :class="`${is_expanded ? 'is-expanded' : ''}`">
    <div class="logo">
      <img src="../assets/vue.svg" alt="Vue" />
    </div>

    <div class="menu-toggle-wrap">
      <button class="menu-toggle" @click="ToggleMenu">
        <span class="material-icons">keyboard_double_arrow_right</span>
      </button>
    </div>

    <h3>Menu</h3>
    <div class="menu">
      <router-link class="button" to="/">
        <span class="material-icons">folder_copy</span>
        <span class="text">Projects</span>
      </router-link>
      <router-link class="button" to="/dashboard">
        <span class="material-icons">dashboard</span>
        <span class="text">Dashboard</span>
      </router-link>
      <router-link class="button" to="/editor">
        <span class="material-icons">edit_note</span>
        <span class="text">Notepad</span>
      </router-link>
      <router-link class="button" to="/supports">
        <span class="material-icons">help</span>
        <span class="text">Supports</span>
      </router-link>
    </div>

    <div class="flex"></div>

    <div class="menu">
      <router-link class="button" to="/settings">
        <span class="material-icons">settings</span>
        <span class="text">Settings</span>
      </router-link>
      <button v-if="session" class="button" @click="signOut">
        <span class="material-icons">logout</span>
        <span class="text">Logout</span>
      </button>
    </div>
  </aside>
</template>

<style lang="scss" scoped>
aside {
  display: flex;
  flex-direction: column;
  width: calc(2rem + 32px);
  min-height: 100vh;
  overflow: hidden;
  padding: 1rem;
  background-color: var(--dark);
  color: var(--light);
  transition: 0.2s ease-out;
  .flex {
    flex: 1 1 0;
  }
  .logo {
    margin-bottom: 1rem;
    img {
      width: 2rem;
    }
  }
  .menu-toggle-wrap {
    display: flex;
    justify-content: flex-end;
    margin-bottom: 1rem;
    position: relative;
    top: 0;
    transition: 0.2s ease-out;
    .menu-toggle {
      transition: 0.2s ease-out;
      .material-icons {
        font-size: 3rem;
        color: var(--light);
        transition: 0.2 ease-out;
      }
      &:hover {
        .material-icons {
          color: var(--primary);
          transform: translateX(0.5rem);
        }
      }
    }
  }
  h3,
  .button .text {
    opacity: 0;
    transition: 0.3s ease-out;
  }
  h3 {
    color: var(--grey);
    font-size: 0.875rem;
    margin-bottom: 0.5rem;
    text-transform: uppercase;
  }
  .menu {
    margin: 0 -1rem;
    .button {
      display: flex;
      align-items: center;
      text-decoration: none;
      padding: 0.5rem;
      transition: 0.2s ease-out;
      .material-icons {
        font-size: 2rem;
        color: var(--light);
        transition: 0.2s ease-out;
      }
      .text {
        color: var(--light);
        transition: 0.2s ease-out;
      }
      &:hover,
      &.router-link-exact-active {
        background-color: var(--dark-alt);
        .material-icons .text {
          color: var(--primary);
        }
      }
      &.router-link-exact-active {
        border-right: 5px solid var(--primary);
      }
    }
  }
  &.is-expanded {
    width: var(--sidebar-width);
    .menu-toggle-wrap {
      top: -3rem;
      .menu-toggle {
        transform: rotate(-180deg);
      }
    }
    h3,
    .button .text {
      opacity: 1;
    }
    .button {
      .material-icons {
        margin-right: 1rem;
      }
    }
  }
  @media (max-width: 1024px) {
    position: fixed;
    z-index: 99;
  }
}
</style>
