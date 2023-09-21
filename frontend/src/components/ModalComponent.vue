<template>
<div class="fixed inset-0 bg-black bg-opacity-30 flex justify-center items-center">
    <div class="bg-white rounded-lg shadow-lg flex">
        <slot></slot>
    </div>
</div>
</template>
<script lang="ts">
  export default {
    name: 'ModalComponent'
  };
</script>
