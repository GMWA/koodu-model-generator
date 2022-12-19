<script lang="ts" setup>
import { ITable } from "../types/tables.type";
import { IAttribut } from "../types/attributs.type";
import { useAttributStore } from "../store/attributs.store";
import { watch } from "vue";

interface TableProps {
  table: ITable;
}
const props = withDefaults(defineProps<TableProps>(), {});
let table: ITable = props.table;
const emit = defineEmits(["delete", "edit", "choose"]);
const attributs = useAttributStore();
let selectedAttribut: IAttribut = attributs.items[0];

watch(
  () => props.table,
  (first, second) => {
    table = { ...first };
  }
);

const setSelectedAttribut = (attrib: IAttribut) => {
  selectedAttribut = { ...attrib };
};
</script>

<template>
  <div class="flex flex-col pl-2 w-full">
    <div class="flex w-full mt-2 mb-2 text-3xl font-bold">
      Attributs for {{ table.name }}
    </div>
    <hr />
    <div class="flex items-center align-middle w-full mt-2 mb-2">
      <select
        id="countries"
        class="bg-gray-50 border border-gray-300 text-gray-900 text-sm rounded-lg focus:ring-blue-500 focus:border-blue-500 block w-full p-2.5 dark:bg-gray-700 dark:border-gray-600 dark:placeholder-gray-400 dark:text-white dark:focus:ring-blue-500 dark:focus:border-blue-500"
      >
        <option
          v-for="(attrib, index) in attributs.items"
          :key="index"
          :value="attrib.name"
          @change="setSelectedAttribut(attrib)"
        >
          {{ attrib.name }}
        </option>
      </select>
    </div>
    <hr />
    <div class="flex w-full">
      <form class="w-full mt-2">
        <div class="grid gap-6 mb-6 md:grid-cols-2">
          <div>
            <label
              for="name"
              class="block mb-2 text-sm font-medium text-gray-900 dark:text-white"
              >Name</label
            >
            <input
              type="text"
              id="first_name"
              class="bg-gray-50 border border-gray-300 text-gray-900 text-sm rounded-lg focus:ring-blue-500 focus:border-blue-500 block w-full p-2.5 dark:bg-gray-700 dark:border-gray-600 dark:placeholder-gray-400 dark:text-white dark:focus:ring-blue-500 dark:focus:border-blue-500"
              placeholder="John"
              :value="selectedAttribut.name"
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
            >
              <option value="String">string</option>
              <option value="Integer">int</option>
              <option value="Float">float</option>
              <option value="Bool">bool</option>
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
              <option value="table1">Table 1</option>
              <option value="table2">Table 2</option>
              <option value="table3">Table 3</option>
              <option value="table4">Table 3</option>
            </select>
          </div>
          <div>
            <label
              for="phone"
              class="block mb-2 text-sm font-medium text-gray-900 dark:text-white"
              >Is Index</label
            >
            <input
              checked
              id="red-checkbox"
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
              placeholder="flowbite.com"
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
              checked
              id="red-checkbox"
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
              checked
              id="red-checkbox"
              type="checkbox"
              value=""
              class="w-4 h-4 text-red-600 bg-gray-100 rounded border-gray-300 focus:ring-red-500 dark:focus:ring-red-600 dark:ring-offset-gray-800 focus:ring-2 dark:bg-gray-700 dark:border-gray-600"
            />
          </div>
        </div>

        <button
          type="submit"
          class="text-white bg-blue-700 hover:bg-blue-800 focus:ring-4 focus:outline-none focus:ring-blue-300 font-medium rounded-lg text-sm w-full sm:w-auto px-5 py-2.5 text-center dark:bg-blue-600 dark:hover:bg-blue-700 dark:focus:ring-blue-800"
        >
          Submit
        </button>
      </form>
    </div>
  </div>
</template>

<style scoped></style>
