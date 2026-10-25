//存储token、用户信息；获取token、用户信息；删除token
const TOKEN_KEY = 'token'
const USER_KEY = 'userInfo'

export function getToken() {
  return localStorage.getItem(TOKEN_KEY)
}

export function setToken(token) {
  return localStorage.setItem(TOKEN_KEY, token)
}

export function removeToken() {
  return localStorage.removeItem(TOKEN_KEY)
}

export function getUserInfo() {
  const str = localStorage.getItem(USER_KEY)
  if (!str) return null
  try {
    return JSON.parse(str)
  } catch {
    return null
  }
}

export function setUserInfo(userInfo) {
  return localStorage.setItem(USER_KEY, JSON.stringify(userInfo))
}

export function removeUserInfo() {
  return localStorage.removeItem(USER_KEY)
}

export function logout() {
  removeToken()
  removeUserInfo()
}
