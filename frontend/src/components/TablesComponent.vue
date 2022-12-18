<script lang="ts" setup>
import { useRoute, useRouter } from "vue-router";
import { Ref, ref } from "vue";
import TableCard from "./TableCard.vue";
import TableDetails from "./TableDetails.vue";
import { useTableStore } from "../store/table.store";
import { ITable } from "../types";

const tables = useTableStore();
const selectedTable: Ref<ITable> = ref(tables.items[0]);

const setSelectedTable = (tab: ITable) => {
  selectedTable.value = { ...tab };
};
</script>

<template>
  <div class="flex flex-row w-full h-full mt-2">
    <div class="flex flex-col w-1/5 h-full border-r-2">
      <div class="flex bg-gray-600 p-2 h-14 align-middle">
        <div class="text-white text-xl pt-2">List of tables</div>
        <div class="grow"></div>
        <div class="bg-blue-700 w-10 h-10 rounded-full">
          <button class="text-white text-xs font-bold w-full h-full">
            <span class="material-icons">add</span>
          </button>
        </div>
      </div>
      <div class="flex flex-col mt-3">
        <TableCard
          v-for="(table, idx) in tables.items"
          :key="idx"
          :table="table"
          @choose="setSelectedTable(table)"
        />
      </div>
    </div>
    <div class="flex w-3/4">
      <TableDetails :table="selectedTable" />
    </div>
  </div>
</template>

<style scoped></style>
