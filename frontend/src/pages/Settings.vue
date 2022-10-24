<script setup lang="ts">
	import Sidebar from "../components/Sidebar.vue";
	import Footer from "../components/Footer.vue";
	import Header from "../components/Header.vue";
</script>

<template>
	<div class="flex">
		<Sidebar />
		
    <main class="flex flex-col w-full">
			<Header
				type="page"
				title="Settings"
			/>

			<div>Settings page</div>
    
			<Footer />
		</main>
	</div>
</template>

<style lang="sass" scoped>

</style>