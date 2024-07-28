import { api } from '../boot/axios';
import { defineStore } from 'pinia';
import { IAttribut } from 'src/interfaces';
import { AttributEndpoint } from 'src/constants/endpoints';

export const useAttributStore = defineStore('attribut', {
  state: () => ({
    attributs: [] as IAttribut[],
    isLoading: false,
  }),
  actions: {
    async getIndexAttributs() {
      try {
        this.isLoading = true;
        const response = await api.get<IAttribut[]>(AttributEndpoint.GET_ALL);
        this.attributs = response.data;
      } catch (error) {
        console.error(error);
      } finally {
        this.isLoading = false;
      }
    },
    async getAttributByTableId(tableId: number): Promise<IAttribut[] | null> {
      try {
        this.isLoading = true;
        const response = await api.get<IAttribut[]>(
          `${AttributEndpoint.GET_ALL_BY_TABLE}/${tableId}`
        );
        this.attributs = response.data;
        return response.data;
      } catch (error) {
        console.error(error);
        return null;
      } finally {
        this.isLoading = false;
      }
    },
    async getAttributById(attributId: number): Promise<IAttribut | null> {
      try {
        this.isLoading = true;
        const response = await api.get<IAttribut>(
          `${AttributEndpoint.GET_ONE}/${attributId}`
        );
        return response.data;
      } catch (error) {
        console.error(error);
        return null;
      } finally {
        this.isLoading = false;
      }
    },
    async createAttribut(attribut: IAttribut) {
      try {
        this.isLoading = true;
        const response = await api.post<IAttribut>(
          AttributEndpoint.CREATE,
          attribut
        );
        this.attributs.push(response.data);
      } catch (error) {
        console.error(error);
      } finally {
        this.isLoading = false;
      }
    },
    async updateAttribut(attribut: IAttribut) {
      try {
        this.isLoading = true;
        const response = await api.put<IAttribut>(
          `${AttributEndpoint.UPDATE}/${attribut.id}`,
          attribut
        );
        const index = this.attributs.findIndex((p) => p.id === attribut.id);
        this.attributs[index] = response.data;
      } catch (error) {
        console.error(error);
      } finally {
        this.isLoading = false;
      }
    },
    async deleteAttribut(attributId: number) {
      try {
        this.isLoading = true;
        await api.delete(`${AttributEndpoint.DELETE}/${attributId}`);
        this.attributs = this.attributs.filter((p) => p.id !== attributId);
      } catch (error) {
        console.error(error);
      } finally {
        this.isLoading = false;
      }
    },
  },
});
