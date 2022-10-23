<script setup lang="ts">

</script>

<template>
   <div class="app">
    <router-view />
  </div>
</template>

<style lang="scss">
	:root {
		--primary: #4ade80;
		--primary-alt: #22c55e;
		--grey: #64748b;
		--dark: #1e293b;
		--dark-alt: #334155;
		--light: #f1f5f9;
		--sidebar-width: 300px;
	}
	* {
		margin: 0;
		padding: 0;
		box-sizing: border-box;
		font-family: 'Fira sans', sans-serif;
	}
	body {
		background: var(--light);
	}
	.app {
		display: flex;
		main {
			flex: 1 1 0;
			padding: 0;
			@media (max-width: 1024px) {
				padding-left: 4rem;
			}
		}
	}
</style>
