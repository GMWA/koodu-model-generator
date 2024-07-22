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
        <q-separator style="width: 100%; margin: 0px" size=".15rem" color="primary" />
      </div>
      <div v-if="projects.length > 0" class="row project-list">
        <div v-for="project in projects" :key="project.id" class="col-3 project-item w-full">
          <ProjectCard :project="project" @deleteProject="
              setDeletedProject(project);
            showDeleteProject = true;
            " @updateProject="
              setUpdatedProject(project);
            showUpdateProject = true;
            " />
        </div>
      </div>
      <div v-else class="no-project">
        <h5>No projects found</h5>
        <q-btn color="primary" @click="showAddProject = !showAddProject" label="Start a new project" />
      </div>
    </div>
    <q-dialog persistent v-model="showAddProject" backdrop-filter="backdrop-filter" transition-show="flip-down"
      transition-hide="flip-up">
      <q-card style="min-width: 600px; padding: 20px">
        <q-card-section class="row items-center q-p-none">
          <div class="text-h6">Create Project</div>
          <q-space />
          <q-btn icon="close" flat round dense v-close-popup />
        </q-card-section>

        <q-card-section class="w-full q-pa-none">
          <q-form @submit="addProject" class="w-full q-pa-none q-ma-none">
            <q-input class="w-full q-pa-md" v-model="project.name" label="Project Name" outlined clearable required />
            <q-input class="w-full q-pa-md" type="textarea" v-model="project.description" label="Project Description"
              outlined clearable required />
            <q-btn type="submit" color="primary" label="Add Project" class="w-full q-pa-md q-mt-md" />
          </q-form>
        </q-card-section>
      </q-card>
    </q-dialog>
    <q-dialog persistent v-model="showUpdateProject" backdrop-filter="backdrop-filter" transition-show="flip-down"
      transition-hide="flip-up">
      <q-card style="min-width: 600px; padding: 20px">
        <q-card-section class="row items-center q-p-none">
          <div class="text-h6">Update project</div>
          <q-space />
          <q-btn icon="close" flat round dense v-close-popup />
        </q-card-section>

        <q-card-section class="w-full q-pa-none">
          <q-form v-if="updatedProject" @submit="updateProject" class="w-full q-pa-none q-ma-none">
            <q-input class="w-full q-pa-md" v-model="updatedProject.name" label="Project Name" outlined clearable
              required />
            <q-input class="w-full q-pa-md" type="textarea" v-model="updatedProject.description"
              label="Project Description" outlined clearable required />
            <q-btn type="submit" color="primary" :disable="!updatedProject.name" label="Udate Project"
              class="w-full q-pa-md q-mt-md" />
          </q-form>
        </q-card-section>
      </q-card>
    </q-dialog>
    <q-dialog persistent v-model="showDeleteProject" backdrop-filter="backdrop-filter" transition-show="flip-down"
      transition-hide="flip-up">
      <q-card style="min-width: 600px; padding: 20px">
        <q-card-section class="row items-center q-p-none">
          <div class="text-h6">Delete project</div>
          <q-space />
          <q-btn icon="close" flat round dense v-close-popup />
        </q-card-section>

        <q-card-section class="w-full q-pa-none">
          <p>Are you sure you want to delete {{ deletedProject?.name }}?</p>
        </q-card-section>

        <q-card-actions>
          <q-btn color="primary" label="Cancel" class="q-mr-md" @click="showDeleteProject = false" />
          <q-btn color="negative" label="Delete" @click="deleteProject" />
        </q-card-actions>
      </q-card>
    </q-dialog>
  </div>
</template>

<script setup lang="ts">
import { ref, Ref, computed, onMounted } from 'vue';
import { IProject } from '../../interfaces';
import ProjectCard from '../../components/projects/ProjectCard.vue';
import { useProjectStore } from '../../stores/projectStore';
import { useUserStore } from '../../stores/userStore';

const userStore = useUserStore();
const projectStore = useProjectStore();
const showAddProject: Ref<boolean> = ref(false);
const showDeleteProject: Ref<boolean> = ref(false);
const showUpdateProject: Ref<boolean> = ref(false);
const project: Ref<IProject> = ref({
  id: 0,
  name: '',
  description: '',
  user_id: userStore.user ? userStore.user.id : 0,
});
const deletedProject: Ref<IProject | null> = ref(null);
const updatedProject: Ref<IProject | null> = ref(null);
const projects: Ref<IProject[]> = computed(() => projectStore.projects);

const addProject = async () => {
  await projectStore.createProject(project.value);
  project.value = {
    id: 0,
    name: '',
    description: '',
    user_id: userStore.user ? userStore.user.id : 0,
  };
  showAddProject.value = false;
};

const setDeletedProject = (project: IProject) => {
  deletedProject.value = {
    id: project.id,
    name: project.name,
    description: project.description,
    user_id: project.user_id,
  };
};

const setUpdatedProject = (project: IProject) => {
  updatedProject.value = {
    id: project.id,
    name: project.name,
    description: project.description,
    user_id: project.user_id,
  };
};

const deleteProject = async () => {
  if (deletedProject.value) {
    await projectStore.deleteProject(deletedProject.value);
    deletedProject.value = null;
    showDeleteProject.value = false;
  }
};

const updateProject = async () => {
  if (updatedProject.value) {
    await projectStore.updateProject(updatedProject.value);
    updatedProject.value = null;
    showUpdateProject.value = false;
  }
};

onMounted(async () => {
  await projectStore.getIndexProjects();
});
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
  padding: 0.5rem;
}

.project-list {
  /*display: grid;
  grid-template-columns: auto auto auto auto;*/
  width: 100%;
}

.project-item {
  display: flex;
  justify-content: center;
  align-items: center;
  border-radius: 5px;
  padding: 1rem;
}

.no-project {
  display: grid;
  grid-template-columns: auto auto auto auto;
  justify-content: center;
  align-items: center;
  height: 100%;
  width: 100%;
}
</style>
