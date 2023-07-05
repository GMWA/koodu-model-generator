// @ts-check
import { defineStore, acceptHMRUpdate } from "pinia";


export const useUserStore = defineStore({
  id: 'user',
  state: () => ({
    name: 'Eduardo',
    isAdmin: true,
  }),

  actions: {
    logout() {
    },

    /**
     * Attempt to login a user
     * @param {string} user
     * @param {string} password
     */
    async login(user: string, password: string) {
    },
  },
})

if (import.meta.hot) {
  import.meta.hot.accept(acceptHMRUpdate(useUserStore as any, import.meta.hot))
}
