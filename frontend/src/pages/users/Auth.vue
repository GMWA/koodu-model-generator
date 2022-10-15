<script setup lang="ts">
	import ThirdPartyEmailPassword from "supertokens-web-js/recipe/thirdpartyemailpassword";
	import Session from "supertokens-web-js/recipe/session";
	import { ref, Ref, onMounted } from "vue";
	import { WEBSITE_DOMAIN } from "../../configs";


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
			return;
		}
		window.location.assign("/");
	}

	const validateEmail = (email: string) => {
		return email
			.toLowerCase()
			.match(
				/^(([^<>()[\]\\.,;:\s@"]+(\.[^<>()[\]\\.,;:\s@"]+)*)|(".+"))@((\[[0-9]{1,3}\.[0-9]{1,3}\.[0-9]{1,3}\.[0-9]{1,3}\])|(([a-zA-Z\-0-9]+\.)+[a-zA-Z]{2,}))$/
		);
	}

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
			return;
		}
	  window.location.assign("/");
	}

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
	}

	const onGithubPressed = async () => {
		const authUrl = await ThirdPartyEmailPassword.getAuthorisationURLWithQueryParamsAndSetState({
			providerId: "github",
			authorisationURL: `${WEBSITE_DOMAIN}/auth/callback/github`,
		});
		window.location.assign(authUrl);
	}

	const onGooglePressed = async () => {
		const authUrl = await ThirdPartyEmailPassword.getAuthorisationURLWithQueryParamsAndSetState({
			providerId: "google",
			authorisationURL: `${WEBSITE_DOMAIN}/auth/callback/google`,
		});
		window.location.assign(authUrl);
	}

	const onFacebookPressed = async () => {
		const authUrl = await ThirdPartyEmailPassword.getAuthorisationURLWithQueryParamsAndSetState({
			providerId: "facebook",
			authorisationURL: `${WEBSITE_DOMAIN}/auth/callback/facebook`,
		});
		window.location.assign(authUrl);
	}

	const checkForSession =  async () => {
		if (await Session.doesSessionExist()) {
			window.location.assign("/");
		}
	}
</script>

