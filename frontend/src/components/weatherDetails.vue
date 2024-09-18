<script setup>
import detailCard from './detailCard.vue';
import { defineProps } from 'vue';

const props = defineProps({
    weatherDetails: Object,
});
</script>

<template>
  <div class="container py-1 details-container">
    <!-- Row for the heading -->
    <div class="row mb-2">
      <div class="col text-start">
        <h5 class="details-heading pt-3">WEATHER DETAILS</h5>
      </div>
    </div>

    <!-- Row for the detail cards -->
    <div class="row justify-content-center">
      <div v-for="(detail, name) in weatherDetails" :key="name" class="col-6 col-lg-1-4 mb-2">
        <detailCard :detailData="detail"/>
      </div>
    </div>
  </div>
</template>

<style scoped>
/* Custom width for cards per row */
.col-lg-1-4 {
  flex: 0 0 auto;
  width: 25%; /* 100 / 4 = 25% for 4 cards per row */
}

/* Background color for the container */
.details-container {
  background-color: #e8eaf6;
  border-radius: 8px;
  padding-top: 0.5rem; /* Adjusted padding for reduced height */
  padding-bottom: 0.5rem;
}

/* Gray color and small left margin for the heading */
.details-heading {
  color: #6c757d; /* Bootstrap's muted gray */
  margin-left: 10px;
}

/* Reduce margin between cards */
.mb-2 {
  margin-bottom: 0.5rem;
}
</style>
