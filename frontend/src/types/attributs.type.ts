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
}