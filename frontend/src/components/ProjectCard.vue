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
		class="flex flex-col items-center
		shadow shadow-inner hover:shadow-ls"
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