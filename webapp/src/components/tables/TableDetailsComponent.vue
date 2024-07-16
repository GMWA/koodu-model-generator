<template>
  <div class="">
    <div class="">
      <div class="">
        <div class="">Attributs for {{ table.name }}</div>
        <div class="grow"></div>
        <div class="">
          <q-btn
            color="primary"
            label="Add Attribut"
            @click="openAddModal"
            round
          />
        </div>
      </div>
    </div>
    <hr />
    <div v-if="items.length > 0">
      <div class="">
        <select class="" v-model="selectedAttribut">
          <option
            v-for="(attrib, index) in items"
            :key="index"
            :value="attrib"
            :selected="attrib.id === selectedAttribut.id"
          >
            {{ attrib.name }}
          </option>
        </select>
      </div>
      <hr />
      <div class="">
        <div class="">
          <div class="">
            <div>
              <label for="name" class="">Name</label>
              <input
                type="text"
                class=""
                placeholder="Name"
                v-model="selectedAttribut.name"
                required
              />
            </div>
            <div>
              <label for="type" class="">Type</label>
              <select class="" v-model="selectedAttribut.type">
                <option
                  v-for="(elem, idx) in attributTypes"
                  :key="idx"
                  :value="elem.value"
                >
                  {{ elem.name }}
                </option>
              </select>
            </div>
            <div>
              <label for="table" class="">Table</label>
              <select class="">
                <option v-for="(tab, idx) in tables" :value="tab.id" :key="idx">
                  {{ tab.name }}
                </option>
              </select>
            </div>
            <div>
              <label for="phone" class="">Is Index</label>
              <input
                v-model="selectedAttribut.index_key"
                type="checkbox"
                value=""
                class=""
              />
            </div>
            <div>
              <label for="website" class="">Size</label>
              <input
                type="number"
                class=""
                placeholder="Size"
                v-model="selectedAttribut.size"
                required
              />
            </div>
            <div>
              <label for="primary_key" class="">Is Primary key</label>
              <input
                v-model="selectedAttribut.primary_key"
                type="checkbox"
                value=""
                class=""
              />
            </div>
            <div>
              <label for="visitors" class="">Description</label>
              <textarea
                class=""
                placeholder="Description"
                v-model="selectedAttribut.description"
              >
              </textarea>
            </div>
            <div>
              <label for="visitors" class="">Is Unique</label>
              <input
                v-model="selectedAttribut.unique_key"
                id="red-checkbox"
                type="checkbox"
                value=""
                class=""
              />
            </div>
          </div>

          <button class="" @click="openDeleteModal">Delete</button>
          <button type="submit" @click="editAttribut" class="">Save</button>
        </div>
      </div>
    </div>

    <!--Add Modal-->
    <q-dialog
      persistent
      v-model="isAddModalOpen"
      backdrop-filter="backdrop-filter"
      transition-show="flip-down"
      transition-hide="flip-up"
    >
      <q-card style="min-width: 600px; padding: 20px">
        <q-card-section class="row items-center q-p-none">
          <div class="text-h6">Add Table to Project</div>
          <q-space />
          <q-btn icon="close" flat round dense v-close-popup />
        </q-card-section>

        <q-card-section class="w-full q-pa-none">
          <q-form @submit="addAttribut" class="w-full q-pa-none q-am-none">
            <q-input
              class="w-full q-pa-md"
              v-model="toCreateAttribut.name"
              label="Name"
              outlined
              clearable
              required
            />
            <q-input
              class="w-full q-pa-md"
              type="textarea"
              v-model="toCreateAttribut.description"
              label="Description"
              outlined
              clearable
              required
            />
            <q-input
              class="w-full q-pa-md"
              type="number"
              v-model="toCreateAttribut.size"
              label="Size"
              outlined
              clearable
              required
            />
            <q-checkbox
              class="w-full q-pa-md"
              type="checkbox"
              v-model="toCreateAttribut.index_key"
              label="Is Index"
              outlined
              clearable
              required
            />
            <q-checkbox
              class="w-full q-pa-md"
              v-model="toCreateAttribut.primary_key"
              label="Is Primary key"
              outlined
              clearable
              required
            />
            <q-checkbox
              class="w-full q-pa-md"
              type="checkbox"
              v-model="toCreateAttribut.unique_key"
              label="Is Unique"
              outlined
              clearable
              required
            />
            <q-checkbox
              class="w-full q-pa-md"
              type="checkbox"
              v-model="toCreateAttribut.is_required"
              label="Is Required"
              outlined
              clearable
              required
            />
            <q-input
              class="w-full q-pa-md"
              type="text"
              v-model="toCreateAttribut.type"
              label="Type"
              outlined
              clearable
              required
            />
            <q-btn
              type="submit"
              color="primary"
              label="Add Table"
              class="w-full q-pa-md q-mt-md"
            />
          </q-form>
        </q-card-section>
      </q-card>
    </q-dialog>

    <!--Delete Modal-->
    <q-dialog
      persistent
      v-model="isDeleteModalOpen"
      backdrop-filter="backdrop-filter"
      transition-show="flip-down"
      transition-hide="flip-up"
    >
      <q-card style="min-width: 600px; padding: 20px">
        <q-card-section class="row items-center q-p-none">
          <div class="text-h6">Delete project</div>
          <q-space />
          <q-btn icon="close" flat round dense v-close-popup />
        </q-card-section>

        <q-card-section class="w-full q-pa-none">
          <p>Are you sure you want to delete {{ toDeleteAttribut?.name }}?</p>
        </q-card-section>

        <q-card-actions>
          <q-btn
            color="primary"
            label="Cancel"
            class="q-mr-md"
            @click="isDeleteModalOpen = false"
          />
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
</script>

<style scoped lang="scss"></style>
