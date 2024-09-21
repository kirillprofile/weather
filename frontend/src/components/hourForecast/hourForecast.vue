<script setup>
import intervalCard from './hourCard.vue';
import { defineProps } from 'vue';

const props = defineProps({
  weatherIntervalsNow: Array, // Array for looping
});
</script>

<template>
  <div class="container py-1 forecast-container">
    <!-- Row for the heading -->
    <div class="row mb-2">
      <div class="col text-start">
        <h5 class="forecast-heading pt-3">TODAY'S FORECAST</h5>
      </div>
    </div>

    <!-- Row for the weather cards -->
    <div class="row justify-content-center">
      <div v-for="(interval, index) in weatherIntervalsNow[1]" :key="index" class="col-6 col-lg-1-5 mb-2">
        <intervalCard :interval="[weatherIntervalsNow[0], interval]"/>
      </div>
    </div>
  </div>
</template>

<style scoped>
/* Custom width for 8 cards per row */
.col-lg-1-5 {
  flex: 0 0 auto;
  width: 12.5%; /* 100 / 8 = 12.5% for 8 cards */
}

/* Background color for the container */
.forecast-container {
  background-color: #e8eaf6;
  border-radius: 8px;
  padding-top: 0.5rem; /* Adjusted padding for reduced height */
  padding-bottom: 0.5rem;
}

/* Gray color and small left margin for the heading */
.forecast-heading {
  color: #6c757d; /* Bootstrap's muted gray */
  margin-left: 10px;
}

/* Reduce margin between cards */
.mb-2 {
  margin-bottom: 0.5rem;
}
</style>
