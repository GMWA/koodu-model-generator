<script lang="ts" setup>
import { useRoute, useRouter } from "vue-router";
import { Ref, ref, computed, onMounted } from "vue";
import TableCard from "./TableCard.vue";
import TableDetails from "./TableDetails.vue";
import { useTableStore } from "../store/table.store";
import { ITable } from "../types";

const tableStore = useTableStore();
interface IProjectRoute {
  projectId: number;
};
const props = defineProps<IProjectRoute>();
const DEFAULT_TABLE: ITable = { id: 0, name: "", project_id: props.projectId};
const selectedTable: Ref<ITable> = ref(DEFAULT_TABLE);
const is_add_modal_open: Ref = ref(false);
const is_edit_modal_open: Ref = ref(false);
const is_delete_modal_open: Ref = ref(false);
const toCreateTable: Ref<ITable> = ref(DEFAULT_TABLE);
const toEditTable: Ref<ITable> = ref(DEFAULT_TABLE);
const toDeleteTable: Ref<ITable> = ref(DEFAULT_TABLE);

const items = computed(() => tableStore.items);

const openAddModal = () => {
  is_add_modal_open.value = true;
};
const closeAddModal = () => {
  is_add_modal_open.value = false;
};

const openEditModal = (table: ITable) => {
  toEditTable.value = { ...table };
  is_edit_modal_open.value = true;
};
const closeEditModal = () => {
  is_edit_modal_open.value = false;
};

const openDeleteModal = (table: ITable) => {
  toDeleteTable.value = { ...table };
  is_delete_modal_open.value = true;
};
const closeDeleteModal = () => {
  is_delete_modal_open.value = false;
};

const setSelectedTable = (tab: ITable) => {
  selectedTable.value = { ...tab };
};

const addTable = () => {
  toCreateTable.value.project_id = props.projectId;
  tableStore.addItem(toCreateTable.value);
  console.log(props);
  console.log(toCreateTable.value);
  toCreateTable.value = {...DEFAULT_TABLE};
  closeAddModal();
};

const editTable = () => {
  tableStore.addItem(toCreateTable.value);
  toEditTable.value = {...DEFAULT_TABLE};
  closeEditModal();
};

const deleteTable = async () => {
  await tableStore.removeItem(toDeleteTable.value.id);
  toDeleteTable.value = {...DEFAULT_TABLE};
  closeDeleteModal()
};

onMounted(async () => {
  await tableStore.getItems();
  if(items.value.length > 0){
    selectedTable.value = {...items.value[0]};
  }
  toCreateTable.value.project_id = props.projectId;
})
</script>

