// @ts-check
import { defineStore, acceptHMRUpdate } from "pinia";
import { IProject } from "../types/projects.type";

export type RootState = {
    projects: IProject[];
  };

export const useProjectStore = defineStore({
    id: "projects",
    state: () => ({
        /** @type {IProject[]} */
        projects: []
    } as RootState),
    
    getters: {
        items: (state) => state.projects
    },

    actions: {
        getItems(){

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
