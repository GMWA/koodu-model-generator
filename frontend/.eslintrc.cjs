/* eslint-env node */
require("@rushstack/eslint-patch/modern-module-resolution")

module.exports = {
  root: true,
  parser: "vue-eslint-parser",
  parserOptions: {
    parser: "@typescript-eslint/parser",
  },
  extends: [
    //"plugin:vue/strongly-recommended",
    "eslint:recommended",
    "@vue/typescript/recommended",
    "plugin:vue/recommended"
  ],
  plugins: ["@typescript-eslint", "prettier"],
  rules: {
    "prettier/prettier": "error",
    // not needed for vue 3
    'no-unused-vars': 'off',
    '@typescript-eslint/no-unused-vars': ['error', { 'varsIgnorePattern': '^_', "argsIgnorePattern": "^_" }],
  },
}