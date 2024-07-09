<template>
  <div class="pcontainer">
    <div class="project-container">
      <div class="header">
        <div class="project-header">
          <div class="col-10">
            <p class="text-h4" color="primary">List of projects</p>
          </div>
          <div class="col-2">
            <q-btn round color="primary" icon="add" @click="showAddProject = !showAddProject" />
          </div>
        </div>
        <q-separator style="width: 100%; margin: 0px;" size=".15rem" color="primary" />
      </div>
      <div v-if="projects.length > 0" class="project-list">
        <div v-for="project in projects" :key="project.id">
          <p>{{ project.name }}</p>
        </div>
      </div>
      <div v-else class="no-project">
        <h5> No projects found </h5>
        <q-btn
          color="primary"
          @click="showAddProject = !showAddProject"
          label="Start a new project"
        />
      </div>
    </div>
  </div>
</template>

<script setup lang="ts">
import { ref, Ref, computed, onMounted } from 'vue'
import { IProject } from '../../interfaces'
import { useProjectStore } from '../../stores/projectStore'

const projectStore = useProjectStore()

const showAddProject: Ref<boolean> = ref(false);
const projects: Ref<IProject[]> = computed(() => projectStore.projects)

onMounted(async () => {
  await projectStore.getIndexProjects();
})
</script>

<style scoped lang="scss">
.project-container {
  display: flex;
  flex-direction: column;
  align-items: start;
  height: 100%;
  width: 100%;
  padding: 1rem;
}

.header {
  display: flex;
  flex-direction: column;
  justify-content: space-between;
  align-items: center;
  margin-bottom: 2px;
  width: 100%;
}

.project-header {
  display: flex;
  justify-content: space-between;
  align-items: center;
  width: 100%;
  padding: 0.5rem ;
}

.project-list {
  display: flex;
  flex-wrap: wrap;
  gap: 20px;
  width: 100%;
}

.no-project {
  display: flex;
  flex-direction: column;
  justify-content: center;
  align-items: center;
  height: 100%;
  width: 100%;
}
</style>
