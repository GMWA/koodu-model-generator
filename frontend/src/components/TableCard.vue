<script lang="ts" , setup>
import { ITable } from "../types/tables.type";

interface TableProps {
  table: ITable;
}
const props = withDefaults(defineProps<TableProps>(), {});
const table = props.table;
const emit = defineEmits(["delete", "edit", "choose"]);

const handleEdit = () => {
  emit("edit", table);
};

const handleDelete = () => {
  emit("delete", table);
};

const handleChoose = () => {
  emit("choose", table);
};
</script>

<template>
  <div class="flex flex-row w-full h-14 align-middle pr-2 hover:cursor-pointer">
    <div class="pl-4 text-xl" @click="handleChoose">{{ table.name }}</div>
    <div class="grow"></div>
    <div class="mr-2">
      <button class="text-green-700 text-xs font-bold w-full h-full" @click="handleEdit">
        <span class="material-icons">edit</span>
      </button>
    </div>
    <div class="">
      <button class="text-red-700 text-xs font-bold w-full h-full" @click="handleDelete">
        <span class="material-icons">delete</span>
      </button>
    </div>
  </div>
  <hr />
</template>

<style scoped></style>
