<script lang="ts" setup>
  const props = defineProps({
    type: {type: String, required: true},
    title: {type: String, required: true}
  })
</script>

<template>
  <div class="flex flex-col w-full rounded-3xl mb-10">
    <p class='text-gray-400'>
        {{ props.type }}
      </p>
      <p class='text-3xl font-extrabold tracking-tight text-slate-900'>
        {{ props.title }}
      </p>
  </div>
</template>

<style scoped>

</style>