<script setup lang="ts">
import { useRoute, useRouter } from "vue-router";
import Sidebar from "../components/Sidebar.vue";
import Footer from "../components/Footer.vue";
import Header from "../components/Header.vue";
import ProjectCard from "../components/ProjectCard.vue";
import { IProject } from "../types/projects.type";
import { ref, Ref, computed, onMounted } from "vue";
import { useProjectStore } from "../store/project.store";

const router = useRouter();
const route = useRoute();
const is_add_modal_open: Ref = ref(false);
const is_edit_modal_open: Ref = ref(false);
const is_delete_modal_open: Ref = ref(false);

const toCreateProject: Ref<IProject> = ref({ id: 0, name: "" });
const toEditProject: Ref<IProject> = ref({ id: 0, name: "" });
const toDeleteProject: Ref<IProject> = ref({ id: 0, name: "" });

const projects = useProjectStore();

const items = computed(() => projects.items);

const openAddModal = () => {
  is_add_modal_open.value = true;
};
const closeAddModal = () => {
  is_add_modal_open.value = false;
};

const openEditModal = (project: IProject) => {
  toEditProject.value = { ...project };
  is_edit_modal_open.value = true;
};
const closeEditModal = () => {
  is_edit_modal_open.value = false;
};

const openDeleteModal = (project: IProject) => {
  toDeleteProject.value = { ...project };
  is_delete_modal_open.value = true;
};

const closeDeleteModal = () => {
  is_delete_modal_open.value = false;
};

const navigateToProject = async (project: IProject) => {
  await router.push(`/project-details/${project.id}`);
};

const deleteProject = async () => {
  console.log(toDeleteProject.value);
  await projects.removeItem(toDeleteProject.value.id);
  closeDeleteModal();
}

const updateProject = async () => {
  await projects.updateItem(toEditProject.value);
  toEditProject.value = { id: 0, name: "" };
  await closeEditModal();
}

const createProject = async () => {
  await projects.addItem(toCreateProject.value);
  toCreateProject.value = { id: 0, name: "" };
  await closeDeleteModal();
}

onMounted(async () => {
  await projects.getItems();
  console.log(projects.items)
});
</script>

