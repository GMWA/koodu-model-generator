<script setup lang="ts">
	import ThirdPartyEmailPassword from "supertokens-web-js/recipe/thirdpartyemailpassword";
	import { ref, Ref } from "vue";

	const tokenPresent = ref(false);
	const error = ref(false);
	const didSubmit = ref(false);
	const errorMessage = ref("");
	const email = ref("");
	const password = ref("")

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
          throw new Error("Password reset token has expired, please go back to the sign in page");
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
  }
</script>

<template>
	<div class="fill">
    <div class="form-container">
      <div v-if="tokenPresent" class="form-content-container">
        <div v-if="error" class="top-error-container">
          <div class="error-message">{{ errorMessage }}</div>
        </div>
        <div v-if="!didSubmit">
          <div class="form-text-header">Enter new password</div>
          <div class="form-subtitle">Please enter your new password below</div>

          <div class="input-section-container">
            <div class="input-label">New Password</div>
            <div class="input-container">
              <div class="input-wrapper">
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
          </div>

          <div class="button-container">
            <button @click="onSubmitClicked" class="form-button">Change Password</button>
          </div>
        </div>
      </div>
      <div v-else class="form-content-container">
        <div v-if="error" class="top-error-container">
          <div class="error-message">{{ errorMessage }}</div>
      	</div>
        <div v-if="!didSubmit">
          <div class="form-text-header">Reset your password</div>
          <div class="form-subtitle">We will send you an email to reset your password</div>

          <div class="input-section-container">
            <div class="input-label">Email</div>
            <div class="input-container">
              <div class="input-wrapper">
                <input autocomplete="email" class="input" type="email" name="email" v-model="email" />
              </div>
            </div>
          </div>

          <div class="button-container">
            <button @click="onSubmitClicked" class="form-button">Email Me</button>
          </div>
        </div>
        <div v-else>
          <div class="confirmation">
            Please check your email for the password recovery link
            <span class="resend-button" @click="onSubmitClicked">Resend</span>
          </div>
        </div>
      </div>
    </div>
	</div>
</template>

<style scoped>

</style>