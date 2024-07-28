<template>
  <div class="pcontainer">
    <div class="bcontainer">
      <div class="header">
        <ProjectHeader :project="project" />
      </div>
      <div class="content">
        <q-tabs v-model="tab" dense align="justify" class="bg-primary text-white shadow-2 w-full" :breakpoint="0">
          <q-tab class="q-pa-md" name="Models" icon="network_node" />
          <q-tab class="q-pa-md" name="Settings" icon="settings" />
          <q-tab class="q-pa-md" name="Code" icon="code" />
        </q-tabs>
        <div v-if="tab === 'Models'" class="row w-full h-full">
          <div class="col-3 h-full">
            <div>
              <div class="row w-full q-pa-sm q-ma-none">
                <div class="col-11">
                  <p class="text-h4" style="margin-bottom: 0px;"> Tables </p>
                </div>
                <div class="col-1">
                  <q-btn round color="primary" icon="add" @click="openAddModel" />
                </div>
              </div>
              <q-separator />
              <div>
                <TableSelectionComponent v-for="table in projectTables" :key="table.id" :table="table"
                  :active="!!selectedTable && selectedTable.id === table.id" @select="handleSelectTable(table)"
                  @delete="handleSelectDelete(table)" @edit="handelSelectEdit(table)" />
              </div>
            </div>
          </div>
          <q-separator vertical />
          <div class="d-content">
            <TableDetailsComponent :key="selectedTable.id" v-if="selectedTable" :table="selectedTable"
              :tables="projectTables" />
          </div>
        </div>
      </div>
    </div>
    <q-dialog v-model="isError" persistent transition-show="scale" transition-hide="scale">
      <q-card class="bg-red text-white" style="width: 600px">
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

    <q-dialog v-model="isAddModalOpen" persistent transition-show="scale" transition-hide="scale">
      <q-card class="bg-white" style="width: 600px">
        <q-card-section class="row items-center q-p-none">
          <div class="text-h6">Add Table to Project</div>
          <q-space />
          <q-btn icon="close" flat round dense v-close-popup />
        </q-card-section>

        <q-card-section>
          <q-form v-if="!!newTable" @submit="addTableToProject">
            <q-input class="w-full q-pa-md" v-model="newTable.name" label="Table Name" outlined required />
            <q-input class="w-full q-pa-md" type="textarea" v-model="newTable.description" label="Table Description"
              outlined required />
            <q-btn type="submit" color="primary" label="Create Table" class="w-full q-pa-md q-mt-md" />
          </q-form>
        </q-card-section>
      </q-card>
    </q-dialog>

    <q-dialog v-model="isDeleteModalOpen" persistent transition-show="scale" transition-hide="scale">
      <q-card class="bg-white" style="width: 600px">
        <q-card-section class="row items-center q-p-none">
          <div class="text-h6">Delete Table</div>
          <q-space />
          <q-btn icon="close" flat round dense v-close-popup />
        </q-card-section>

        <q-card-section>
          <q-form v-if="!!selectedTable" @submit="deleteTable">
            <p class="text-h6">Are you sure you want to delete {{ tableForDeletion?.name }}?</p>
            <q-btn type="submit" color="red" label="Delete Table" class="w-full q-pa-md q-mt-md" />
          </q-form>
        </q-card-section>
      </q-card>
    </q-dialog>

    <q-dialog v-model="isEditModalOpen" persistent transition-show="scale" transition-hide="scale">
      <q-card class="bg-white" style="width: 600px">
        <q-card-section class="row items-center q-p-none">
          <div class="text-h6">Edit Table</div>
          <q-space />
          <q-btn icon="close" flat round dense v-close-popup />
        </q-card-section>

        <q-card-section>
          <q-form v-if="!!tableForEdition" @submit="editTable">
            <q-input class="w-full q-pa-md" v-model="tableForEdition.name" label="Table Name" outlined required />
            <q-input class="w-full q-pa-md" type="textarea" v-model="tableForEdition.description"
              label="Table Description" outlined required />
            <q-btn type="submit" color="primary" label="Edit Table" class="w-full q-pa-md q-mt-md" />
          </q-form>
        </q-card-section>
      </q-card>
    </q-dialog>
  </div>
