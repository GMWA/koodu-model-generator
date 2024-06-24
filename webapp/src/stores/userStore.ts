import { api } from '../boot/axios';
import { defineStore } from 'pinia';
import { ICreateUser, IUser, IAccessToken } from 'src/interfaces';
import { AuthEndpoint } from 'src/constants/endpoints';


export const useUserStore = defineStore('user', {
  state: () => ({
    isLoggedIn: false,
    user: null as IUser | null,
    token: null as IAccessToken | null,
  }),
  actions: {
    async login(username: string, password: string): Promise<IAccessToken> {
      const response = await api.post<IAccessToken>(AuthEndpoint.LOGIN, { username, password });
      const token = response.data;
      this.isLoggedIn = true;
      this.token = token;
      console.log('User logged in', token);
      return token;
    },
    async register(newUser: ICreateUser): Promise<IUser> {
      const response = await api.post<IUser>(AuthEndpoint.REGISTER, newUser);
      const user = response.data;
      console.log('User registered', user);
      return user;
    },
    async fetchUser() {
      const response = await api.get<IUser>(AuthEndpoint.ME);
      const user = response.data;
      this.isLoggedIn = true;
      this.user = user;
      console.log('User fetched', user);
      return user;
    },
    logout() {
      // Perform logout logic here
      // Example: clear user session, reset state
      this.isLoggedIn = false;
      this.user = null;
    },
  },
});
