// @ts-check
import axios from "axios";
import { defineStore, acceptHMRUpdate } from "pinia";
import { IUser, IRootTableState } from "../types/users.type";
import { BASE_ENDPOINT } from "../configs";

export const useUserStore = defineStore({
  id: 'user',
  state: () => ({
    logged_user: null,
    loading: false,
    error: null
  } as IRootTableState),
  getters: {
    user: (state) => state.logged_user
  },
  actions: {
    async getItem(userId: string) : Promise<IUser | null> {
      this.loading = true;
      try {
        const { data, status } = await axios.get<IUser>(
          BASE_ENDPOINT + `users/${userId}`,
          {
            headers: {
              Accept: 'application/json',
            }
          }
        );
        if(status == 200){
          return data;
        }else{
          return null;
        }
      } catch (error) {
        if (axios.isAxiosError(error)) {
          this.error = error.message;
        } else {
          this.error = "An unexpected error occurred";
        }
        return null;
      } finally {
        this.loading = false;
      }
    },
    async addItem() : Promise<IUser | null> {
      this.loading = true;
      try {
        const { data, status } = await axios.post<IUser>(
          BASE_ENDPOINT + "users",
          {
            headers: {
              Accept: 'application/json',
            }
          }
        );
        if(status == 200){
          return data;
        }else{
          return null;
        }
      } catch (error) {
        if (axios.isAxiosError(error)) {
          this.error = error.message;
        } else {
          this.error = "An unexpected error occurred";
        }
        return null;
      } finally {
        this.loading = false;
      }
    }
  },
})

if (import.meta.hot) {
  import.meta.hot.accept(acceptHMRUpdate(useUserStore as any, import.meta.hot))
}
