<script setup>
import { defineProps } from 'vue';

const props = defineProps({
  interval: Object,
})
</script>

<template>
  <div class="card text-center custom-card-bg">
    <div class="card-body p-2">
      <p class="card-title mb-2 text-muted">{{ interval[1].time }}</p> <!-- Gray time -->
      <img :src="interval[1].pic_url" alt="weather icon" class="img-fluid mb-2" style="max-width: 50px;"/>
      <p class="card-text fw-bold text-black">{{ interval[1].temperature }}{{interval[0]}}</p> <!-- Bold black temperature -->
    </div>
  </div>
</template>

<style scoped>
/* Remove border and set the background color */
.custom-card-bg {
  background-color: #eff0fa;
  border: none; /* Removes the default card border */
}

/* Scoped styles to ensure image size is consistent */
.img-fluid {
  max-height: 50px;
}
</style>
