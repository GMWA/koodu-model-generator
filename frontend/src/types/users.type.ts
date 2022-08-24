export interface IUser  {
    id: number;
    email: string;
    username: string;
    firstname?: string;
    lastname?: string;
    phone?: string;
    is_verified: boolean,
    created_at?: string;
    updated_at?: string;
}