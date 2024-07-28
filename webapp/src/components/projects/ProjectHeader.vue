<template>
  <div class="q-pa-md">
    <p class="text-h6" style="margin-bottom: 0px;">
      {{ props.project.name }}
    </p>
  </div>
</template>

<script setup lang="ts">
import { IProject } from '../../interfaces';

const props = defineProps({
  project: {
    type: Object as () => IProject,
    required: true,
  },
});
</script>

<style scoped lang="scss"></style>
