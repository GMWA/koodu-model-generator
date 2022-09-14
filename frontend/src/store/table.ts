// @ts-check
import axios from "axios";
import { defineStore, acceptHMRUpdate } from "pinia";
import { ITable, GetTableResponse, RootTableState } from "../types/tables.type";
import { BASE_ENDPOINT } from "../configs";

export const useTableStore = defineStore({
    id: "tables",
    state: () => ({
        /** @type {ITable[]} */
        tables: [],
        loading: false,
        error: null
    } as RootTableState),

    getters: {
        items: (state) => state.tables
    },

    actions: {
        async getItems(){
            this.loading = true;
            try {
                const { data, status } = await axios.get<GetTableResponse>(
                    BASE_ENDPOINT + "tables",
                    {
                        headers: {
                            Accept: 'application/json',
                        },
                    },
                );            
                this.tables = data.data;
            } catch (error) {
                if(axios.isAxiosError(error)) {
                    this.error = error.message;
                } else {
                    this.error = "An unexpected error occurred";
                }
            } finally {
                this.loading = false;
            }
        },
        addItem(table: ITable){
            if(!table) return
            this.tables.push(table);
        },
        removeItem(id: number){
            this.tables = this.tables.filter((elem: ITable) => elem.id != id);
        }
    }
})

if (import.meta.hot) {
  import.meta.hot.accept(acceptHMRUpdate(useTableStore, import.meta.hot))
}
