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
		class="w-3/12 items-center p-2 m-2
		shadow-md shadow-inner hover:shadow-2xl"
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