import { getUserInfo, setToken, setUserInfo } from './auth'
import { ref } from 'vue'

//仅供页面的setup函数使用
const userInfo = ref(getUserInfo())

export function useUser() {
  function saveLoginData(data) {
    setToken(data.token)
    setUserInfo(data.user)
    userInfo.value = data.user
  }

  function updataUser(user) {
    setUserInfo(user)
    userInfo.value = user
  }

  function reloadUser() {
    userInfo.value = getUserInfo()
  }

  return {
    userInfo,
    saveLoginData,
    updataUser,
    reloadUser
  }
}
