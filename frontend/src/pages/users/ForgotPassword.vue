<script setup lang="ts">
import ThirdPartyEmailPassword from "supertokens-web-js/recipe/thirdpartyemailpassword";
import { ref, Ref } from "vue";

const tokenPresent = ref(false);
const error = ref(false);
const didSubmit = ref(false);
const errorMessage = ref("");
const email = ref("");
const password = ref("");

const onSubmitClicked = async () => {
  if (tokenPresent.value) {
    try {
      const response = await ThirdPartyEmailPassword.submitNewPassword({
        formFields: [
          {
            id: "password",
            value: password.value,
          },
        ],
      });
      if (response.status === "FIELD_ERROR") {
        throw new Error(response.formFields[0].error);
      } else if (response.status === "RESET_PASSWORD_INVALID_TOKEN_ERROR") {
        throw new Error(
          "Password reset token has expired, please go back to the sign in page"
        );
      }
      window.location.assign("/auth");
    } catch (e: any) {
      errorMessage.value = e.message;
      error.value = true;
    }
  } else {
    try {
      const response = await ThirdPartyEmailPassword.sendPasswordResetEmail({
        formFields: [
          {
            id: "email",
            value: email.value,
          },
        ],
      });
      if (response.status !== "OK") {
        throw new Error(response.formFields[0].error);
      }
      if (didSubmit.value !== true) {
        didSubmit.value = true;
      }
    } catch (e: any) {
      errorMessage.value = e.message;
      error.value = true;
    }
  }
};
</script>

<template>
  <main>
    <div
      class="min-h-screen min-w-screen bg-gray-100 text-gray-800 antialiased py-6 flex-col justify-center sm:py-12"
    >
      <div class="relative py-3 sm:w-96 mx-auto text-center">
        <span class="text-3xl font-bold"> Model Generator App </span>
        <div class="mt-4 bg-white shadow-md rounded-lg text-left">
          <div class="h-3 bg-green-400 rounded-t-md"></div>
          <div v-if="didSubmit" class="px-8 py-6">
            <div class="w-full mt-0 text-center text-md">
              <span> Reset your password </span>
            </div>

            <div v-if="error" class="w-full text-red-400">
              <p>
                {{ errorMessage }}
              </p>
            </div>

            <label class="block font-semibold mt-4" for="passeword">
              New Password:
            </label>
            <input
              class="border w-full h-5 px-3 py-5 mt-2 hover:outline-none focus:outline-none focus:ring-1 focus:ring-green-400 rounded-md"
              type="password"
              name="email"
              placeholder="Password"
            />
            <button
              type="submit"
              class="mt-4 bg-green-500 text-white py-2 px-6 w-full rounded-md hover:bg-green-600"
              @click="onSubmitClicked"
            >
              Change Password
            </button>

            <div class="w-full mt-4 items-center text-center">
              <a href="/auth" class="mt-4 text-sm hover:underline"> back to login? </a>
            </div>
          </div>
          <div v-else class="px-8 py-6">
            <div class="w-full mt-0 text-center text-md">
              <span> Email to reset password </span>
            </div>

            <div v-if="error" class="w-full text-red-400">
              <p>
                {{ errorMessage }}
              </p>
            </div>
            <div v-if="!didSubmit" class="w-full">
              <label class="block font-semibold mt-4" for="email"> Email: </label>
              <input
                class="border w-full h-5 px-3 py-5 mt-2 hover:outline-none focus:outline-none focus:ring-1 focus:ring-green-400 rounded-md"
                type="text"
                name="email"
                placeholder="Email"
              />
              <button
                type="submit"
                class="mt-4 bg-green-500 text-white py-2 px-6 w-full rounded-md hover:bg-green-600"
              >
                Email Me
              </button>
            </div>
            <div v-else class="w-full">
              <div class="w-full mt-0 text-center text-md">
                <span>
                  Please check your email for the password recovery link
                  <span class="resend-button" @click="onSubmitClicked"> Resend </span>
                </span>
              </div>
            </div>

            <div class="w-full mt-4 items-center text-center">
              <a href="/auth" class="mt-4 text-sm hover:underline"> back to login? </a>
            </div>
          </div>
        </div>
      </div>
    </div>
  </main>
</template>

<style scoped></style>
