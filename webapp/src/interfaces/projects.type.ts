export interface IProject  {
  id: number;
  name: string;
  user_id: string;
  description?: string;
  created_at?: string;
  updated_at?: string;
}

export interface IGetProjectResponse {
  data: IProject[];
  status: number;
};

export interface IRootProjectState {
  projects: IProject[];
  loading: boolean;
  error: null | string;
};
