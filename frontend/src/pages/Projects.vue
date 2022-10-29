<script setup lang="ts">
	import Sidebar from "../components/Sidebar.vue";
	import Footer from "../components/Footer.vue";
	import Header from "../components/Header.vue";
	import ProjectCard from "../components/ProjectCard.vue";
	import { IProject } from "../types/projects.type";

	const projects : IProject[] = [
		{id: 1, name: "Project 1", description: "Description of the project 1"},
		{id: 2, name: "Project 2", description: "Description of the project 2"},
		{id: 3, name: "Project 3", description: "Description of the project 3"},
		{id: 4, name: "Project 4", description: "Description of the project 4"},
		{id: 5, name: "Project 5", description: "Description of the project 5"},
		{id: 6, name: "Project 6", description: "Description of the project 6"},
	];
</script>

<template>
	<div class="flex w-full">
		<Sidebar />

    <main class="flex flex-col w-full">
			<Header
				type="page"
				title="Projects"
			/>

			<div class="flex flex-wrap w-full border-4 border-red wrap">
				<ProjectCard
					v-for="(project, idx) in projects" :key="idx"
					:project="project"
				/>
			</div>

			<Footer />
    </main>
	</div>
</template>

<style lang="sass" scoped>

</style>