<script setup>
import pageHeader from './components/pageHeader.vue';
import nowForecastDisplay from './components/nowForecastDisplay.vue';
import todaysForecst from './components/todaysForecst.vue';
import weatherDetails from './components/weatherDetails.vue';

import { ref } from 'vue';
import axios from 'axios';

const weatherData = ref(null);

const forwardingCityOperator = async (searchData) => {
  try {
    const response = await axios.get(`http://localhost:8000/weather/${searchData.city}`, {
      params: { units: searchData.units }
    });

    weatherData.value = response.data;
  }
  catch (error) {
    console.error('Error fetching weather data: ', error);
  }
}
</script>

<template>
  <div>
    <pageHeader @forwardingCityInput="forwardingCityOperator"/>
    <nowForecastDisplay v-if="weatherData" :weatherNow="weatherData.now"/>
    <todaysForecst v-if="weatherData" :weatherIntervalsNow="weatherData.todays_forecast" style="margin-top: 2rem;"/> 
    <weatherDetails v-if="weatherData" :weatherDetails="weatherData.now_details" style="margin-top: 2rem;"/>
  </div>
</template>

<style>
/* Custom margin to position the component lower */
.mt-4 {
  margin-top: 5rem; /* Adjust as needed for desired spacing */
}
</style>
