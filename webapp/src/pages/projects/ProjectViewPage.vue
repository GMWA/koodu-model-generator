<template>
  <div class="pcontainer">
    <div class="bcontainer">
      <div class="header">
        <ProjectHeader :project="project" />
      </div>
      <div class="content">
      <q-tabs
        v-model="tab"
        dense
        align="justify"
        class="bg-primary text-white shadow-2 w-full"
        :breakpoint="0"
      >
        <q-tab name="Models" icon="network_node" />
        <q-tab name="Settings" icon="settings" />
        <q-tab name="Code" icon="code" />
      </q-tabs>
      <div v-if="tab==='Models'" class="row">
        <div class="col-3">

        </div>
        <div class="col-9">

        </div>
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


const route = useRoute();
const projectStore = useProjectStore();
const tab: Ref<string> = ref('Models');
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
.bcontainer {
  display: flex;
  flex-direction: column;
  align-items: start;
}

.header {
  width: 100%;
  background-color: #1976D2;
  color: white;
  padding: 10px;
}

.content {
  display: flex;
  flex-direction: column;
  flex: 1;
  align-items: start;
  width: 100%;
}
</style>