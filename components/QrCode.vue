<script setup lang="ts">
import { computed } from 'vue'
import qrcode from 'qrcode-generator'

const props = defineProps({
  url: { type: String, required: true },
  size: { type: Number, default: 120 },
  caption: { type: String, default: '' },
})

const qrDataUrl = computed(() => {
  const qr = qrcode(0, 'M')
  qr.addData(props.url)
  qr.make()
  return qr.createDataURL(4, 4)
})
</script>

<template>
  <div class="qr">
    <img :src="qrDataUrl" :width="size" :height="size" class="qr-img" />
    <div v-if="caption" class="qr-caption">{{ caption }}</div>
  </div>
</template>

<style scoped>
.qr {
  display: inline-flex;
  flex-direction: column;
  align-items: center;
  gap: 0.5rem;
}
.qr-img {
  border-radius: 8px;
}
.qr-caption {
  font-family: 'Geist Mono', monospace;
  font-size: 0.85rem;
  color: var(--ink-dim);
}
</style>
