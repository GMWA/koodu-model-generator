// @ts-check
import axios from "axios";
import { defineStore, acceptHMRUpdate } from "pinia";
import { IProject, IGetProjectResponse, IRootProjectState } from "../types/projects.type";
import { BASE_ENDPOINT } from "../configs";

export const useProjectStore = defineStore({
  id: "projectState",
  state: () => ({
    /** @type {IProject[]} */
    projects: [] as IProject[],
    loading: false,
    error: null
  } as IRootProjectState),

  getters: {
    items: (state) => state.projects
  },

  actions: {
    async getItems() {
      // Set the loading state to true
      this.loading = true;
      try {
        const { data, status } = await axios.get<IGetProjectResponse>(
          BASE_ENDPOINT + "projects",
          {
            headers: {
              Accept: 'application/json',
            },
          },
        );
        // Update the projects array with the response data
        this.projects = data.data;
      } catch (error) {
        // Handle errors and set the error state
        if (axios.isAxiosError(error)) {
          this.error = error.message;
        } else {
          this.error = "An unexpected error occurred";
        }
      } finally {
        // Set the loading state back to false
        this.loading = false;
      }
    },
    async addItem(project: IProject){
      this.loading = true;
      try {
        const { data, status } = await axios.post<IProject>(
          BASE_ENDPOINT + `projects`,
          {...project},
          {
            headers: {
              "Content-Type": "application/json"
            },

          },
        );
        if(status === 200){
          this.projects.push(data);
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
		async updateItem(newProject: IProject){
			this.loading = true;
      try {
        const { data, status } = await axios.put<IProject>(
          BASE_ENDPOINT + `projects/${newProject.id}`,
          {...newProject},
          {
            headers: {
              "Content-Type": "application/json"
            },
          },
        );
        if(status === 200){
          const idx = this.projects.findIndex(
            elem => elem.id === newProject.id
          )
          this.projects[idx] = {...data};
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
        const { data, status } = await axios.delete<IProject>(
          BASE_ENDPOINT + `tables/${id}`,
          {
            headers: {
              "Content-Type": "application/json"
            },
          },
        );
        if(status === 200){
          this.projects = this.projects.filter(
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
  import.meta.hot.accept(acceptHMRUpdate(useProjectStore, import.meta.hot))
}
