export interface ICreateUser {
  email: string;
  username: string;
  password: string;
  password_confirmation: string;
  firstname: string;
  lastname: string;
  phone: string;
  is_admin: boolean;
  thirdparty: string;
}

export interface IUser  {
  id: number;
  email: string;
  username: string;
  firstname: string;
  lastname: string;
  phone: string;
  is_admin: boolean;
  thirdparty: string;
  created_at: string;
  updated_at: string;
}

export interface IRootTableState {
  logged_user: IUser | null;
  loading: boolean;
  error: null | string;
};
