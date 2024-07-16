<script lang="ts" setup>
import { ITable } from '../../interfaces';
import { ref, watch } from 'vue';

interface TableProps {
  table: ITable;
  active: boolean;
}
const props = withDefaults(defineProps<TableProps>(), {});
const table = props.table;
const isActive = ref(props.active);
const emit = defineEmits(['delete', 'edit', 'select']);

watch(
  () => props.active,
  (first) => {
    isActive.value = first;
  }
);

const handleEdit = () => {
  emit('edit', table);
};

const handleDelete = () => {
  emit('delete', table);
};

const handleChoose = () => {
  emit('select', table);
};
</script>

<template>
  <div
    class="flex flex-row w-full h-14 align-middle pr-2 hover:cursor-pointer hover:bg-gray-200"
    :class="{ 'bg-green-200': isActive }"
  >
    <div class="pl-4 text-xl" @click="handleChoose">{{ table.name }}</div>
    <div class="grow"></div>
    <div class="mr-2">
      <q-btn flat color="green" icon="edit" @click="handleEdit" />
    </div>
    <div class="">
      <q-btn flat color="red" icon="delete" @click="handleDelete" />
    </div>
  </div>
  <hr />
</template>

<style scoped lang="scss"></style>
