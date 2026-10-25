import request from '@/utils/request'

/**
 * 登录请求
 */
export function loginAPI(data) {
  return request({
    url: '/api/auth/login',
    method: 'post',
    data
  })
}
