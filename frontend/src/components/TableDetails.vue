<script lang="ts" setup>
import { ITable } from "../types/tables.type";
import { IAttribut } from "../types/attributs.type";
import { useAttributStore } from "../store/attributs.store";
import { watch, Ref, ref } from "vue";

interface TableProps {
  table: ITable;
  tables: ITable[];
}
const props = withDefaults(defineProps<TableProps>(), {});
let table: ITable = props.table;
let tables: ITable[] = props.tables;
const emit = defineEmits(["delete", "edit", "choose"]);
const attributs = useAttributStore();
const selectedAttribut: Ref<IAttribut> = ref(attributs.items[0]);
const is_add_modal_open: Ref = ref(false);
const is_delete_modal_open: Ref = ref(false);
const toCreateAttribut: Ref<IAttribut> = ref({
  id: 0,
  name: "",
  table_id: table.id,
  index_key: false,
  primary_key: false,
  unique_key: false,
  type: "",
  size: 0,
});
const toDeleteAttribut: Ref<IAttribut> = ref({
  id: 0,
  name: "",
  table_id: table.id,
  index_key: false,
  primary_key: false,
  unique_key: false,
  type: "",
  size: 0,
});

watch(
  () => props.table,
  (first, second) => {
    table = { ...first };
  }
);

const setSelectedAttribut = (attrib: IAttribut) => {
  selectedAttribut.value = { ...attrib };
};

const openAddModal = () => {
  is_add_modal_open.value = true;
};
const closeAddModal = () => {
  is_add_modal_open.value = false;
};

const openDeleteModal = () => {
  toDeleteAttribut.value = { ...selectedAttribut.value };
  is_delete_modal_open.value = true;
};
const closeDeleteModal = () => {
  is_delete_modal_open.value = false;
};

const addAttribut = () => {
  console.log(toCreateAttribut);
};

const editAttribut = () => {
  console.log(selectedAttribut);
};

const deleteAttribut = () => {
  console.log(toDeleteAttribut);
};
</script>

