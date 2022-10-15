// @ts-check
import axios from "axios";
import { defineStore, acceptHMRUpdate } from "pinia";
import {
	IAttribut,
	GetAttributResponse,
	RootAttributState } from "../types/attributs.type";
import { BASE_ENDPOINT } from "../configs";

export const useAttributStore = defineStore({
  id: "attributs",
  state: () => ({
    /** @type {IAttribut[]} */
    attributs: [],
    loading: false,
    error: null
  } as RootAttributState),

  getters: {
    items: (state) => state.attributs
  },

  actions: {
    async getItems(){
      this.loading = true;
      try {
        const { data, status } = await axios.get<GetAttributResponse>(
          BASE_ENDPOINT + "attributs",
          {
            headers: {
              Accept: 'application/json',
            },
          },
        );            
        this.attributs = data.data;
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
    async addItem(attribut: IAttribut){
      this.loading = true;
      try {
        const { data, status } = await axios.post<IAttribut>(
          BASE_ENDPOINT + `attributs`,
          {...attribut},
          {
            headers: {
              "Content-Type": "application/json"
            },
                        
          },
        );
        if(status === 200){
          this.attributs.push(data);
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
		async updateItem(newAttribut: IAttribut){
			this.loading = true;
      try {
        const { data, status } = await axios.put<IAttribut>(
          BASE_ENDPOINT + `attributs/${newAttribut.id}`,
          {...newAttribut},
          {
            headers: {
              "Content-Type": "application/json"
            },
          },
        );
        if(status === 200){
          const idx = this.attributs.findIndex(
            elem => elem.id === newAttribut.id
          )
          this.attributs[idx] = {...data};
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
        const { data, status } = await axios.delete<IAttribut>(
          BASE_ENDPOINT + `attributs/${id}`,
          {
            headers: {
              "Content-Type": "application/json"
            },
          },
        );
        if(status === 200){
          this.attributs = this.attributs.filter(
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
  import.meta.hot.accept(acceptHMRUpdate(useAttributStore, import.meta.hot))
}
