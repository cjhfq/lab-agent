<template>
  <div class="common-layout">
    <el-container style="min-height: 100vh">
      <el-header
        style="
          display: flex;
          align-items: center;
          border-bottom: 1px solid #ddd;
          background-color: #fff;
        "
      >
        <div
          style="flex: 1; display: flex; align-items: center; font-size: 24px; font-weight: bold"
        >
          <img src="@/assets/imgs/logo.png" style="width: 40px; margin-right: 5px" alt="Logo" />
          <div>智能实验室预约系统</div>
        </div>
        <div>
          <el-dropdown>
            <div style="display: flex; align-items: center; cursor: pointer">
              <img src="@/assets/imgs/logo.png" style="width: 30px; border-radius: 50%" />
              <div style="margin-left: 3px">管理员</div>
            </div>
            <template #dropdown>
              <el-dropdown-menu>
                <el-dropdown-item @click="handleLogout">退出登录</el-dropdown-item>
              </el-dropdown-menu>
            </template>
          </el-dropdown>
        </div>
      </el-header>
      <el-container>
        <el-aside width="220px">
          <el-menu router style="height: 100%" default-active="/manager/home">
            <el-menu-item index="/manager/home">
              <el-icon><icon-menu /></el-icon>
              <span>系统首页</span>
            </el-menu-item>
            <el-menu-item index="/manager/lab">
              <el-icon><House /></el-icon>
              <span>实验室管理</span>
            </el-menu-item>
            <el-menu-item index="/manager/equ">
              <el-icon><Setting /></el-icon>
              <span>设备管理</span>
            </el-menu-item>
            <el-menu-item index="/manager/user">
              <el-icon><User /></el-icon>
              <span>用户管理</span>
            </el-menu-item>
          </el-menu>
        </el-aside>
        <el-main>
          <router-view />
        </el-main>
      </el-container>
    </el-container>
  </div>
</template>
<script setup>
import router from '@/router'
import { logout } from '@/utils/auth'
import { Setting, Menu as IconMenu, House, User } from '@element-plus/icons-vue'

const handleLogout = () => {
  logout()
  router.push('/login')
}
</script>
