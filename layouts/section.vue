<template>
  <div class="slidev-layout section-band h-full grid place-content-center">
    <div class="my-auto">
      <slot />
    </div>
  </div>
</template>

<style scoped>
/* Секционный разделитель — очень мягкая плитка (surface-soft) + Stripe-style top-mesh,
   full-bleed. Класс не "section", чтобы не цеплять h1-правила темы. */
.slidev-layout.section-band {
  position: absolute;
  inset: 0;
  padding: 0;
  background: var(--slide-top-mesh), var(--surface-soft);
}
</style>
