export interface IAttribut  {
  id: number;
  name: string;
  primary_key: boolean;
  index_key: boolean;
  unique_key: boolean;
  type: string;
  size: number;
  description?: string;
  created_at?: string;
  updated_at?: string;
  table_id: number;
};

export type GetAttributResponse = {
  data: IAttribut[];
};

export type RootAttributState = {
  attributs: IAttribut[];
  loading: boolean,
  error: null | string
};