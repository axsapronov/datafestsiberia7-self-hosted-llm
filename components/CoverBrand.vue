<script setup lang="ts">
// Брендинг обложки: логотипы конференции лежат в public/img/.
// Если файла нет, картинка 404-ит и скрывает себя — блок не падает
// на отсутствующих ассетах, обложка деградирует до чистой текстовой.
// Имена файлов — по факту в public/img/; при замене ассетов поправить здесь.
const logos = [
  { src: '/img/df7-logo.png', alt: 'Data Fest Siberia 7' },
  { src: '/img/ods-logo.svg', alt: 'Open Data Science' },
  { src: '/img/koronatech-logo.svg', alt: 'koronatech' },
]

function hide(e: Event) {
  ;(e.target as HTMLImageElement).style.display = 'none'
}
</script>

<template>
  <div class="cover-brand">
    <img
      v-for="logo in logos"
      :key="logo.src"
      :src="logo.src"
      :alt="logo.alt"
      class="brand-logo"
      @error="hide"
    />
  </div>
</template>

<style scoped>
/* Логотипы — вертикально, строчка за строчкой, по правому краю:
   горизонтальный ряд не помещается (широкий вордмарк koronatech). */
.cover-brand {
  position: absolute;
  top: 2rem;
  right: 2.5rem;
  display: flex;
  flex-direction: column;
  align-items: flex-end;
  gap: 0.7rem;
}
.brand-logo {
  height: 30px;
  width: auto;
}
</style>
