<template>
  <div class="w-full h-full">
    <div class="w-full q-pa-sm items-end">
      <div class="row items-center">
        <div class="col-11">
          <p class="text-h4">Attributs for {{ table.name }}</p>
        </div>
        <div class="col-1 justify-end">
          <q-btn color="primary" icon="add" @click="openAddModal" round />
        </div>
      </div>
    </div>
    <q-separator />
    <div v-if="items.length > 0">
      <div class="">
        <select class="" v-model="selectedAttribut">
          <option v-for="(attrib, index) in items" :key="index" :value="attrib"
            :selected="attrib.id === selectedAttribut.id">
            {{ attrib.name }}
          </option>
        </select>
      </div>
      <q-separator />
      <div class="w-full">
        <div class="w-full">
          <q-form class="w-full">
            <q-input v-model="selectedAttribut.name" type="text" label="Name" class="" required />
            <q-select outlined v-model="selectedAttribut.type" :options="attributTypes" label="Type" />
            <q-select outlined v-model="selectedAttribut.table_id" :options="buildTableOptions(tables)" label="Table" />
            <q-checkbox v-model="selectedAttribut.index_key" label="Is Index" />
            <q-checkbox v-model="selectedAttribut.primary_key" label="Is Primary key" />
            <q-checkbox v-model="selectedAttribut.unique_key" label="Is Unique" />
            <q-checkbox v-model="selectedAttribut.is_required" label="Is Required" />
            <q-input v-model="selectedAttribut.size" type="number" label="Size" class="" required />
            <q-btn type="submit" @click="editAttribut" class="">Save</q-btn>
            <q-btn @click="openDeleteModal" class="">Delete</q-btn>
          </q-form>
        </div>
      </div>
    </div>
    <div v-else>
      <p>No attributs found</p>
    </div>

    <!--Add Modal-->
    <q-dialog persistent v-model="isAddModalOpen" backdrop-filter="backdrop-filter" transition-show="scale"
      transition-hide="scale">
      <q-card style="min-width: 600px; padding: 20px">
        <q-card-section class="row items-center q-p-none">
          <div class="text-h6">Add attribut to table</div>
          <q-space />
          <q-btn icon="close" flat round dense v-close-popup />
        </q-card-section>
        <q-card-section class="w-full q-pa-none">
          <q-form @submit="addAttribut" class="w-full q-pa-none q-am-none">
            <q-input class="w-full q-pa-md" v-model="toCreateAttribut.name" label="Name" outlined clearable required />
            <q-input class="w-full q-pa-md" type="textarea" v-model="toCreateAttribut.description" label="Description"
              outlined clearable required />
            <div class="row w-full q-pa-none q-ma-none">
              <q-input class="col q-pa-md" type="number" v-model="toCreateAttribut.size" label="Size" outlined
                required />
              <q-select class="col q-pa-md" v-model="toCreateAttribut.type" :options="attributTypes" label="Type"
                outlined required />
            </div>
            <div class="row w-full q-pa-none q-ma-none">
              <q-checkbox class="col q-pa-md" type="checkbox" v-model="toCreateAttribut.index_key" label="Is Index"
                outlined clearable required />
              <q-checkbox class="col q-pa-md" v-model="toCreateAttribut.primary_key" label="Is Primary key" outlined
                clearable required />
            </div>
            <div class="row w-full q-pa-none q-ma-none">
              <q-checkbox class="col q-pa-md" type="checkbox" v-model="toCreateAttribut.unique_key" label="Is Unique"
                outlined clearable required />
              <q-checkbox class="col q-pa-md" type="checkbox" v-model="toCreateAttribut.is_required" label="Is Required"
                outlined clearable required />
            </div>
            <q-btn type="submit" color="primary" label="Add Attribut to table" class="w-full q-pa-md q-mt-md" />
          </q-form>
        </q-card-section>
      </q-card>
    </q-dialog>

    <!--Delete Modal-->
    <q-dialog persistent v-model="isDeleteModalOpen" backdrop-filter="backdrop-filter" transition-show="scale"
      transition-hide="scale">
      <q-card style="min-width: 600px; padding: 20px">
        <q-card-section class="row items-center q-p-none">
          <div class="text-h6">Delete attribute from table</div>
          <q-space />
          <q-btn icon="close" flat round dense v-close-popup />
        </q-card-section>

        <q-card-section class="w-full q-pa-none">
          <p>Are you sure you want to delete {{ toDeleteAttribut?.name }}?</p>
        </q-card-section>

        <q-card-actions>
          <q-btn color="primary" label="Cancel" class="q-mr-md" @click="isDeleteModalOpen = false" />
          <q-btn color="negative" label="Delete" @click="deleteAttribut" />
        </q-card-actions>
      </q-card>
    </q-dialog>
  </div>
