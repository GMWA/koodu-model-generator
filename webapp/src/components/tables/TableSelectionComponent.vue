<template>
  <div class="row w-full items-center q-pa-md" :class="{ 'bg-green-200': isActive }">
    <div class=" col-8 pl-4 text-xl" @click="handleChoose">{{ table.name }}</div>
    <div class="col-2">
      <q-btn round color="green" icon="edit" @click="handleEdit" />
    </div>
    <div class="col-2">
      <q-btn round color="red" icon="delete" @click="handleDelete" />
    </div>
  </div>
  <hr />
</template>

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

<style scoped lang="scss"></style>
