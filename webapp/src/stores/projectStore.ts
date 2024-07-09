import { api } from '../boot/axios';
import { defineStore } from 'pinia';
import { IProject } from 'src/interfaces';
import { ProjectEndpoint } from 'src/constants/endpoints';


export const useProjectStore = defineStore('project', {
	state: () => ({
		projects: [] as IProject[],
		isLoading: false,
	}),
	actions: {
		async getIndexProjects() {
			try {
				this.isLoading = true;
				const response = await api.get<IProject[]>(ProjectEndpoint.GET_ALL);
				this.projects = response.data;
			} catch (error) {
				console.error(error);
			} finally {
				this.isLoading = false;
			}
		},
		async createProject(project: IProject) {
			try {
				this.isLoading = true;
				const response = await api.post<IProject>(ProjectEndpoint.CREATE, project);
				this.projects.push(response.data);
			} catch (error) {
				console.error(error);
			} finally {
				this.isLoading = false;
			}
		},
		async updateProject(project: IProject) {
			try {
				this.isLoading = true;
				const response = await api.put<IProject>(`${ProjectEndpoint.UPDATE}/${project.id}`, project);
				const index = this.projects.findIndex((p) => p.id === project.id);
				this.projects[index] = response.data;
			} catch (error) {
				console.error(error);
			} finally {
				this.isLoading = false;
			}
		},
		async deleteProject(project: IProject) {
			try {
				this.isLoading = true;
				await api.delete(`${ProjectEndpoint.DELETE}/${project.id}`);
				this.projects = this.projects.filter((p) => p.id !== project.id);
			} catch (error) {
				console.error(error);
			} finally {
				this.isLoading = false;
			}
		},
	},
});
