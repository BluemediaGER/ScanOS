<script setup lang="ts">
import Logo from './icons/Logo.vue';
import SettingsGear from './icons/SettingsGear.vue';
import PowerButton from './icons/PowerButton.vue';
import { RouterLink } from 'vue-router';
</script>
<template>
    <div class="w-full h-28 p-4 flex-shrink-0">
        <div class="w-full h-full pl-6 pr-6 rounded-lg shadow-lg bg-white flex flex-row justify-center items-center gap-5">
            <RouterLink to="/" class="h-full w-auto pt-4 pb-4 flex-none">
                <Logo class="h-full w-auto flex-none text-gray-600" />
            </RouterLink>
            <span class="h-full grow"></span>
            <RouterLink to="/settings" class="h-full w-auto pt-5 pb-5 flex-none">
                <SettingsGear class="h-full w-auto text-gray-600" />
            </RouterLink>
            <RouterLink to="/power" class="h-full w-auto pt-5 pb-5 flex-none">
                <PowerButton class="h-full w-auto text-gray-600" />
            </RouterLink>
        </div>
    </div>
</template>