import { api } from '../boot/axios';
import { defineStore } from 'pinia';
import {
  ICreateUser,
  IUser,
  IAccessToken,
  IResetPassword,
  IVerifyToken,
} from 'src/interfaces';
import { AuthEndpoint } from 'src/constants/endpoints';

export const useUserStore = defineStore('user', {
  state: () => ({
    isLoggedIn: localStorage.getItem('isLoggedIn')
      ? localStorage.getItem('isLoggedIn') === 'true'
      : false,
    user: localStorage.getItem('user')
      ? (JSON.parse(localStorage.getItem('user') as string) as IUser)
      : null,
    token: localStorage.getItem('token')
      ? (JSON.parse(localStorage.getItem('token') as string) as IAccessToken)
      : null,
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
      localStorage.setItem('isLoggedIn', 'true');
      localStorage.setItem('token', JSON.stringify(token));
      api.defaults.headers.common.Authorization = `Bearer ${token.access_token}`;
      this.isLoggedIn = true;
      this.token = token;
      return token;
    },
    async register(newUser: ICreateUser): Promise<IUser> {
      try {
        const response = await api.post<IUser>(AuthEndpoint.REGISTER, newUser);
        const user = response.data;
        return user;
      } catch (error) {
        console.error(error);
        if (localStorage.getItem('isLoggedIn')) {
          localStorage.removeItem('isLoggedIn');
        }
        if (localStorage.getItem('token')) {
          localStorage.removeItem('token');
        }
        if (localStorage.getItem('user')) {
          localStorage.removeItem('user');
        }
        throw new Error('Invalid user');
      }
    },
    async fetchUser(): Promise<IUser> {
      const response = await api.get<IUser>(AuthEndpoint.ME);
      const user = response.data;
      this.isLoggedIn = true;
      if (!user) {
        throw new Error('Invalid user');
      }
      this.user = user;
      localStorage.setItem('user', JSON.stringify(user));
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
        const response = await api.get<IUser>(
          `${AuthEndpoint.ACTIVATE}/${token}`
        );
        const user = response.data;
        return user;
      } catch (error) {
        console.error(error);
        return null;
      }
    },
    async verifyToken(token: string): Promise<IVerifyToken> {
      try {
        const response = await api.post<IVerifyToken>(
          `${AuthEndpoint.VERIFY_TOKEN}`,
          { token }
        );
        const data = response.data;
        return data;
      } catch (error) {
        console.error(error);
        return { valid: false, message: 'SERVER_ERROR' };
      }
    },
    async activationLink(token: string): Promise<IUser | null> {
      try {
        const response = await api.post<IUser>(
          `${AuthEndpoint.ACTIVATE_LINK}`,
          { token }
        );
        const user = response.data;
        return user;
      } catch (error) {
        console.error(error);
        return null;
      }
    },
    logout() {
      localStorage.removeItem('isLoggedIn');
      localStorage.removeItem('user');
      localStorage.removeItem('token');
      this.isLoggedIn = false;
      this.user = null;
    },
  },
});
