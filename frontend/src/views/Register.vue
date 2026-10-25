<template>
  <div class="register-container">
    <div class="register-box">
      <h1 style="font-size: 28px; margin-bottom: 30px">欢迎注册实验室预约系统</h1>
      <el-form :model="form" label-width="auto" style="max-width: 600px">
        <el-form-item>
          <el-input
            size="large"
            v-model="form.username"
            placeholder="请输入用户名"
            :prefix-icon="User"
          />
        </el-form-item>
        <el-form-item>
          <el-input
            size="large"
            v-model="form.password"
            placeholder="请输入密码"
            :prefix-icon="Lock"
            show-password
          />
        </el-form-item>
        <el-form-item>
          <el-input
            size="large"
            v-model="form.comfirmPassword"
            placeholder="请确认密码"
            :prefix-icon="Lock"
            show-password
          />
        </el-form-item>
        <el-button size="large" type="primary" style="width: 100%">注册</el-button>
        <div style="text-align: right; margin-top: 10px">
          已有账号？请<a style="color: var(--el-color-primary)" href="/login">登录</a>
        </div>
      </el-form>
    </div>
  </div>
</template>
<script setup>
import { reactive } from 'vue'
import { User, Lock } from '@element-plus/icons-vue'
const form = reactive({
  username: '',
  password: '',
  comfirmPassword: ''
})
</script>
<style scoped>
.register-container {
  display: flex;
  justify-content: center;
  align-items: center;
  height: 100vh;
}

.register-box {
  width: 380px;
  border-radius: 8px;
  box-shadow: 0 8px 12px rgba(0, 0, 0, 0.1);
  padding: 30px;
  text-align: center;
  background-color: #fff;
}
</style>
