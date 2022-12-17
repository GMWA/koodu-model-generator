<script lang="ts" , setup>
import { ITable } from "../types/tables.type";
import { useAttributStore } from "../store/attributs.store";
import { reactive } from "vue";

interface TableProps {
  table: ITable;
}
const props = withDefaults(defineProps<TableProps>(), {});
const table = reactive(props.table);
const emit = defineEmits(["delete", "edit", "choose"]);
const attributs = useAttributStore();
</script>

<template>
  <div class="flex flex-col">
    <div>{{ table.name }}</div>
    <div>Select</div>
    <div>Body</div>
  </div>
</template>

<style scoped></style>
