<template>
  <div class="slidev-layout center-dark h-full grid place-content-center">
    <div class="my-auto">
      <slot />
    </div>
  </div>
</template>

<style scoped>
/* Тёмная закрывающая плитка (surface-dark) — аналог footer, full-bleed,
   + приглушённые Stripe-style glow-пятна в углах (indigo / pink / blue) */
.slidev-layout.center-dark {
  position: absolute;
  inset: 0;
  padding: 0;
  background: var(--slide-dark-mesh), var(--surface-dark);
  color: var(--on-dark);
}
</style>