<template>
  <div class="flex w-full">
    <Sidebar />

    <main class="flex flex-col w-full">
      <Header type="page" title="Projects" />

      <div @click="openAddModal" class="flex flex-row-reverse pr-20 px-10 py-2">
        <div class="w-12 h-12 rounded-full text-white bg-green-600 content-center">
          <button class="text-white font-bold content-center w-full h-full">
            <span class="material-icons">add</span>
          </button>
        </div>
      </div>

      <div class="grid grid-cols-4 gap-4 pl-10 pr-20">
        <ProjectCard
          v-if="items"
          v-for="(project, idx) in items"
          :key="idx"
          :project="project"
          @choose="navigateToProject(project)"
          @delete="openDeleteModal"
          @edit="openEditModal"
        />
      </div>

      <Footer />
    </main>

    <!--Add Modal-->

    <div
      class="overflow-y-auto overflow-x-auto fixed flex items-center justify-center bg-gray-900 bg-opacity-50 z-50 w-full md:inset-0 md:h-full transition duration-150 ease-in-out"
      :class="{ hidden: !is_add_modal_open }"
    >
      <div class="flex items-center justify-center w-full max-w-2xl h-screen md:h-auto">
        <!-- Modal content -->
        <div class="center bg-white rounded-lg shadow dark:bg-gray-700 w-full">
          <!-- Modal header -->
          <div
            class="flex justify-between items-start p-4 rounded-t border-b dark:border-gray-600"
          >
            <h3 class="text-xl font-semibold text-gray-900 dark:text-white">
              Add Project
            </h3>
            <button
              @click="closeAddModal"
              type="button"
              class="text-gray-400 bg-transparent hover:bg-gray-200 hover:text-gray-900 rounded-lg text-sm p-1.5 ml-auto inline-flex items-center dark:hover:bg-gray-600 dark:hover:text-white"
              data-modal-toggle="defaultModal"
            >
              <svg
                aria-hidden="true"
                class="w-5 h-5"
                fill="currentColor"
                viewBox="0 0 20 20"
                xmlns="http://www.w3.org/2000/svg"
              >
                <path
                  fill-rule="evenodd"
                  d="M4.293 4.293a1 1 0 011.414 0L10 8.586l4.293-4.293a1 1 0 111.414 1.414L11.414 10l4.293 4.293a1 1 0 01-1.414 1.414L10 11.414l-4.293 4.293a1 1 0 01-1.414-1.414L8.586 10 4.293 5.707a1 1 0 010-1.414z"
                  clip-rule="evenodd"
                ></path>
              </svg>
              <span class="sr-only">Close modal</span>
            </button>
          </div>
          <!-- Modal body -->
          <div class="p-6 space-y-6 w-full">
            <form class="flex flex-col w-full">
              <label for="name">Name:</label>
              <input
                type="text"
                name="name"
                class="form-input px-4 py-3 mt-1 rounded-2xl"
                placeholder="Name"
                v-model="toCreateProject.name"
              />
              <label class="mt-4" for="desciption"> Description: </label>
              <textarea
                name="description"
                class="form-input px-4 py-3 mt-1 rounded-2xl"
                rows="10"
                placeholder="Description"
                v-model="toCreateProject.description"
              >
              </textarea>
            </form>
          </div>
          <!-- Modal footer -->
          <div
            class="flex flex-row-reverse items-center p-6 space-x-2 rounded-b border-t border-gray-200 dark:border-gray-600"
          >
            <button
              @click="createProject"
              type="button"
              class="text-white bg-blue-700 hover:bg-blue-800 focus:ring-4 focus:outline-none focus:ring-blue-300 font-medium rounded-lg text-sm px-5 py-2.5 text-center dark:bg-blue-600 dark:hover:bg-blue-700 dark:focus:ring-blue-800"
            >
              Add
            </button>
            <button
              @click="closeAddModal"
              type="button"
              class="text-gray-500 bg-white hover:bg-gray-100 focus:ring-4 focus:outline-none focus:ring-blue-300 rounded-lg border border-gray-200 text-sm font-medium px-5 py-2.5 hover:text-gray-900 focus:z-10 dark:bg-gray-700 dark:text-gray-300 dark:border-gray-500 dark:hover:text-white dark:hover:bg-gray-600 dark:focus:ring-gray-600"
            >
              Decline
            </button>
          </div>
        </div>
      </div>
    </div>

    <!--Edit Modal-->

    <div
      class="overflow-y-auto overflow-x-auto fixed flex items-center justify-center bg-gray-900 bg-opacity-50 z-50 w-full md:inset-0 md:h-full transition duration-150 ease-in-out"
      :class="{ hidden: !is_edit_modal_open }"
    >
      <div class="flex items-center justify-center w-full max-w-2xl h-screen md:h-auto">
        <!-- Modal content -->
        <div class="center bg-white rounded-lg shadow dark:bg-gray-700 w-full">
          <!-- Modal header -->
          <div
            class="flex justify-between items-start p-4 rounded-t border-b dark:border-gray-600"
          >
            <h3 class="text-xl font-semibold text-gray-900 dark:text-white">
              Edit Project
            </h3>
            <button
              @click="closeEditModal"
              type="button"
              class="text-gray-400 bg-transparent hover:bg-gray-200 hover:text-gray-900 rounded-lg text-sm p-1.5 ml-auto inline-flex items-center dark:hover:bg-gray-600 dark:hover:text-white"
              data-modal-toggle="defaultModal"
            >
              <svg
                aria-hidden="true"
                class="w-5 h-5"
                fill="currentColor"
                viewBox="0 0 20 20"
                xmlns="http://www.w3.org/2000/svg"
              >
                <path
                  fill-rule="evenodd"
                  d="M4.293 4.293a1 1 0 011.414 0L10 8.586l4.293-4.293a1 1 0 111.414 1.414L11.414 10l4.293 4.293a1 1 0 01-1.414 1.414L10 11.414l-4.293 4.293a1 1 0 01-1.414-1.414L8.586 10 4.293 5.707a1 1 0 010-1.414z"
                  clip-rule="evenodd"
                ></path>
              </svg>
              <span class="sr-only">Close modal</span>
            </button>
          </div>
          <!-- Modal body -->
          <div class="p-6 space-y-6 w-full">
            <form class="flex flex-col w-full">
              <label for="name">Name:</label>
              <input
                type="text"
                name="name"
                class="form-input px-4 py-3 mt-1 rounded-2xl"
                placeholder="Name"
                v-model="toEditProject.name"
              />
              <label class="mt-4" for="desciption"> Description: </label>
              <textarea
                name="description"
                class="form-input px-4 py-3 mt-1 rounded-2xl"
                rows="10"
                placeholder="Description"
                v-model="toEditProject.description"
              >
              </textarea>
            </form>
          </div>
          <!-- Modal footer -->
          <div
            class="flex flex-row-reverse items-center p-6 space-x-2 rounded-b border-t border-gray-200 dark:border-gray-600"
          >
            <button
              @click="updateProject"
              type="button"
              class="text-white bg-blue-700 hover:bg-blue-800 focus:ring-4 focus:outline-none focus:ring-blue-300 font-medium rounded-lg text-sm px-5 py-2.5 text-center dark:bg-blue-600 dark:hover:bg-blue-700 dark:focus:ring-blue-800"
            >
              Edit
            </button>
            <button
              @click="closeEditModal"
              type="button"
              class="text-gray-500 bg-white hover:bg-gray-100 focus:ring-4 focus:outline-none focus:ring-blue-300 rounded-lg border border-gray-200 text-sm font-medium px-5 py-2.5 hover:text-gray-900 focus:z-10 dark:bg-gray-700 dark:text-gray-300 dark:border-gray-500 dark:hover:text-white dark:hover:bg-gray-600 dark:focus:ring-gray-600"
            >
              Decline
            </button>
          </div>
        </div>
      </div>
    </div>

    <!--Delete Modal-->

    <div
      class="overflow-y-auto overflow-x-auto fixed flex items-center justify-center bg-gray-900 bg-opacity-50 z-50 w-full md:inset-0 md:h-full transition duration-150 ease-in-out"
      :class="{ hidden: !is_delete_modal_open }"
    >
      <div class="flex items-center justify-center w-full max-w-2xl h-screen md:h-auto">
        <!-- Modal content -->
        <div class="center bg-white rounded-lg shadow dark:bg-gray-700 w-full">
          <!-- Modal header -->
          <div
            class="flex justify-between items-start p-4 rounded-t border-b dark:border-gray-600"
          >
            <h3 class="text-xl font-semibold text-gray-900 dark:text-white">
              Delete Project
            </h3>
            <button
              @click="closeDeleteModal"
              type="button"
              class="text-gray-400 bg-transparent hover:bg-gray-200 hover:text-gray-900 rounded-lg text-sm p-1.5 ml-auto inline-flex items-center dark:hover:bg-gray-600 dark:hover:text-white"
              data-modal-toggle="defaultModal"
            >
              <svg
                aria-hidden="true"
                class="w-5 h-5"
                fill="currentColor"
                viewBox="0 0 20 20"
                xmlns="http://www.w3.org/2000/svg"
              >
                <path
                  fill-rule="evenodd"
                  d="M4.293 4.293a1 1 0 011.414 0L10 8.586l4.293-4.293a1 1 0 111.414 1.414L11.414 10l4.293 4.293a1 1 0 01-1.414 1.414L10 11.414l-4.293 4.293a1 1 0 01-1.414-1.414L8.586 10 4.293 5.707a1 1 0 010-1.414z"
                  clip-rule="evenodd"
                ></path>
              </svg>
              <span class="sr-only">Close modal</span>
            </button>
          </div>
          <!-- Modal body -->
          <div class="p-6 space-y-6 w-full">
            <p class="text-2xl">
              Are you sur you want to delete the Project {{ toDeleteProject.name }}?
            </p>
          </div>
          <!-- Modal footer -->
          <div
            class="flex flex-row-reverse items-center p-6 space-x-2 rounded-b border-t border-gray-200 dark:border-gray-600"
          >
            <button
              @click="deleteProject"
              type="button"
              class="text-white bg-blue-700 hover:bg-blue-800 focus:ring-4 focus:outline-none focus:ring-blue-300 font-medium rounded-lg text-sm px-5 py-2.5 text-center dark:bg-blue-600 dark:hover:bg-blue-700 dark:focus:ring-blue-800"
            >
              Delete
            </button>
            <button
              @click="closeDeleteModal"
              type="button"
              class="text-gray-500 bg-white hover:bg-gray-100 focus:ring-4 focus:outline-none focus:ring-blue-300 rounded-lg border border-gray-200 text-sm font-medium px-5 py-2.5 hover:text-gray-900 focus:z-10 dark:bg-gray-700 dark:text-gray-300 dark:border-gray-500 dark:hover:text-white dark:hover:bg-gray-600 dark:focus:ring-gray-600"
            >
              Decline
            </button>
          </div>
        </div>
      </div>
    </div>
  </div>
</template>

<style lang="sass" scoped></style>
