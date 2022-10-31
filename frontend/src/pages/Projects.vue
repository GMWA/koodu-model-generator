<script setup lang="ts">
	import Sidebar from "../components/Sidebar.vue";
	import Footer from "../components/Footer.vue";
	import Header from "../components/Header.vue";
	import ProjectCard from "../components/ProjectCard.vue";
	import { IProject } from "../types/projects.type";
	import { ref, Ref } from "vue";

	const is_add_btn_open: Ref = ref(false);

	const projects : IProject[] = [
		{id: 1, name: "Project 1", description: "Description of the project 1"},
		{id: 2, name: "Project 2", description: "Description of the project 2"},
		{id: 3, name: "Project 3", description: "Description of the project 3"},
		{id: 4, name: "Project 4", description: "Description of the project 4"},
		{id: 5, name: "Project 5", description: "Description of the project 5"},
		{id: 6, name: "Project 6", description: "Description of the project 6"},
	];

	const openModel = () => {
		is_add_btn_open.value = !is_add_btn_open.value;
	}
</script>

<template>
	<div class="flex w-full">
		<Sidebar />

    	<main class="flex flex-col w-full">
			<Header
				type="page"
				title="Projects"
			/>

			<div @click="openModel" class="flex flex-row-reverse m-3 px-10 py-2">
				<div class="w-12 h-12 rounded-full text-white bg-gray-900">
					<button class="text-white-500 h-full w-full">
						<span class="material-icons p-0 m-0">add</span>
					</button>
				</div>
			</div>

			<div class="flex flex-wrap w-full border-4 border-red wrap">
				<ProjectCard
					v-for="(project, idx) in projects" :key="idx"
					:project="project"
				/>
			</div>

			<Footer />
    	</main>
		<div
			aria-hidden="false"
			class="overflow-y-auto overflow-x-auto fixed flex items-center justify-center bg-gray-900 z-50 w-full md:inset-0 md:h-full"
			:class="{ hidden: is_add_btn_open }"
		>
			<div
				class="flex items-center justify-center bg-gray-900 w-full max-w-2xl h-screen md:h-auto"
			>
				<!-- Modal content -->
				<div class="center bg-white rounded-lg shadow dark:bg-gray-700">
					<!-- Modal header -->
					<div class="flex justify-between items-start p-4 rounded-t border-b dark:border-gray-600">
						<h3 class="text-xl font-semibold text-gray-900 dark:text-white">
							Terms of Service
						</h3>
						<button @click="openModel" type="button" class="text-gray-400 bg-transparent hover:bg-gray-200 hover:text-gray-900 rounded-lg text-sm p-1.5 ml-auto inline-flex items-center dark:hover:bg-gray-600 dark:hover:text-white" data-modal-toggle="defaultModal">
							<svg aria-hidden="true" class="w-5 h-5" fill="currentColor" viewBox="0 0 20 20" xmlns="http://www.w3.org/2000/svg"><path fill-rule="evenodd" d="M4.293 4.293a1 1 0 011.414 0L10 8.586l4.293-4.293a1 1 0 111.414 1.414L11.414 10l4.293 4.293a1 1 0 01-1.414 1.414L10 11.414l-4.293 4.293a1 1 0 01-1.414-1.414L8.586 10 4.293 5.707a1 1 0 010-1.414z" clip-rule="evenodd"></path></svg>
							<span class="sr-only">Close modal</span>
						</button>
					</div>
					<!-- Modal body -->
					<div class="p-6 space-y-6">
						<p class="text-base leading-relaxed text-gray-500 dark:text-gray-400">
							With less than a month to go before the European Union enacts new consumer privacy laws for its citizens, companies around the world are updating their terms of service agreements to comply.
						</p>
						<p class="text-base leading-relaxed text-gray-500 dark:text-gray-400">
							The European Union’s General Data Protection Regulation (G.D.P.R.) goes into effect on May 25 and is meant to ensure a common set of data rights in the European Union. It requires organizations to notify users as soon as possible of high-risk data breaches that could personally affect them.
						</p>
					</div>
					<!-- Modal footer -->
					<div class="flex items-center p-6 space-x-2 rounded-b border-t border-gray-200 dark:border-gray-600">
						<button data-modal-toggle="defaultModal" type="button" class="text-white bg-blue-700 hover:bg-blue-800 focus:ring-4 focus:outline-none focus:ring-blue-300 font-medium rounded-lg text-sm px-5 py-2.5 text-center dark:bg-blue-600 dark:hover:bg-blue-700 dark:focus:ring-blue-800">I accept</button>
						<button @click="openModel" type="button" class="text-gray-500 bg-white hover:bg-gray-100 focus:ring-4 focus:outline-none focus:ring-blue-300 rounded-lg border border-gray-200 text-sm font-medium px-5 py-2.5 hover:text-gray-900 focus:z-10 dark:bg-gray-700 dark:text-gray-300 dark:border-gray-500 dark:hover:text-white dark:hover:bg-gray-600 dark:focus:ring-gray-600">Decline</button>
					</div>
				</div>
			</div>
		</div>
	</div>
</template>

<style lang="sass" scoped>

</style>