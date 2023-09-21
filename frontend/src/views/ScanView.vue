<script setup lang="ts">
import ScannedPage from '@/components/ScannedPage.vue';
import { useRoute } from 'vue-router'
import { ref } from 'vue';
import axios from 'axios';

const route = useRoute()
let backend = route.query.backend;

const data = ref({
    pages: new Array<any>(),
    status: "idle"
})

function getUpdate() {
    axios.get('/api/scan/status')
        .then(function (response) {
            data.value = response.data
            if (response.data.status === "running") {
                setTimeout(getUpdate, 1000)
            }
        })
        .catch(function (error) {
            // handle error
            console.log(error);
    })
}
axios.post('/api/scan')
    .then(function (response) {
        data.value.status = "running"
        setTimeout(getUpdate, 2000)
    })
</script>
<template>
    <dev class="w-full h-full flex flex-col">
        <div class="w-full h-full p-2 flex flex-row flex-wrap overflow-auto">
            <ScannedPage v-for="page in data.pages" :key="page.filename" class="w-1/5 h-1/2" :imgUrl="'/img/' + page.filename" />
            <ScannedPage v-if="data.status==='running'" class="w-1/5 h-1/2" />
        </div>
        <div class="w-full h-28 p-4 flex">

        </div>
    </dev>
</template>