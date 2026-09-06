<script setup lang="ts">
withDefaults(
  defineProps<{
    code: string
    size?: number
  }>(),
  {
    size: 20,
  },
)
</script>

<template>
  <svg
    class="flag"
    :width="size"
    :height="size * (2 / 3)"
    viewBox="0 0 24 16"
    aria-hidden="true"
    focusable="false"
  >
    <!-- United States -->
    <g v-if="code === 'us'">
      <rect width="24" height="16" fill="#ffffff" />
      <rect y="0" width="24" height="2.29" fill="#b22234" />
      <rect y="4.57" width="24" height="2.29" fill="#b22234" />
      <rect y="9.14" width="24" height="2.29" fill="#b22234" />
      <rect y="13.71" width="24" height="2.29" fill="#b22234" />
      <rect width="10" height="8" fill="#3c3b6e" />
    </g>
    <!-- European Union -->
    <g v-else-if="code === 'eu'">
      <rect width="24" height="16" fill="#003399" />
      <g fill="#ffcc00">
        <circle cx="16.5" cy="8" r="0.9" />
        <circle cx="15.18" cy="11.18" r="0.9" />
        <circle cx="12" cy="12.5" r="0.9" />
        <circle cx="8.82" cy="11.18" r="0.9" />
        <circle cx="7.5" cy="8" r="0.9" />
        <circle cx="8.82" cy="4.82" r="0.9" />
        <circle cx="12" cy="3.5" r="0.9" />
        <circle cx="15.18" cy="4.82" r="0.9" />
      </g>
    </g>
    <!-- Russia -->
    <g v-else-if="code === 'ru'">
      <rect width="24" height="16" fill="#ffffff" />
      <rect y="5.33" width="24" height="5.34" fill="#0039a6" />
      <rect y="10.67" width="24" height="5.33" fill="#d52b1e" />
    </g>
    <!-- China -->
    <g v-else-if="code === 'cn'">
      <rect width="24" height="16" fill="#de2910" />
      <polygon
        fill="#ffde00"
        points="5,1.9 5.588,3.691 7.473,3.697 5.951,4.809 6.528,6.603 5,5.5 3.472,6.603 4.049,4.809 2.527,3.697 4.412,3.691"
      />
    </g>
    <!-- India -->
    <g v-else-if="code === 'in'">
      <rect width="24" height="5.33" fill="#ff9933" />
      <rect y="5.33" width="24" height="5.34" fill="#ffffff" />
      <rect y="10.67" width="24" height="5.33" fill="#138808" />
      <circle cx="12" cy="8" r="2.1" fill="none" stroke="#000080" stroke-width="0.7" />
      <circle cx="12" cy="8" r="0.5" fill="#000080" />
    </g>
    <!-- Japan -->
    <g v-else-if="code === 'jp'">
      <rect width="24" height="16" fill="#ffffff" />
      <circle cx="12" cy="8" r="5" fill="#bc002d" />
    </g>
    <!-- Indonesia -->
    <g v-else-if="code === 'id'">
      <rect width="24" height="16" fill="#ffffff" />
      <rect width="24" height="8" fill="#ce1126" />
    </g>
    <!-- Fallback -->
    <g v-else>
      <rect width="24" height="16" fill="#e5e7eb" />
    </g>
  </svg>
</template>

<style scoped>
.flag {
  display: block;
  border-radius: 3px;
}
</style>
