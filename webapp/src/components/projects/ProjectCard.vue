<template>
  <div>
    <h1>Project Card</h1>
    <p>{{ props.project.name }}</p>
  </div>
</template>

<script setup lang="ts">
import { IProject } from '../../interfaces';

const props =  defineProps({
  project: {
    type: Object as () => IProject,
    required: true
  }
})
</script>
