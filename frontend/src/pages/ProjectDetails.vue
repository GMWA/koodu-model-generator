<script setup lang="ts">
import Sidebar from "../components/Sidebar.vue";
import Footer from "../components/Footer.vue";
import { useRouter, useRoute } from "vue-router";
import { useProjectStore } from "../store/project.store";
import { onMounted, reactive, ref, Ref, ReactiveEffect } from "vue";
import { IProject } from "../types/projects.type";

interface IProjectRoute {
  id: number;
}
const projects = useProjectStore();
//const props = defineProps<ITodoRoute>();
const router = useRouter();
const route = useRoute();
let projectId: Ref<string | string[]> = ref("");
let project: Ref<IProject> = ref({
  id: 0,
  name: "",
});

const activeTab: Ref<string> = ref("configs");

onMounted(async () => {
  await projects.getItems();
  await router.isReady();
  projectId.value = route.params.id;
  const idx = projects.items.findIndex((elem) => String(elem.id) === projectId.value);
  project.value = { ...projects.items[idx] };
});

const changeActiveTab = (newTAb: string) => {
  activeTab.value = newTAb;
};
</script>

<template>
  <div class="flex w-full">
    <Sidebar />

    <main class="flex flex-col w-full">
      <div class="flex flex-col w-full rounded-3xl mb-10">
        <p class="text-3xl font-extrabold tracking-tight text-slate-900">
          {{ project.name }}
        </p>
      </div>

      <div class="flex w-full">
        <div class="border-b border-gray-200 dark:border-gray-700 w-full">
          <ul
            class="flex flex-wrap -mb-px text-sm font-medium text-center text-gray-500 dark:text-gray-400"
          >
            <li class="mr-2">
              <a
                href="#"
                @click="changeActiveTab('configs')"
                class="inline-flex p-4 rounded-t-lg border-b-2 group"
                :class="{
                  'border-blue-600 active text-blue-600 dark:text-blue-500 dark:border-blue-500':
                    activeTab === 'configs',
                  'border-transparent hover:text-gray-600 hover:border-gray-300 dark:hover:text-gray-300':
                    activeTab !== 'configs',
                }"
              >
                Configs
              </a>
            </li>
            <li class="mr-2">
              <a
                href="#"
                @click="changeActiveTab('tables')"
                class="inline-flex p-4 rounded-t-lg border-b-2 group"
                :class="{
                  'border-blue-600 active text-blue-600 dark:text-blue-500 dark:border-blue-500':
                    activeTab === 'tables',
                  'border-transparent hover:text-gray-600 hover:border-gray-300 dark:hover:text-gray-300':
                    activeTab !== 'tables',
                }"
              >
                Tables
              </a>
            </li>
            <li class="mr-2">
              <a
                href="#"
                @click="changeActiveTab('settings')"
                class="inline-flex p-4 rounded-t-lg border-b-2 group"
                :class="{
                  'border-blue-600 active text-blue-600 dark:text-blue-500 dark:border-blue-500':
                    activeTab === 'settings',
                  'border-transparent hover:text-gray-600 hover:border-gray-300 dark:hover:text-gray-300':
                    activeTab !== 'settings',
                }"
              >
                Settings
              </a>
            </li>
            <li class="mr-2">
              <a
                href="#"
                @click="changeActiveTab('contacts')"
                class="inline-flex p-4 rounded-t-lg border-b-2 group"
                :class="{
                  'border-blue-600 active text-blue-600 dark:text-blue-500 dark:border-blue-500':
                    activeTab === 'contacts',
                  'border-transparent hover:text-gray-600 hover:border-gray-300 dark:hover:text-gray-300':
                    activeTab !== 'contacts',
                }"
              >
                Contacts
              </a>
            </li>
            <li>
              <a
                class="inline-block p-4 text-gray-400 rounded-t-lg cursor-not-allowed dark:text-gray-500"
              >
                Disabled
              </a>
            </li>
          </ul>
        </div>
      </div>

      <div class="flex w-full">
        <div v-if="activeTab === 'configs'">Configs</div>
        <div v-if="activeTab === 'tables'">Tables</div>
        <div v-if="activeTab === 'settings'">Settings</div>
        <div v-if="activeTab === 'contacts'">Contacts</div>
      </div>

      <Footer />
    </main>
  </div>
</template>

<style lang="sass" scoped></style>
