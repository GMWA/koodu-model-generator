<template>
  <div>
    <h1>Projects</h1>
    <div>
      <input v-model="name" type="text" placeholder="Project Name" />
      <button @click="createProject" :disabled="loading">Create Project</button>
    </div>
    <div v-for="project in projects" :key="project.id">
      <p>{{ project.name }}</p>
    </div>
  </div>
</template>

<script setup lang="ts">
import { ref, Ref } from 'vue'
import { IProject } from '../../interfaces'
// import { useProjectStore } from '../../stores/projectStore'

const name = ref('');
const loading = ref(false);
const projects: Ref<IProject[]> = ref([]);

const createProject = async () => {
  loading.value = true;
  try {
    // await store.dispatch('projects/create', { name: name.value })
  } catch (e) {
    // error.value = e.message
  } finally {
    loading.value = false;
  }
}
</script>