<template>
  <div class="flex flex-col pl-2 w-full">
    <div class="flex w-full mt-2 mb-2 text-3xl font-bold">
      <div class="flex flex-row w-full">
        <div class="flex text-3xl font-bold">Attributs for {{ table.name }}</div>
        <div class="grow"></div>
        <div class="flex bg-green-700 w-10 h-10 rounded-full">
          <button
            @click="openAddModal"
            class="text-white text-xs font-bold w-full h-full"
          >
            <span class="material-icons">add</span>
          </button>
        </div>
      </div>
    </div>
    <hr />
    <div class="flex items-center align-middle w-full mt-2 mb-2">
      <select
        class="bg-gray-50 border border-gray-300 text-gray-900 text-sm rounded-lg focus:ring-blue-500 focus:border-blue-500 block w-full p-2.5 dark:bg-gray-700 dark:border-gray-600 dark:placeholder-gray-400 dark:text-white dark:focus:ring-blue-500 dark:focus:border-blue-500"
        v-model="selectedAttribut"
      >
        <option
          v-for="(attrib, index) in attributs.items"
          :key="index"
          :value="attrib"
          :selected="attrib.id === selectedAttribut.id"
        >
          {{ attrib.name }}
        </option>
      </select>
    </div>
    <hr />
    <div class="flex w-full">
      <div class="w-full mt-2">
        <div class="grid gap-6 mb-6 md:grid-cols-2">
          <div>
            <label
              for="name"
              class="block mb-2 text-sm font-medium text-gray-900 dark:text-white"
              >Name</label
            >
            <input
              type="text"
              class="bg-gray-50 border border-gray-300 text-gray-900 text-sm rounded-lg focus:ring-blue-500 focus:border-blue-500 block w-full p-2.5 dark:bg-gray-700 dark:border-gray-600 dark:placeholder-gray-400 dark:text-white dark:focus:ring-blue-500 dark:focus:border-blue-500"
              placeholder="Name"
              v-model="selectedAttribut.name"
              required
            />
          </div>
          <div>
            <label
              for="type"
              class="block mb-2 text-sm font-medium text-gray-900 dark:text-white"
              >Type</label
            >
            <select
              class="bg-gray-50 border border-gray-300 text-gray-900 text-sm rounded-lg focus:ring-blue-500 focus:border-blue-500 block w-full p-2.5 dark:bg-gray-700 dark:border-gray-600 dark:placeholder-gray-400 dark:text-white dark:focus:ring-blue-500 dark:focus:border-blue-500"
              v-model="selectedAttribut.type"
            >
              <option value="string">String</option>
              <option value="integer">Integer</option>
              <option value="decimal">Decimal</option>
              <option value="bool">Bool</option>
            </select>
          </div>
          <div>
            <label
              for="table"
              class="block mb-2 text-sm font-medium text-gray-900 dark:text-white"
              >Table</label
            >
            <select
              class="bg-gray-50 border border-gray-300 text-gray-900 text-sm rounded-lg focus:ring-blue-500 focus:border-blue-500 block w-full p-2.5 dark:bg-gray-700 dark:border-gray-600 dark:placeholder-gray-400 dark:text-white dark:focus:ring-blue-500 dark:focus:border-blue-500"
            >
              <option v-for="(tab, idx) in tables" :value="tab.id">
                {{ tab.name }}
              </option>
            </select>
          </div>
          <div>
            <label
              for="phone"
              class="block mb-2 text-sm font-medium text-gray-900 dark:text-white"
              >Is Index</label
            >
            <input
              v-model="selectedAttribut.index_key"
              type="checkbox"
              value=""
              class="w-4 h-4 text-red-600 bg-gray-100 rounded border-gray-300 focus:ring-red-500 dark:focus:ring-red-600 dark:ring-offset-gray-800 focus:ring-2 dark:bg-gray-700 dark:border-gray-600"
            />
          </div>
          <div>
            <label
              for="website"
              class="block mb-2 text-sm font-medium text-gray-900 dark:text-white"
              >Size</label
            >
            <input
              type="number"
              class="bg-gray-50 border border-gray-300 text-gray-900 text-sm rounded-lg focus:ring-blue-500 focus:border-blue-500 block w-full p-2.5 dark:bg-gray-700 dark:border-gray-600 dark:placeholder-gray-400 dark:text-white dark:focus:ring-blue-500 dark:focus:border-blue-500"
              placeholder="Size"
              v-model="selectedAttribut.size"
              required
            />
          </div>
          <div>
            <label
              for="primary_key"
              class="block mb-2 text-sm font-medium text-gray-900 dark:text-white"
              >Is Primary key</label
            >
            <input
              v-model="selectedAttribut.primary_key"
              type="checkbox"
              value=""
              class="w-4 h-4 text-red-600 bg-gray-100 rounded border-gray-300 focus:ring-red-500 dark:focus:ring-red-600 dark:ring-offset-gray-800 focus:ring-2 dark:bg-gray-700 dark:border-gray-600"
            />
          </div>
          <div>
            <label
              for="visitors"
              class="block mb-2 text-sm font-medium text-gray-900 dark:text-white"
              >Description</label
            >
            <textarea
              class="w-full h-20 bg-gray-100 rounded border-gray-300 dark:ring-offset-gray-800 focus:ring-2 dark:bg-gray-700 dark:border-gray-600"
              placeholder="Description"
              v-model="selectedAttribut.description"
            >
            </textarea>
          </div>
          <div>
            <label
              for="visitors"
              class="block mb-2 text-sm font-medium text-gray-900 dark:text-white"
              >Is Unique</label
            >
            <input
              v-model="selectedAttribut.unique_key"
              id="red-checkbox"
              type="checkbox"
              value=""
              class="w-4 h-4 text-red-600 bg-gray-100 rounded border-gray-300 focus:ring-red-500 dark:focus:ring-red-600 dark:ring-offset-gray-800 focus:ring-2 dark:bg-gray-700 dark:border-gray-600"
            />
          </div>
        </div>

        <button
          class="text-white bg-red-700 hover:bg-red-800 focus:ring-4 focus:outline-none focus:ring-red-300 font-medium rounded-lg text-sm w-full sm:w-auto px-5 py-2.5 text-center dark:bg-red-600 dark:hover:bg-grren-700 dark:focus:ring-red-800"
          @click="openDeleteModal"
        >
          Delete
        </button>
        <button
          type="submit"
          class="text-white bg-green-700 hover:bg-green-800 focus:ring-4 focus:outline-none focus:ring-green-300 font-medium rounded-lg text-sm w-full sm:w-auto px-5 py-2.5 text-center dark:bg-green-600 dark:hover:bg-grren-700 dark:focus:ring-green-800"
        >
          Save
        </button>
      </div>
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
            <h3 class="text-xl font-semibold text-gray-900 dark:text-white">
              Add Attribut
            </h3>
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
                v-model="toCreateAttribut.name"
              />
              <label class="mt-4" for="desciption"> Description: </label>
              <textarea
                name="description"
                class="form-input px-4 py-3 mt-1 rounded-2xl"
                rows="3"
                placeholder="Description"
                v-model="toCreateAttribut.description"
              >
              </textarea>
            </form>
          </div>
          <!-- Modal footer -->
          <div
            class="flex flex-row-reverse items-center p-6 space-x-2 rounded-b border-t border-gray-200 dark:border-gray-600"
          >
            <button
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
              Delete Attribut
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
              Are you sur you want to delete the Project {{ toDeleteAttribut.name }}?
            </p>
          </div>
          <!-- Modal footer -->
          <div
            class="flex flex-row-reverse items-center p-6 space-x-2 rounded-b border-t border-gray-200 dark:border-gray-600"
          >
            <button
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
