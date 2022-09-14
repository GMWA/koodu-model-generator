// @ts-check
import axios from "axios";
import { defineStore, acceptHMRUpdate } from "pinia";
import { IProject, GetProjectResponse, RootProjectState } from "../types/projects.type";
import { BASE_ENDPOINT } from "../configs";

export const useProjectStore = defineStore({
    id: "projects",
    state: () => ({
        /** @type {IProject[]} */
        projects: [],
        loading: false,
        error: null
    } as RootProjectState),

    getters: {
        items: (state) => state.projects
    },

    actions: {
        async getItems(){
            this.loading = true;
            try {
                const { data, status } = await axios.get<GetProjectResponse>(
                    BASE_ENDPOINT + "projects",
                    {
                        headers: {
                            Accept: 'application/json',
                        },
                    },
                );            
                this.projects = data.data;
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
        addItem(project: IProject){
            if(!project) return
            this.projects.push(project);
        },
        removeItem(id: number){
            this.projects = this.projects.filter((elem: IProject) => elem.id != id);
        }
    }
})

if (import.meta.hot) {
  import.meta.hot.accept(acceptHMRUpdate(useProjectStore, import.meta.hot))
}
