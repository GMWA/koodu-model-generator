export interface ICreateUser {
  username: string;
  lastname: string;
  firstname: string;
  phone: string;
  email: string;
  password: string;
  password_confirmation: string;
  is_admin: boolean;
}

export interface IUser {
  id: number;
  email: string;
  username: string;
  firstname: string;
  lastname: string;
  phone: string;
  is_admin: boolean;
  created_at: string;
  updated_at: string;
}

export interface IRootTableState {
  logged_user: IUser | null;
  loading: boolean;
  error: null | string;
}

export interface IAccessToken {
  access_token: string;
  token_type: string;
}

export interface IResetPassword {
  token: string;
  password: string;
  password_confirmation: string;
}

export interface IVerifyToken {
  valid: boolean;
  message: string;
}
