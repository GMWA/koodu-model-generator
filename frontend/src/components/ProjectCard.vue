<script lang="ts" setup>
	import { IProject } from "../types/projects.type";

	interface ProjectProps {
		project: IProject
	}
	const props = withDefaults(defineProps<ProjectProps>(), {});
	const project = props.project;
	const emit = defineEmits(['delete', 'edit']);

	const handelEdit = () => {
		emit('edit', project);
	}

	const handelDelete = () => {
		emit('delete', project);
	}
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
		<div class="flex flex-row-reverse">
			<button
				class=""
				@click="handelDelete"
			>
				<span class="material-icons">delete</span>
			</button>
			<button
				class=""
				@click="handelEdit"
			>
				<span class="material-icons">edit</span>
			</button>
		</div>
	</div>
</template>

<style scoped>

</style>