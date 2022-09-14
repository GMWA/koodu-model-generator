export interface ITable  {
    id: number;
    name: string;
    description?: string;
    created_at?: string;
    updated_at?: string;
}

export type GetTableResponse = {
    data: ITable[];
};

export type RootTableState = {
    tables: ITable[];
    loading: boolean,
    error: null | string
};