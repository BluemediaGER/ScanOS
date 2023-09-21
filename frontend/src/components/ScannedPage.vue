<script setup lang="ts">
import { ref } from 'vue';
import LoadingSpinner from '@/components/LoadingSpinner.vue';

const props = defineProps({
    imgUrl: String
})

const imgLoaded = ref(false)
</script>
<template>
    <div class="p-2">
        <div class="w-full h-full rounded-lg shadow-lg bg-white flex justify-center items-center">
            <LoadingSpinner v-if="!imgLoaded" class="w-10 h-10 text-gray-600" />
            <img v-if="imgUrl" v-show="imgLoaded" :src="imgUrl" @load="imgLoaded=true" class="w-full h-full rounded-lg object-cover">
        </div>
    </div>
</template>