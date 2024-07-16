import { api } from '../boot/axios';
import { defineStore } from 'pinia';
import { ITable } from 'src/interfaces';
import { TableEndpoint } from 'src/constants/endpoints';

export const useTableStore = defineStore('table', {
  state: () => ({
    tables: [] as ITable[],
    isLoading: false,
  }),
  actions: {
    async getIndexTables() {
      try {
        this.isLoading = true;
        const response = await api.get<ITable[]>(TableEndpoint.GET_ALL);
        this.tables = response.data;
      } catch (error) {
        console.error(error);
      } finally {
        this.isLoading = false;
      }
    },
    async getTablesbyProjectId(projectId: number) {
      try {
        this.isLoading = true;
        const response = await api.get<ITable[]>(
          `${TableEndpoint.GET_ALL}/project/${projectId}`
        );
        this.tables = response.data;
      } catch (error) {
        console.error(error);
      } finally {
        this.isLoading = false;
      }
    },
    async getTableById(tableId: number): Promise<ITable | null> {
      try {
        this.isLoading = true;
        const response = await api.get<ITable>(
          `${TableEndpoint.GET_ONE}/${tableId}`
        );
        return response.data;
      } catch (error) {
        console.error(error);
        return null;
      } finally {
        this.isLoading = false;
      }
    },
    async createTable(table: ITable) {
      try {
        this.isLoading = true;
        const response = await api.post<ITable>(TableEndpoint.CREATE, table);
        this.tables.push(response.data);
      } catch (error) {
        console.error(error);
      } finally {
        this.isLoading = false;
      }
    },
    async updateTable(table: ITable) {
      try {
        this.isLoading = true;
        const response = await api.put<ITable>(
          `${TableEndpoint.UPDATE}/${table.id}`,
          table
        );
        const index = this.tables.findIndex((p) => p.id === table.id);
        this.tables[index] = response.data;
      } catch (error) {
        console.error(error);
      } finally {
        this.isLoading = false;
      }
    },
    async deleteTable(tableId: number) {
      try {
        this.isLoading = true;
        await api.delete(`${TableEndpoint.DELETE}/${tableId}`);
        this.tables = this.tables.filter((p) => p.id !== tableId);
      } catch (error) {
        console.error(error);
      } finally {
        this.isLoading = false;
      }
    },
  },
});
