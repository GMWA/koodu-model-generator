<script lang="ts" setup>
	import { IProject } from "../types/projects.type";

	interface ProjectProps {
		project: IProject
	}
	const props = withDefaults(defineProps<ProjectProps>(), {});
	const project = props.project;
</script>

<template>
	<div
		class="w-full items-center p-2 m-2 rounded-md
		shadow-2xl shadow-inner hover:shadow-md"
	>
		<div>
			{{ project.name }}
		</div>
		<div>
			{{ project.description }}
		</div>
	</div>
</template>

<style scoped>

</style>