<template>
  <div class="w-full item">
    <q-card flat bordered class="my-card" :class="$q.dark.isActive ? 'bg-grey-9' : 'bg-grey-2'">
      <q-card-section>
        <div class="row items-center no-wrap">
          <div class="col">
            <div class="text-h6">{{ props.project.name }}</div>
            <!--<div class="text-subtitle2">by John Doe</div> -->
          </div>
        </div>
      </q-card-section>
      <q-card-section>
        {{ props.project.description }}
      </q-card-section>

      <q-separator />

      <q-card-actions>
        <div class="w-full row justify-end items-end">
          <!--<q-btn flat>View</q-btn>
          <q-btn flat>Delete</q-btn> -->
          <q-btn flat>Open</q-btn>
          <div class="col-auto">
            <q-btn color="grey-7" round flat icon="more_vert">
              <q-menu cover auto-close>
                <q-list>
                  <q-item clickable>
                    <q-item-section>View</q-item-section>
                  </q-item>
                  <q-item clickable @click="updateProject">
                    <q-item-section>Update</q-item-section>
                  </q-item>
                  <q-item clickable @click="deleteProject">
                    <q-item-section>Delete</q-item-section>
                  </q-item>
                  <q-item clickable>
                    <q-item-section>Export as JSON</q-item-section>
                  </q-item>
                </q-list>
              </q-menu>
            </q-btn>
          </div>
        </div>
      </q-card-actions>
    </q-card>
  </div>
</template>

<script setup lang="ts">
import { IProject } from '../../interfaces';

const props = defineProps({
  project: {
    type: Object as () => IProject,
    required: true
  }
})
const emit = defineEmits(['deleteProject', 'updateProject']);

const deleteProject = () => {
  emit('deleteProject');
}

const updateProject = () => {
  emit('updateProject');
}
</script>

<style scoped lang="scss">

</style>
