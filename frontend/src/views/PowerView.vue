<script setup lang="ts">
import ShadowCard from '@/components/ShadowCard.vue';
import PowerButton from '@/components/icons/PowerButton.vue';
import ArrowClockwise from '@/components/icons/ArrowClockwise.vue';
import ModalComponent from '@/components/ModalComponent.vue';
import axios from 'axios';
import {ref} from 'vue';

const showModal = ref(false);
const action = ref("");
</script>

<template>
<div class="w-full h-full pt-10 pb-10 pl-4 pr-4 flex flex-shrink-0 flex-row justify-center items-center gap-20 text-gray-700">
    <ShadowCard @click="action='shutdown';showModal=true" class="h-1/3 w-1/5">
        <div class="w-full h-full flex flex-col justify-center items-center">
            <PowerButton class="w-12 h-12 text-red-700" />
            <h1 class="mt-5 text-xl font-semibold">Shutdown</h1>
        </div>
    </ShadowCard>
    <ShadowCard @click="action='restart';showModal=true" class="h-1/3 w-1/5">
        <div class="w-full h-full flex flex-col justify-center items-center">
            <ArrowClockwise class="w-12 h-12 text-orange-400" />
            <h1 class="mt-5 text-xl font-semibold">Restart</h1>
        </div>
    </ShadowCard>
    <ModalComponent v-if="showModal">
        <div class="flex flex-col p-10">
            <h1 class="font-semibold text-lg mb-5">Do you really want to {{ action }}?</h1>
            <div class="flex flex-row justify-between items-center">
                <button @click="confirm(action)" class="h-12 w-20 rounded-md bg-green-500 text-white font-semibold">Yes</button>
                <button @click="showModal=false" class="h-12 w-20 rounded-md bg-red-500 text-white font-semibold">No</button>
            </div>
        </div>
    </ModalComponent>
</div>
</template>

<script lang="ts">
function confirm(action: String) {
    if (action == "shutdown") {
        axios.post('/api/power/shutdown', {});
    } else {
        axios.post('/api/power/restart', {});
    }
}
</script>