</template>

<script lang="ts" setup>
import { ITable } from '../../interfaces';
import { IAttribut } from '../../interfaces';
import { useAttributStore } from '../../stores/attributStore';
import { watch, Ref, ref, computed, onMounted } from 'vue';
import { ISelectOption } from '../../interfaces';
import { attributTypes } from '../../constants/attributs';

interface TableProps {
  table: ITable;
  tables: ITable[];
}
const attributsStore = useAttributStore();
const props = withDefaults(defineProps<TableProps>(), {});
let table: ITable = props.table;
let tables: ITable[] = props.tables;
// const emit = defineEmits(['delete', 'edit', 'select']);
const DEFAULT_ATTRIBUT: IAttribut = {
  id: 0,
  name: '',
  table_id: table.id,
  index_key: false,
  primary_key: false,
  unique_key: false,
  is_required: false,
  type: 'str',
  size: 0,
};
const selectedAttribut: Ref<IAttribut> = ref(DEFAULT_ATTRIBUT);
const isAddModalOpen: Ref = ref(false);
const isDeleteModalOpen: Ref = ref(false);
const toCreateAttribut: Ref<IAttribut> = ref(DEFAULT_ATTRIBUT);
// const toEditAttribut: Ref<IAttribut> = ref(DEFAULT_ATTRIBUT);
const toDeleteAttribut: Ref<IAttribut> = ref(DEFAULT_ATTRIBUT);

watch(
  () => props.table,
  async (first) => {
    table = { ...first };
    await attributsStore.getAttributByTableId(first.id);
    if (items.value.length > 0) {
      selectedAttribut.value = { ...items.value[0] };
      toCreateAttribut.value.table_id = props.table.id;
    }
  }
);

const items = computed(() => attributsStore.attributs);

// const setSelectedAttribut = (attrib: IAttribut) => {
//   selectedAttribut.value = { ...attrib };
// };

const openAddModal = () => {
  isAddModalOpen.value = true;
};

const closeAddModal = () => {
  isAddModalOpen.value = false;
};

const openDeleteModal = () => {
  toDeleteAttribut.value = { ...selectedAttribut.value };
  isDeleteModalOpen.value = true;
};

const closeDeleteModal = () => {
  isDeleteModalOpen.value = false;
};

const addAttribut = async () => {
  toCreateAttribut.value.table_id = table.id;
  await attributsStore.createAttribut(toCreateAttribut.value);
  if (items.value.length > 0) {
    selectedAttribut.value = { ...items.value[items.value.length - 1] };
    toCreateAttribut.value.table_id = props.table.id;
  }
  toCreateAttribut.value = DEFAULT_ATTRIBUT;
  closeAddModal();
};

const editAttribut = async () => {
  selectedAttribut.value.table_id = table.id;
  await attributsStore.updateAttribut(selectedAttribut.value);
  console.log(selectedAttribut.value);
};

const deleteAttribut = async () => {
  await attributsStore.deleteAttribut(toDeleteAttribut.value.id);
  toDeleteAttribut.value = { ...DEFAULT_ATTRIBUT };
  closeDeleteModal();
};

onMounted(async () => {
  await attributsStore.getAttributByTableId(props.table.id);
  if (items.value.length > 0) {
    selectedAttribut.value = { ...items.value[0] };
    toCreateAttribut.value.table_id = props.table.id;
  }
});

const buildTableOptions = (tables: ITable[]): ISelectOption[] => {
  return tables.map((table) => {
    return {
      label: table.name,
      value: `${table.id}`,
    };
  });
};
</script>

<style scoped lang="scss"></style>
