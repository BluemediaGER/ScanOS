<script setup lang="ts">
import { RouterView } from 'vue-router'
import TopBar from './components/TopBar.vue'
</script>

<template>
  <div class="w-full h-full bg-gray-100 flex flex-col">
    <TopBar />
    <div class="w-full h-full flex flex-row">
      <RouterView v-slot="{ Component, route}">
        <!--<Transition>-->
          <component :is="Component" :key="route.path" />
        <!--</Transition-->
      </RouterView>
    </div>
  </div>
</template>

<style scoped>
@keyframes slidein {
  0% {
    transform: translateX(-200vh);
  }
  100% {
    transform: translateX(0);
  }
}
@keyframes slideout {
  0% {
    transform: translateX(0);
  }
  100% {
    transform: translateX(+200vh);
  }
}
.v-enter-from {
  transform: translateX(-200vh);
}
.v-enter-active {
  animation: slidein 0.3s ease-in-out;
}
.v-leave-from {
  transform: translateX(0);
}
.v-leave-active {
  animation: slideout 0.3s ease-in-out;
}

.v-leave-to {
  transform: translateX(+200vh);
}
</style>