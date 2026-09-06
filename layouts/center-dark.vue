<template>
  <div class="slidev-layout center-dark h-full grid place-content-center">
    <div class="my-auto">
      <slot />
    </div>
  </div>
</template>

<style scoped>
/* Тёмная закрывающая плитка (surface-dark) — аналог footer, full-bleed */
.slidev-layout.center-dark {
  position: absolute;
  inset: 0;
  padding: 0;
  background: var(--surface-dark);
  color: var(--on-dark);
}
</style>