</template>

<script setup lang="ts">
import { useRoute } from 'vue-router';
import { ref, Ref, onMounted, computed } from 'vue';
import { IProject, ITable } from '../../interfaces';
import { useProjectStore } from '../../stores/projectStore';
import { useTableStore } from 'src/stores/tableStore';
import ProjectHeader from '../../components/projects/ProjectHeader.vue';
import TableDetailsComponent from 'src/components/tables/TableDetailsComponent.vue';
import TableSelectionComponent from 'src/components/tables/TableSelectionComponent.vue';


const route = useRoute();
const projectStore = useProjectStore();
const tableStore = useTableStore();
const tab: Ref<string> = ref('Models');
const project: Ref<IProject> = ref({
  id: 0,
  name: '',
  description: '',
  user_id: 0,
});
const isError: Ref<boolean> = ref(false);
const errorMsg: Ref<string> = ref('');
const projectTables = computed(() => tableStore.tables);
const selectedTable: Ref<ITable | null> = ref(null);
const tableForDeletion: Ref<ITable | null> = ref(null);
const tableForEdition: Ref<ITable | null> = ref(null);
const isAddModalOpen: Ref<boolean> = ref(false);
const isDeleteModalOpen: Ref<boolean> = ref(false);
const isEditModalOpen: Ref<boolean> = ref(false);
const newTable: Ref<ITable | null> = ref(null);


const openAddModel = () => {
  newTable.value = {
    id: 0,
    name: '',
    description: '',
    project_id: project.value.id,
  };
  isAddModalOpen.value = true;
};


const addTableToProject = async () => {
  if (!newTable.value) {
    return;
  }
  try {
    await tableStore.createTable(newTable.value);
  } catch (e) {
    console.error(e);
  } finally {
    isAddModalOpen.value = false;
    newTable.value = null;
  }
};

const handleSelectTable = (table: ITable) => {
  selectedTable.value = { ...table };
};

const handleSelectDelete = (table: ITable) => {
  tableForDeletion.value = { ...table };
  isDeleteModalOpen.value = true;
};

const handelSelectEdit = (table: ITable) => {
  tableForEdition.value = { ...table };
  isEditModalOpen.value = true;
};

const deleteTable = async () => {
  if (!tableForDeletion.value) {
    return;
  }
  try {
    await tableStore.deleteTable(tableForDeletion.value.id);
  } catch (e) {
    console.error(e);
  } finally {
    isDeleteModalOpen.value = false;
    tableForDeletion.value = null;
  }
};

const editTable = async () => {
  if (!tableForEdition.value) {
    return;
  }
  try {
    await tableStore.updateTable(tableForEdition.value);
  } catch (e) {
    console.error(e);
  } finally {
    isEditModalOpen.value = false;
    tableForEdition.value = null;
  }
};


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
    errorMsg.value =
      'The project does not exist. Either it was deleted or you do not have permission to view it.';
    return;
  }
  project.value = {
    id: data.id,
    name: data.name,
    description: data.description,
    user_id: data.user_id,
  };
  await tableStore.getTablesbyProjectId(projectId);
  if (projectTables.value.length > 0) {
    selectedTable.value = projectTables.value[0];
  }
  console.log(project.value);
});
</script>

<style scoped lang="scss">
.bcontainer {
  display: flex;
  flex-direction: column;
  align-items: start;
}

.header {
  width: 100%;
  background-color: #1976d2;
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

.project-content {
  display: flex;
  flex-direction: row;
  flex: 1;
  align-items: start;
  width: 100%;
}

.border-l {
  border: 1px solid #000;
  /* #000 */
}

.d-content {
  display: flex;
  flex-direction: column;
  flex: 1;
  align-items: start;
  width: 100%;
}
</style>
