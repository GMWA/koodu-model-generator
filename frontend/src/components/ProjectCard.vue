<script lang="ts" setup>
import { IProject } from "../types/projects.type";

interface ProjectProps {
  project: IProject;
}
const props = withDefaults(defineProps<ProjectProps>(), {});
const project = props.project;
const emit = defineEmits(["delete", "edit", "choose"]);

const handleEdit = () => {
  emit("edit", project);
};

const handleDelete = () => {
  emit("delete", project);
};

const handleChoose = () => {
  emit("choose", project);
};
</script>

<template>
  <div class="w-full items-center p-2 m-2 rounded-md border-solid border border-gray-300">
    <div class="hover:cursor-pointer" @click="handleChoose">
      <div class="text-2xl font-bold mb-1">
        {{ project.name }}
      </div>
      <hr />
      <div class="mt-4 mb-4">
        {{ project.description }}
      </div>
    </div>
    <hr />
    <div class="flex flex-row-reverse mt-1 mb-1">
      <button class="mr-2 text-red-700" @click="handleDelete">
        <span class="material-icons">delete</span>
      </button>
      <button class="mr-2 text-main1" @click="handleEdit">
        <span class="material-icons">edit</span>
      </button>
    </div>
  </div>
</template>

<style scoped></style>