<template>
  <div class="flex flex-row w-full h-full mt-2">
    <div class="flex flex-col w-1/5 h-full border-r-2">
      <div class="flex bg-gray-600 p-2 h-14 align-middle">
        <div class="text-white text-xl pt-2">List of tables</div>
        <div class="grow"></div>
        <div class="bg-blue-700 w-10 h-10 rounded-full">
          <button
            @click="openAddModal"
            class="text-white text-xs font-bold w-full h-full"
          >
            <span class="material-icons">add</span>
          </button>
        </div>
      </div>
      <div class="flex flex-col mt-3">
        <TableCard
          v-for="(table, idx) in items"
          :key="idx"
          :table="table"
          :active="table.id === selectedTable.id"
          @choose="setSelectedTable(table)"
          @delete="openDeleteModal"
          @edit="openEditModal"
        />
      </div>
    </div>
    <div class="flex w-3/4">
      <TableDetails
        v-if="selectedTable.id > 0"
        :table="selectedTable"
        :tables="tableStore.items"
      />
    </div>

    <!--Add Modal-->

    <div
      class="overflow-y-auto overflow-x-auto fixed flex items-center justify-center bg-gray-900 bg-opacity-50 z-50 w-full md:inset-0 md:h-full transition duration-150 ease-in-out"
      :class="{ hidden: !is_add_modal_open }"
    >
      <div class="flex items-center justify-center w-full max-w-2xl h-screen md:h-auto">
        <!-- Modal content -->
        <div class="center bg-white rounded-lg shadow dark:bg-gray-700 w-full">
          <!-- Modal header -->
          <div
            class="flex justify-between items-start p-4 rounded-t border-b dark:border-gray-600"
          >
            <h3 class="text-xl font-semibold text-gray-900 dark:text-white">Add Table</h3>
            <button
              @click="closeAddModal"
              type="button"
              class="text-gray-400 bg-transparent hover:bg-gray-200 hover:text-gray-900 rounded-lg text-sm p-1.5 ml-auto inline-flex items-center dark:hover:bg-gray-600 dark:hover:text-white"
              data-modal-toggle="defaultModal"
            >
              <svg
                aria-hidden="true"
                class="w-5 h-5"
                fill="currentColor"
                viewBox="0 0 20 20"
                xmlns="http://www.w3.org/2000/svg"
              >
                <path
                  fill-rule="evenodd"
                  d="M4.293 4.293a1 1 0 011.414 0L10 8.586l4.293-4.293a1 1 0 111.414 1.414L11.414 10l4.293 4.293a1 1 0 01-1.414 1.414L10 11.414l-4.293 4.293a1 1 0 01-1.414-1.414L8.586 10 4.293 5.707a1 1 0 010-1.414z"
                  clip-rule="evenodd"
                ></path>
              </svg>
              <span class="sr-only">Close modal</span>
            </button>
          </div>
          <!-- Modal body -->
          <div class="p-6 space-y-6 w-full">
            <form class="flex flex-col w-full">
              <label for="name">Name:</label>
              <input
                type="text"
                name="name"
                class="form-input px-4 py-3 mt-1 rounded-2xl"
                placeholder="Name"
                v-model="toCreateTable.name"
              />
              <label class="mt-4" for="desciption"> Description: </label>
              <textarea
                name="description"
                class="form-input px-4 py-3 mt-1 rounded-2xl"
                rows="3"
                placeholder="Description"
                v-model="toCreateTable.description"
              >
              </textarea>
            </form>
          </div>
          <!-- Modal footer -->
          <div
            class="flex flex-row-reverse items-center p-6 space-x-2 rounded-b border-t border-gray-200 dark:border-gray-600"
          >
            <button
              @click="addTable"
              type="button"
              class="text-white bg-blue-700 hover:bg-blue-800 focus:ring-4 focus:outline-none focus:ring-blue-300 font-medium rounded-lg text-sm px-5 py-2.5 text-center dark:bg-blue-600 dark:hover:bg-blue-700 dark:focus:ring-blue-800"
            >
              Add
            </button>
            <button
              @click="closeAddModal"
              type="button"
              class="text-gray-500 bg-white hover:bg-gray-100 focus:ring-4 focus:outline-none focus:ring-blue-300 rounded-lg border border-gray-200 text-sm font-medium px-5 py-2.5 hover:text-gray-900 focus:z-10 dark:bg-gray-700 dark:text-gray-300 dark:border-gray-500 dark:hover:text-white dark:hover:bg-gray-600 dark:focus:ring-gray-600"
            >
              Decline
            </button>
          </div>
        </div>
      </div>
    </div>

    <!--Edit Modal-->

    <div
      class="overflow-y-auto overflow-x-auto fixed flex items-center justify-center bg-gray-900 bg-opacity-50 z-50 w-full md:inset-0 md:h-full transition duration-150 ease-in-out"
      :class="{ hidden: !is_edit_modal_open }"
    >
      <div class="flex items-center justify-center w-full max-w-2xl h-screen md:h-auto">
        <!-- Modal content -->
        <div class="center bg-white rounded-lg shadow dark:bg-gray-700 w-full">
          <!-- Modal header -->
          <div
            class="flex justify-between items-start p-4 rounded-t border-b dark:border-gray-600"
          >
            <h3 class="text-xl font-semibold text-gray-900 dark:text-white">
              Edit {{ toEditTable.name }}
            </h3>
            <button
              @click="closeEditModal"
              type="button"
              class="text-gray-400 bg-transparent hover:bg-gray-200 hover:text-gray-900 rounded-lg text-sm p-1.5 ml-auto inline-flex items-center dark:hover:bg-gray-600 dark:hover:text-white"
              data-modal-toggle="defaultModal"
            >
              <svg
                aria-hidden="true"
                class="w-5 h-5"
                fill="currentColor"
                viewBox="0 0 20 20"
                xmlns="http://www.w3.org/2000/svg"
              >
                <path
                  fill-rule="evenodd"
                  d="M4.293 4.293a1 1 0 011.414 0L10 8.586l4.293-4.293a1 1 0 111.414 1.414L11.414 10l4.293 4.293a1 1 0 01-1.414 1.414L10 11.414l-4.293 4.293a1 1 0 01-1.414-1.414L8.586 10 4.293 5.707a1 1 0 010-1.414z"
                  clip-rule="evenodd"
                ></path>
              </svg>
              <span class="sr-only">Close modal</span>
            </button>
          </div>
          <!-- Modal body -->
          <div class="p-6 space-y-6 w-full">
            <form class="flex flex-col w-full">
              <label for="name">New name:</label>
              <input
                type="text"
                name="name"
                class="form-input px-4 py-3 mt-1 rounded-2xl"
                placeholder="Name"
                v-model="toEditTable.name"
              />
              <label class="mt-4" for="desciption">New description: </label>
              <textarea
                name="description"
                class="form-input px-4 py-3 mt-1 rounded-2xl"
                rows="3"
                placeholder="Description"
                v-model="toEditTable.description"
              >
              </textarea>
            </form>
          </div>
          <!-- Modal footer -->
          <div
            class="flex flex-row-reverse items-center p-6 space-x-2 rounded-b border-t border-gray-200 dark:border-gray-600"
          >
            <button
              @click="editTable"
              type="button"
              class="text-white bg-blue-700 hover:bg-blue-800 focus:ring-4 focus:outline-none focus:ring-blue-300 font-medium rounded-lg text-sm px-5 py-2.5 text-center dark:bg-blue-600 dark:hover:bg-blue-700 dark:focus:ring-blue-800"
            >
              Edit
            </button>
            <button
              @click="closeEditModal"
              type="button"
              class="text-gray-500 bg-white hover:bg-gray-100 focus:ring-4 focus:outline-none focus:ring-blue-300 rounded-lg border border-gray-200 text-sm font-medium px-5 py-2.5 hover:text-gray-900 focus:z-10 dark:bg-gray-700 dark:text-gray-300 dark:border-gray-500 dark:hover:text-white dark:hover:bg-gray-600 dark:focus:ring-gray-600"
            >
              Decline
            </button>
          </div>
        </div>
      </div>
    </div>

    <!--Delete Modal-->

    <div
      class="overflow-y-auto overflow-x-auto fixed flex items-center justify-center bg-gray-900 bg-opacity-50 z-50 w-full md:inset-0 md:h-full transition duration-150 ease-in-out"
      :class="{ hidden: !is_delete_modal_open }"
    >
      <div class="flex items-center justify-center w-full max-w-2xl h-screen md:h-auto">
        <!-- Modal content -->
        <div class="center bg-white rounded-lg shadow dark:bg-gray-700 w-full">
          <!-- Modal header -->
          <div
            class="flex justify-between items-start p-4 rounded-t border-b dark:border-gray-600"
          >
            <h3 class="text-xl font-semibold text-gray-900 dark:text-white">
              Delete {{ toDeleteTable.name }}
            </h3>
            <button
              @click="closeDeleteModal"
              type="button"
              class="text-gray-400 bg-transparent hover:bg-gray-200 hover:text-gray-900 rounded-lg text-sm p-1.5 ml-auto inline-flex items-center dark:hover:bg-gray-600 dark:hover:text-white"
              data-modal-toggle="defaultModal"
            >
              <svg
                aria-hidden="true"
                class="w-5 h-5"
                fill="currentColor"
                viewBox="0 0 20 20"
                xmlns="http://www.w3.org/2000/svg"
              >
                <path
                  fill-rule="evenodd"
                  d="M4.293 4.293a1 1 0 011.414 0L10 8.586l4.293-4.293a1 1 0 111.414 1.414L11.414 10l4.293 4.293a1 1 0 01-1.414 1.414L10 11.414l-4.293 4.293a1 1 0 01-1.414-1.414L8.586 10 4.293 5.707a1 1 0 010-1.414z"
                  clip-rule="evenodd"
                ></path>
              </svg>
              <span class="sr-only">Close modal</span>
            </button>
          </div>
          <!-- Modal body -->
          <div class="p-6 space-y-6 w-full">
            <p class="text-2xl">
              Are you sur you want to delete {{ toDeleteTable.name }}?
            </p>
          </div>
          <!-- Modal footer -->
          <div
            class="flex flex-row-reverse items-center p-6 space-x-2 rounded-b border-t border-gray-200 dark:border-gray-600"
          >
            <button
              @click="deleteTable"
              type="button"
              class="text-white bg-blue-700 hover:bg-blue-800 focus:ring-4 focus:outline-none focus:ring-blue-300 font-medium rounded-lg text-sm px-5 py-2.5 text-center dark:bg-blue-600 dark:hover:bg-blue-700 dark:focus:ring-blue-800"
            >
              Delete
            </button>
            <button
              @click="closeDeleteModal"
              type="button"
              class="text-gray-500 bg-white hover:bg-gray-100 focus:ring-4 focus:outline-none focus:ring-blue-300 rounded-lg border border-gray-200 text-sm font-medium px-5 py-2.5 hover:text-gray-900 focus:z-10 dark:bg-gray-700 dark:text-gray-300 dark:border-gray-500 dark:hover:text-white dark:hover:bg-gray-600 dark:focus:ring-gray-600"
            >
              Decline
            </button>
          </div>
        </div>
      </div>
    </div>
  </div>
</template>

<style scoped></style>
