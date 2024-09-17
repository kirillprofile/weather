<script setup>
import pageHeader from './components/pageHeader.vue';
import nowForecastDisplay from './components/nowForecastDisplay.vue';
import { ref } from 'vue';

const weatherData = ref(null);

const forwardingCityOperator = (city) => {
   // api implementation
   alert(city.city);
}

</script>


<template>
  <pageHeader @forwardingCityInput="forwardingCityOperator"/>
  <nowForecastDisplay/>
</template>

<style>

</style>
