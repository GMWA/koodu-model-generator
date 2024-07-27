<template>
  <div class="row w-full items-center q-pa-none q-ma-none" :class="{ 'bg-primary': props.active }">
    <div class="col-10 row w-full q-pa-sm">
      <div class="col-10 pl-4 text-h6 select-text "
        :class="{ 'text-white': props.active, 'text-primary': !props.table }" @click="handleChoose">
        {{
    props.table.name }}</div>
    </div>
    <div class="row col-2 w-full">
      <div class="col-6">
        <q-btn round color="white" text-color="primary" icon="edit" @click="handleEdit" />
      </div>
      <div class="col-6">
        <q-btn round color="white" text-color="red" icon="delete" @click="handleDelete" />
      </div>
    </div>
  </div>
  <q-separator />
</template>

<script lang="ts" setup>
import { ITable } from '../../interfaces';

interface ITableProps {
  table: ITable;
  active: boolean;
}
const props = defineProps<ITableProps>();
const emit = defineEmits(['delete', 'edit', 'select']);

const handleEdit = () => {
  emit('edit', props.table);
};

const handleDelete = () => {
  emit('delete', props.table);
};

const handleChoose = () => {
  emit('select', props.table);
};
</script>

<style scoped lang="scss">
.select-text {
  &:hover {
    cursor: pointer;
  }
}
</style>
