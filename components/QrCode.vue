<script setup lang="ts">
import { computed } from 'vue'
import qrcode from 'qrcode-generator'

const props = defineProps({
  url: { type: String, required: true },
  size: { type: Number, default: 120 },
  caption: { type: String, default: '' },
  icon: { type: String, default: '' },
})

const qrDataUrl = computed(() => {
  const qr = qrcode(0, 'H')
  qr.addData(props.url)
  qr.make()
  return qr.createDataURL(4, 4)
})

const iconBoxSize = computed(() => Math.round(props.size * 0.28))
</script>

<template>
  <a :href="url" target="_blank" rel="noopener noreferrer" class="qr">
    <span class="qr-img-wrap">
      <img :src="qrDataUrl" :width="size" :height="size" class="qr-img" />
      <span v-if="icon" class="qr-icon" :style="{ width: iconBoxSize + 'px', height: iconBoxSize + 'px' }">
        <svg v-if="icon === 'slides'" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round">
          <path d="M2 3h20" />
          <path d="M21 3v11a2 2 0 0 1-2 2H5a2 2 0 0 1-2-2V3" />
          <path d="m7 21 5-5 5 5" />
        </svg>
        <svg v-else-if="icon === 'wrench'" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round">
          <path d="M14.7 6.3a1 1 0 0 0 0 1.4l1.6 1.6a1 1 0 0 0 1.4 0l3.77-3.77a6 6 0 0 1-7.94 7.94l-6.91 6.91a2.12 2.12 0 0 1-3-3l6.91-6.91a6 6 0 0 1 7.94-7.94l-3.76 3.76z" />
        </svg>
      </span>
    </span>
    <div v-if="caption" class="qr-caption">{{ caption }}</div>
  </a>
</template>

<style scoped>
.qr {
  display: inline-flex;
  flex-direction: column;
  align-items: center;
  gap: 0.5rem;
  text-decoration: none;
  cursor: pointer;
}
.qr-img-wrap {
  position: relative;
  display: inline-block;
  background: #fff;
  border-radius: 12px;
  padding: 0.45rem;
  transition: box-shadow 0.2s ease;
}
.qr:hover .qr-img-wrap {
  box-shadow: 0 0 0 2px var(--accent);
}
.qr-img {
  display: block;
}
.qr-icon {
  position: absolute;
  top: 50%;
  left: 50%;
  transform: translate(-50%, -50%);
  display: flex;
  align-items: center;
  justify-content: center;
  background: #fff;
  border-radius: 22%;
  box-shadow: 0 0 0 4px #fff;
  color: #18181b;
}
.qr-icon svg {
  width: 60%;
  height: 60%;
}
.qr-caption {
  font-family: var(--font-mono);
  font-size: 0.85rem;
  color: var(--muted-soft);
}
</style>
