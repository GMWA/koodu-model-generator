import { defineStore } from 'pinia';


export const useUserStore = defineStore('user', {
  state: () => ({
    isLoggedIn: false,
    user: null,
  }),
  actions: {
    login(username: string, password: string) {
      // Perform login logic here
      // Example: make an API call to authenticate the user
      // If successful, update the store state
      this.isLoggedIn = true;
      // this.user = { username };
      console.log('User logged in:', this.user, password);
    },
    logout() {
      // Perform logout logic here
      // Example: clear user session, reset state
      this.isLoggedIn = false;
      this.user = null;
    },
  },
});
