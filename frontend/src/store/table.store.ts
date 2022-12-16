// @ts-check
import axios from "axios";
import { defineStore, acceptHMRUpdate } from "pinia";
import { ITable, GetTableResponse, RootTableState } from "../types/tables.type";
import { BASE_ENDPOINT } from "../configs";

export const useTableStore = defineStore({
  id: "tables",
  state: () => ({
    /** @type {ITable[]} */
    tables: [
      {id: 1, name: "table 1", description: "Description of the table 1"},
      {id: 2, name: "table 2", description: "Description of the table 2"},
      {id: 3, name: "table 3", description: "Description of the table 3"},
      {id: 4, name: "table 4", description: "Description of the table 4"},
      {id: 5, name: "table 5", description: "Description of the table 5"},
      {id: 6, name: "table 6", description: "Description of the table 6"}
    ],
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
    async addItem(table: ITable){
      this.loading = true;
      try {
        const { data, status } = await axios.post<ITable>(
          BASE_ENDPOINT + `tables`,
          {...table},
          {
            headers: {
              "Content-Type": "application/json"
            },
                        
          },
        );
        if(status === 200){
          this.tables.push(data);
        }
      } catch(error) {
        if(axios.isAxiosError(error)) {
          this.error = error.message;
        } else {
          this.error = "An unexpected error occurred";
        }
      } finally {
        this.loading = false;
      }
    },
		async updateItem(newTable: ITable){
			this.loading = true;
      try {
        const { data, status } = await axios.put<ITable>(
          BASE_ENDPOINT + `tables/${newTable.id}`,
          {...newTable},
          {
            headers: {
              "Content-Type": "application/json"
            },
          },
        );
        if(status === 200){
          const idx = this.tables.findIndex(
            elem => elem.id === newTable.id
          )
          this.tables[idx] = {...data};
        }
      } catch(error) {
        if(axios.isAxiosError(error)) {
          this.error = error.message;
        } else {
          this.error = "An unexpected error occurred";
        }
      } finally {
        this.loading = false;
      }
		},
    async removeItem(id: number){
      this.loading = true;
      try {
        const { data, status } = await axios.delete<ITable>(
          BASE_ENDPOINT + `tables/${id}`,
          {
            headers: {
              "Content-Type": "application/json"
            },
          },
        );
        if(status === 200){
          this.tables = this.tables.filter(
            elem => elem.id !== id
          );
        }
      } catch(error) {
        if(axios.isAxiosError(error)) {
          this.error = error.message;
        } else {
          this.error = "An unexpected error occurred";
        }
      } finally {
        this.loading = false;
      }
    }
  }
});

if (import.meta.hot) {
  import.meta.hot.accept(acceptHMRUpdate(useTableStore, import.meta.hot))
}
