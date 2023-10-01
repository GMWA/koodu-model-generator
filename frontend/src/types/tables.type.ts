export interface ITable  {
  id: number;
  name: string;
  project_id: number;
  description?: string;
  created_at?: string;
  updated_at?: string;
}

export interface IGetTableResponse {
  data: ITable[];
};

export interface IRootTableState {
  tables: ITable[];
  loading: boolean;
  error: null | string;
};
