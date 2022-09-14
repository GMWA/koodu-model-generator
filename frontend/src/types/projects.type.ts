export interface IProject  {
    id: number;
    name: string;
    description?: string;
    created_at?: string;
    updated_at?: string;
}

export type GetProjectResponse = {
    data: IProject[];
};

export type RootProjectState = {
    projects: IProject[];
    loading: boolean,
    error: null | string
};