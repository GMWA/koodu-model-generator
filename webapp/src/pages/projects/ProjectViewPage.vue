<template>
  <div class="pcontainer">
    <div>
      <div>
        <ProjectHeader :project="project" />
      </div>
      <div class="row">
        <div class="col-3">

        </div>
        <div class="col-9">

        </div>
      </div>
    </div>
    <q-dialog v-model="isError" persistent transition-show="scale" transition-hide="scale">
      <q-card class="bg-red text-white" style="width: 600px;">
        <q-card-section>
          <div class="text-h4">Error</div>
        </q-card-section>

        <q-card-section class="q-pt-none">
          <p class="text-h6">
            {{ errorMsg }}
          </p>
        </q-card-section>

        <q-card-actions align="right" class="bg-white text-teal">
          <q-btn flat to="/projects" label="Back to Project list" v-close-popup />
        </q-card-actions>
      </q-card>
    </q-dialog>
  </div>
</template>

<script setup lang="ts">
import { useRoute } from 'vue-router';
import { ref, Ref, onMounted } from 'vue';
import { IProject } from '../../interfaces';
import { useProjectStore } from '../../stores/projectStore';
import ProjectHeader from '../../components/projects/ProjectHeader.vue';
// import { useUserStore } from '../../stores/userStore';


const route = useRoute();
const projectStore = useProjectStore();
// const userStore = useUserStore();
const project: Ref<IProject> = ref({
  id: 0,
  name: '',
  description: '',
  user_id: 0
})
const isError: Ref<boolean> = ref(false);
const errorMsg: Ref<string> = ref('');


onMounted(async () => {
  const projectId = route.params.id ? parseInt(route.params.id as string) : 0;
  if (projectId <= 0) {
    isError.value = true;
    errorMsg.value = 'Invalid project id';
    return;
  }
  const data = await projectStore.getProjectById(projectId);
  if (!data) {
    isError.value = true;
    errorMsg.value = 'The project does not exist. Either it was deleted or you do not have permission to view it.';
    return;
  }
  project.value = {
    id: data.id,
    name: data.name,
    description: data.description,
    user_id: data.user_id

  }
  console.log(project.value)
})
</script>

<style scoped lang="scss">
</style>
