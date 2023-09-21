<script setup lang="ts">
import ShadowCard from '@/components/ShadowCard.vue';
import PaperlessLogo from '@/components/icons/PaperlessLogo.vue'
import EnvelopeAt from '@/components/icons/EnvelopeAt.vue';
import FolderSymlink from '@/components/icons/FolderSymlink.vue';
</script>

<template>
  <div class="w-full h-full pt-10 pb-10 pl-4 pr-4 flex flex-shrink-0 flex-row justify-between items-center gap-5 text-gray-700">
    <RouterLink to="/scan?backend=paperless" class="h-2/3 max-w-xs">
      <ShadowCard class="h-full w-full">
        <div class="h-full w-full p-5 flex flex-col justify-center items-center">
          <div class="h-full w-full flex flex-col justify-center items-center gap-4">
            <PaperlessLogo class="h-16 w-auto" />
            <h1 class="text-xl select-none">Paperless-ngx</h1>
          </div>
          <div class="h-full w-full flex justify-center items-start">
            <p class="text-lg select-none">Scan your documents right into Paperless-ngx. You can also customize correspondent, document type and tags.</p>
          </div>
        </div>
      </ShadowCard>
    </RouterLink>
    <RouterLink to="/scan?backend=mail" class="h-2/3 max-w-xs">
      <ShadowCard class="h-full w-full">
        <div class="h-full w-full p-5 flex flex-col justify-center items-center">
          <div class="h-full w-full flex flex-col justify-center items-center gap-4">
            <EnvelopeAt class="h-16 w-auto" />
            <h1 class="text-xl select-none">Scan2Mail</h1>
          </div>
          <div class="h-full w-full flex justify-center items-start">
            <p class="text-lg select-none">Scan your documents and send them as a PDF file attachment via email.</p>
          </div>
        </div>
      </ShadowCard>
    </RouterLink>
    <RouterLink to="/scan?backend=storage-share" class="h-2/3 max-w-xs">
      <ShadowCard class="h-full w-full">
        <div class="h-full w-full p-5 flex flex-col justify-center items-center">
          <div class="h-full w-full flex flex-col justify-center items-center gap-4">
            <FolderSymlink class="h-16 w-auto" />
            <h1 class="text-xl select-none">Network Share</h1>
          </div>
          <div class="h-full w-full flex justify-center items-start">
            <p class="text-lg select-none">Scan your documents and save them as PDF files to a network storage share.</p>
          </div>
        </div>
      </ShadowCard>
    </RouterLink>
  </div>
</template>
