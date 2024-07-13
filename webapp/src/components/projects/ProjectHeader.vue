<template>
  <div class="q-pa-md">
    {{ props.project.name }}
  </div>
</template>

<script setup lang="ts">
import { IProject } from '../../interfaces';


const props = defineProps({
  project: {
    type: Object as () => IProject,
    required: true,
  }
})

</script>

<style scoped lang="scss">
</style>
