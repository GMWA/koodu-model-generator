export const AuthEndpoint = {
  LOGIN: '/users/login',
  REGISTER: '/users/register',
  ME: '/users/me',
  REFRESH: '/users/refresh-token',
  LOGOUT: '/users/logout',
  ACTIVATE: '/users/activate',
  ACTIVATE_LINK: '/users/activate-link',
  FORGOT_PASSWORD: '/users/forgot-password',
  RESET_PASSWORD: '/users/reset-password',
  ACTIVATE_ACCOUNT: '/users/activate',
  ACTIVATE_ACCOUNT_LINK: '/users/activate-link',
  VERIFY_TOKEN: '/users/verify-token',
}

export const ProjectEndpoint = {
  CREATE: '/projects',
  GET_ALL: '/projects',
  GET_ONE: '/projects',
  UPDATE: '/projects',
  DELETE: '/projects',
}

export const TableEndpoint = {
  CREATE: '/tables',
  GET_ALL: '/tables',
  GET_ONE: '/tables',
  UPDATE: '/tables',
  DELETE: '/tables',
}

export const AttributEndpoint = {
  CREATE: '/attributs',
  GET_ALL: '/attributs',
  GET_ONE: '/attributs',
  UPDATE: '/attributs',
  DELETE: '/attributs',
}
