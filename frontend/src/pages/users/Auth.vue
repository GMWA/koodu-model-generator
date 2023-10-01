<script setup lang="ts">
import { useRouter } from "vue-router";
import ThirdPartyEmailPassword from "supertokens-web-js/recipe/thirdpartyemailpassword";
import Session from "supertokens-web-js/recipe/session";
import { ref, Ref, onMounted } from "vue";
import { WEBSITE_DOMAIN } from "../../configs";

const router = useRouter();
const isSignIn = ref(true);
const email = ref("");
const password = ref("");
const error = ref(false);
const errorMessage = ref("Something went wrong");
const emailError = ref("");
const passwordError = ref("");

onMounted(() => {
  const params = new URLSearchParams(window.location.search);
  if (params.has("error")) {
    errorMessage.value = "Something went wrong";
    error.value = true;
  }
  checkForSession();
});

const goToSignUp = () => {
  isSignIn.value = false;
};

const goToSignIn = () => {
  isSignIn.value = true;
};

const signIn = async (_: Event) => {
  const response = await ThirdPartyEmailPassword.emailPasswordSignIn({
    formFields: [
      {
        id: "email",
        value: email.value,
      },
      {
        id: "password",
        value: password.value,
      },
    ],
  });
  if (response.status === "WRONG_CREDENTIALS_ERROR") {
    errorMessage.value = "Invalid credentials";
    error.value = true;
    return;
  }
  if (response.status === "FIELD_ERROR") {
    response.formFields.forEach((item) => {
      if (item.id === "email") {
        emailError.value = item.error;
      } else if (item.id === "password") {
        passwordError.value = item.error;
      }
    });
    console.log(response);
  } else {
    await router.push("/");
  }
};

const validateEmail = (email: string) => {
  return email
    .toLowerCase()
    .match(
      /^(([^<>()[\]\\.,;:\s@"]+(\.[^<>()[\]\\.,;:\s@"]+)*)|(".+"))@((\[[0-9]{1,3}\.[0-9]{1,3}\.[0-9]{1,3}\.[0-9]{1,3}\])|(([a-zA-Z\-0-9]+\.)+[a-zA-Z]{2,}))$/
    );
};

const signUp = async (_: Event) => {
  const response = await ThirdPartyEmailPassword.emailPasswordSignUp({
    formFields: [
      {
        id: "email",
        value: email.value,
      },
      {
        id: "password",
        value: password.value,
      },
    ],
  });
  if (response.status === "FIELD_ERROR") {
    response.formFields.forEach((item) => {
      if (item.id === "email") {
        emailError.value = item.error;
      } else if (item.id === "password") {
        passwordError.value = item.error;
      }
    });
    console.log(response);
  } else {
    await router.push("/");
  }
};

const onSubmitPressed = (e: Event) => {
  e.preventDefault();
  error.value = false;
  emailError.value = "";
  passwordError.value = "";
  if (isSignIn.value) {
    signIn(e);
  } else {
    signUp(e);
  }
};

const onGithubPressed = async () => {
  const authUrl = await ThirdPartyEmailPassword.getAuthorisationURLWithQueryParamsAndSetState(
    {
      providerId: "github",
      authorisationURL: `${WEBSITE_DOMAIN}/auth/callback/github`,
    }
  );
  window.location.assign(authUrl);
};

const onGooglePressed = async () => {
  const authUrl = await ThirdPartyEmailPassword.getAuthorisationURLWithQueryParamsAndSetState(
    {
      providerId: "google",
      authorisationURL: `${WEBSITE_DOMAIN}/auth/callback/google`,
    }
  );
  window.location.assign(authUrl);
};

const onFacebookPressed = async () => {
  const authUrl = await ThirdPartyEmailPassword.getAuthorisationURLWithQueryParamsAndSetState(
    {
      providerId: "facebook",
      authorisationURL: `${WEBSITE_DOMAIN}/auth/callback/facebook`,
    }
  );
  window.location.assign(authUrl);
};

const checkForSession = async () => {
  if (await Session.doesSessionExist()) {
    console.log("session exist");
    window.location.assign("/");
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
          <div class="px-8 py-6">
            <div class="w-full mt-0 text-center text-md">
              <span v-if="isSignIn">
                Not yet registered?
                <span class="hover:underline hover:cursor-pointer" @click="goToSignUp">
                  Sign Up
                </span>
              </span>
              <span v-else>
                Already have an account?
                <span class="hover:underline hover:cursor-pointer" @click="goToSignIn">
                  Sign In
                </span>
              </span>
            </div>

            <div v-if="error" class="w-full text-red-400">
              <p>
                {{ errorMessage }}
              </p>
            </div>

            <button
              type="submit"
              class="mt-6 bg-blue-500 text-white py-2 px-6 w-full rounded-md hover:bg-blue-600"
              @click="onFacebookPressed"
            >
              Login with Facebook
            </button>

            <button
              type="submit"
              class="mt-4 bg-red-500 text-white py-2 px-6 w-full rounded-md hover:bg-red-600"
              @click="onGooglePressed"
            >
              Login with Google
            </button>

            <button
              type="submit"
              class="mt-4 bg-gray-700 text-white py-2 px-6 w-full rounded-md hover:bg-gray-900"
              @click="onGithubPressed"
            >
              Login with Github
            </button>

            <label class="block font-semibold mt-10" for="username">
              Username or Email:
            </label>
            <input
              class="border w-full h-5 px-3 py-5 mt-2 hover:outline-none focus:outline-none focus:ring-1 focus:ring-green-400 rounded-md"
              type="text"
              name="username"
              placeholder="Username or Email"
            />

            <label class="block mt-5 font-semibold" for="password"> Password: </label>
            <input
              class="border w-full h-5 px-3 py-5 mt-2 hover:outline-none focus:outline-none focus:ring-1 focus:ring-green-400 rounded-md"
              type="password"
              name="password"
              placeholder="Password"
            />

            <button
              type="submit"
              class="mt-4 bg-green-500 text-white py-2 px-6 w-full rounded-md hover:bg-green-600"
              @click="onSubmitPressed"
            >
              {{ isSignIn ? "Login" : "Create an Account" }}
            </button>
            <div class="w-full mt-4 items-center text-center">
              <div v-if="isSignIn">
                <router-link :to="{ path: `/auth/reset-password` }">
                  Forgot Password?
                </router-link>
              </div>
            </div>
          </div>
        </div>
      </div>
    </div>
  </main>
</template>

<style scoped></style>
