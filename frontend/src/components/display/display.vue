<script setup>
import { defineProps } from 'vue';

// Define props
const props = defineProps({
    weatherNow: Array,
});
</script>

<template>
  <div class="container mt-4 d-flex justify-content-center align-items-center">
    <div class="weather-card d-flex align-items-center p-3">
      <!-- Text block -->
      <div class="weather-text d-flex flex-column flex-grow-1 me-3">
        <h1 class="city-name mb-2">{{ weatherNow[1].city }}</h1>
        <div class="d-flex align-items-baseline">
          <div class="temperature-max me-2">{{ weatherNow[1].temperature_max }}{{ weatherNow[0] }}</div>
          <div class="temperature-min">{{ weatherNow[1].temperature_min }}{{ weatherNow[0] }}</div>
        </div>
      </div>

      <!-- Image on the right -->
      <img 
        src="@/assets/icons/weather.png" 
        alt="Weather Icon"
        class="weather-icon"
      />
    </div>
  </div>
</template>

<style>
/* Import fonts */
@import url('https://fonts.googleapis.com/css2?family=Roboto:wght@400;700&family=Open+Sans:wght@300;600&display=swap');

.weather-card {
  max-width: 400px; 
  height: 200px; 
  display: flex;
  align-items: center;
}

.weather-text {
  flex-grow: 1;
}

.city-name {
  font-family: 'Roboto', sans-serif;
  font-size: 2rem; /* Adjust font size as needed */
  font-weight: 600;
  color: #333;
  margin-bottom: 0.5rem;
}

.temperature-max {
  font-family: 'Open Sans', sans-serif;
  font-size: 3rem;
  font-weight: normal;
  color: #333;
}

.temperature-min {
  font-family: 'Open Sans', sans-serif;
  font-size: 2rem;
  font-weight: 300;
  color: #888;
}

.weather-icon {
  height: 100%; 
  width: auto; 
  object-fit: cover;
}
</style>
