// @ts-check
import axios from "axios";
import { defineStore, acceptHMRUpdate } from "pinia";
import { ITable, IGetTableResponse, IRootTableState } from "../types/tables.type";
import { BASE_ENDPOINT } from "../configs";

export const useTableStore = defineStore({
  id: "tables",
  state: () => ({
    /** @type {ITable[]} */
    tables: [],
    loading: false,
    error: null
  } as IRootTableState),

  getters: {
    items: (state) => state.tables
  },

  actions: {
    async getItems(){
      this.loading = true;
      try {
        const { data, status } = await axios.get<ITable[]>(
          BASE_ENDPOINT + "tables",
          {
            headers: {
              Accept: 'application/json',
            },
          },
        );
        if(status == 200){
          this.tables = data;
        }
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
    async getItemsByProject(projectId: string) : Promise<ITable[]> {
      this.loading = true;
      try {
        const { data, status } = await axios.get<ITable[]>(
          BASE_ENDPOINT + `tables/project/${projectId}`,
          {
            headers: {
              Accept: 'application/json',
            }
          }
        );
        if(status == 200){
          return data;
        }else{
          return [];
        }
      } catch (error) {
        if (axios.isAxiosError(error)) {
          this.error = error.message;
        } else {
          this.error = "An unexpected error occurred";
        }
        return [];
      } finally {
        this.loading = false;
      }
    },
    async getItem(tableId: string) : Promise<ITable | null> {
      this.loading = true;
      try {
        const { data, status } = await axios.get<ITable>(
          BASE_ENDPOINT + `tables/${tableId}`,
          {
            headers: {
              Accept: 'application/json',
            }
          }
        );
        if(status == 200){
          return data;
        }else{
          return null;
        }
      } catch (error) {
        if (axios.isAxiosError(error)) {
          this.error = error.message;
        } else {
          this.error = "An unexpected error occurred";
        }
        return null;
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
