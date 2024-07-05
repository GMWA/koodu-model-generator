import { api } from '../boot/axios';
import { defineStore } from 'pinia';
import { ICreateUser, IUser, IAccessToken, IResetPassword } from 'src/interfaces';
import { AuthEndpoint } from 'src/constants/endpoints';


export const useUserStore = defineStore('user', {
  state: () => ({
    isLoggedIn: false,
    user: null as IUser | null,
    token: null as IAccessToken | null,
  }),
  actions: {
    async login(username: string, password: string): Promise<IAccessToken> {
      // Perform login logic here with form data
      const data = new FormData();
      data.append('username', username);
      data.append('password', password);
      const response = await api.post<IAccessToken>(AuthEndpoint.LOGIN, data);
      const token = response.data;
      if (!token) {
        throw new Error('Invalid token');
      }
      api.defaults.headers.common.Authorization = `Bearer ${token.access_token}`;
      this.isLoggedIn = true;
      this.token = token;
      return token;
    },
    async register(newUser: ICreateUser): Promise<IUser> {
      const response = await api.post<IUser>(AuthEndpoint.REGISTER, newUser);
      const user = response.data;
      return user;
    },
    async fetchUser(): Promise<IUser> {
      const response = await api.get<IUser>(AuthEndpoint.ME);
      const user = response.data;
      this.isLoggedIn = true;
      if (!user) {
        throw new Error('Invalid user');
      }
      this.user = user;
      return user;
    },
    async refresh(): Promise<IAccessToken> {
      const response = await api.post<IAccessToken>(AuthEndpoint.REFRESH);
      const token = response.data;
      if (!token) {
        throw new Error('Invalid token');
      }
      api.defaults.headers.common.Authorization = `Bearer ${token.access_token}`;
      this.isLoggedIn = true;
      this.token = token;
      return token;
    },
    async forgotPassword(email: string): Promise<void> {
      const data = new FormData();
      data.append('email', email);
      await api.post(AuthEndpoint.FORGOT_PASSWORD, data);
    },
    async resetPassword(data: IResetPassword): Promise<IUser | null> {
      const response = await api.post<IUser>(AuthEndpoint.RESET_PASSWORD, data);
      const user = response.data;
      return user;
    },
    async activateAccount(token: string): Promise<IUser | null> {
      try {
        const response = await api.get<IUser>(`${AuthEndpoint.ACTIVATE}/${token}`);
        const user = response.data;
        return user;
      } catch (error) {
        console.error(error);
        return null;
      }
    },
    logout() {
      // Perform logout logic here
      // Example: clear user session, reset state
      this.isLoggedIn = false;
      this.user = null;
    },
  },
});