<template>
	<div class="auth-container">
    <div class="auth-form-container">
    	<div v-if="error" class="error-container">
        <div class="error-message">{{ errorMessage }}</div>
      </div>
      <div class="auth-form-content-container">
        <div class="form-title" v-if="isSignIn">Sign In</div>
        <div class="form-title" v-else>Sign Up</div>
        <div class="sign-in-up-text-container">
          <span v-if="isSignIn"
            >Not yet registered? <span class="clickable-text" @click="goToSignUp">Sign Up</span></span
          >
          <span v-else
            >Already have an account? <span class="clickable-text" @click="goToSignIn">Sign In</span></span
          >
        </div>
        <div class="divider-container">
          <div class="divider" />
        </div>
        <div class="providerContainer">
          <span>
            <button class="providerButton providerGithub" @click="onGithubPressed">
              <div class="providerButtonLeft">
                <div class="providerButtonLogo">
                  <div class="providerButtonLogoCenter">
                    <svg
                      xmlns="http://www.w3.org/2000/svg"
                      width="18"
                      height="17.556"
                      viewBox="0 0 18 17.556"
                    >
                      <path
                        fill="#fff"
                        fill-rule="evenodd"
                        d="M145.319 107.44a9 9 0 0 0-2.844 17.54c.45.082.614-.2.614-.434 0-.214-.008-.78-.012-1.531-2.5.544-3.032-1.206-3.032-1.206a2.384 2.384 0 0 0-1-1.317c-.817-.559.062-.547.062-.547a1.89 1.89 0 0 1 1.378.927 1.916 1.916 0 0 0 2.619.748 1.924 1.924 0 0 1 .571-1.2c-2-.227-4.1-1-4.1-4.448a3.479 3.479 0 0 1 .927-2.415 3.233 3.233 0 0 1 .088-2.382s.755-.242 2.475.923a8.535 8.535 0 0 1 4.506 0c1.718-1.165 2.472-.923 2.472-.923a3.234 3.234 0 0 1 .09 2.382 3.473 3.473 0 0 1 .925 2.415c0 3.458-2.1 4.218-4.11 4.441a2.149 2.149 0 0 1 .611 1.667c0 1.2-.011 2.174-.011 2.469 0 .24.162.52.619.433a9 9 0 0 0-2.851-17.539z"
                        transform="translate(-136.32 -107.44)"
                      ></path>
                    </svg>
                	</div>
                </div>
              </div>
              <div class="providerButtonText">Continue with Github</div>
            </button>
          </span>
        </div>

        <div class="providerContainer">
          <span>
            <button class="providerButton providerGoogle" @click="onGooglePressed">
              <div class="providerButtonLeft">
                <div class="providerButtonLogo">
                  <div class="providerButtonLogoCenter">
                    <svg
                      xmlns="http://www.w3.org/2000/svg"
                      width="18.001"
                      height="18"
                      viewBox="0 0 18.001 18"
                    >
                      <g id="Group_9292" transform="translate(-534 -389)">
                        <path
                          id="Path_85803"
                          d="M3.989 144.285l-.627 2.339-2.29.048a9.016 9.016 0 0 1-.066-8.4l2.039.374.893 2.027a5.371 5.371 0 0 0 .05 3.616z"
                          transform="translate(534 255.593)"
                          style="fill: rgb(255, 255, 255)"
                        ></path>
                        <path
                          id="Path_85804"
                          d="M270.273 208.176a9 9 0 0 1-3.208 8.7l-2.568-.131-.363-2.269a5.364 5.364 0 0 0 2.308-2.739h-4.813v-3.56h8.645z"
                          transform="translate(281.57 188.143)"
                          style="fill: rgb(255, 255, 255)"
                        ></path>
                        <path
                          id="Path_85805"
                          d="M44.07 314.549a9 9 0 0 1-13.561-2.749l2.917-2.387a5.353 5.353 0 0 0 7.713 2.741z"
                          transform="translate(504.564 90.469)"
                          style="fill: rgb(255, 255, 255)"
                        ></path>
                        <path
                          id="Path_85806"
                          d="M42.362 2.072l-2.915 2.387a5.352 5.352 0 0 0-7.89 2.8l-2.932-2.4a9 9 0 0 1 13.737-2.787z"
                          transform="translate(506.383 389)"
                          style="fill: rgb(255, 255, 255)"
                        ></path>
                      </g>
                  	</svg>
                	</div>
              	</div>
          	</div>
          	<div class="providerButtonText">Continue with Google</div>
      		</button>
  			</span>
    	</div>

      <div class="providerContainer">
        <span>
        	<button class="providerButton providerApple" @click="onFacebookPressed">
            <div class="providerButtonLeft">
              <div class="providerButtonLogo">
                <div class="providerButtonLogoCenter">
                  <svg
                    xmlns="http://www.w3.org/2000/svg"
                    width="18.001"
                    height="18"
                    viewBox="0 0 18.001 18"
                  >
                    <path
                      fill="none"
                      d="M0 0h24v24H0z"
                    />
                    <path
                      fill="#fff"
                      d="M12 2C6.477 2 2 6.477 2 12c0 4.991 3.657 9.128 8.438 9.879V14.89h-2.54V12h2.54V9.797c0-2.506 1.492-3.89 3.777-3.89 1.094 0 2.238.195 2.238.195v2.46h-1.26c-1.243 0-1.63.771-1.63 1.562V12h2.773l-.443 2.89h-2.33v6.989C18.343 21.129 22 16.99 22 12c0-5.523-4.477-10-10-10z"
                    />
                  </svg>
                </div>
              </div>
            </div>
            <div class="providerButtonText">Continue with Facebook</div>
          </button>
        </span>
      </div>

      <div class="divider-container">
        <div class="divider" />
        <div class="divider-text">or</div>
        <div class="divider" />
      </div>

      <form @submit="onSubmitPressed" autocomplete="on" novalidate>
        <div class="input-section-container" v-bind:class="emailError ? 'error' : ''">
          <div class="input-label">Email</div>
          <div class="input-container">
            <div class="input-wrapper" v-bind:class="emailError ? 'error' : ''">
              <input
                autocomplete="email"
                class="input"
                type="email"
                name="email"
                placeholder="Email address"
                v-model="email"
              />
            </div>
          </div>
          <div v-if="emailError" class="input-error">{{ `${emailError}` }}</div>
        </div>

        <div class="input-section-container" v-bind:class="passwordError ? 'error' : ''">
        	<div class="input-label">Password</div>
            <div class="input-container">
              <div class="input-wrapper" v-bind:class="passwordError ? 'error' : ''">
                <input
                  autocomplete="current-password"
                  class="input"
                  type="password"
                  name="password"
                  placeholder="Password"
                  v-model="password"
              	/>
            	</div>
        		</div>
        	<div v-if="passwordError" class="input-error">{{ `${passwordError}` }}</div>
        </div>

        <div class="input-section-container">
          <div v-if="isSignIn">
            <button type="submit" class="button">SIGN IN</button>
          </div>
          <div v-else>
            <button type="submit" class="button">SIGN UP</button>
          </div>
        </div>
      </form>
      </div>
      <div v-if="isSignIn">
        <router-link :to="{ path: `/auth/reset-password` }"> Forgot Password? </router-link>
      </div>
      <div style="margin-bottom: 10px" />
    </div>
	</div>
</template>

<style scoped>

</style>