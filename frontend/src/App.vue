<script setup>
import pageHeader from './components/pageHeader.vue';
import nowForecastDisplay from './components/display/display.vue';
import todaysForecst from './components/hourForecast/hourForecast.vue';
import weatherDetails from './components/details/weatherDetails.vue';
import cityLogo from './components/cityLogo.vue';

import { ref } from 'vue';
import axios from 'axios';

const weatherDataNow = ref(null);
const weatherData5Days = ref(null);
const modeGlobal = ref(null);
const city = ref(null);

const unitsGlobal = ref('metric');
const degreeSymbol = ref('°C')

const unitsChangeOperatorDynamic = async (data) => {
    unitsGlobal.value = data.units;
    forwardingCityOperator(data);
};

const forwardingCityOperator = async (searchData) => {
    city.value = searchData.city;
    modeGlobal.value = searchData.mode;
    
    unitsGlobal.value = searchData.units;
    degreeSymbol.value = (unitsGlobal.value === 'metric') ? '°C' : '°F';

    // Check for city presence
    if (!searchData.city?.trim()) {
        console.warn('City is undefined or empty. No action taken.');
        return;
    }
    
    if (modeGlobal.value === 'now') {
        try {
            const response = await axios.get(`http://localhost:8000/weather/${city.value}`, {
                params: { units: unitsGlobal.value }
            });
            weatherDataNow.value = response.data;
        } catch (error) {
            console.error('Error fetching weather data: ', error);
        }
    } else if (modeGlobal.value === 'fiveDays') {
        try {
            const response = await axios.get(`http://localhost:8000/weather/5days/${city.value}`, {
                params: { units: unitsGlobal.value }
            });
            weatherData5Days.value = response.data;
        } catch (error) {
            console.error('Error fetching weather data: ', error);
        }
    }
};
import 'bootstrap/dist/css/bootstrap.min.css'; // Импортируем стили Bootstrap
import 'bootstrap'; // Импортируем JavaScript Bootstrap (если нужно)
</script>

<template>
  <div class="container">
      <pageHeader 
          @forwardingCityInput="forwardingCityOperator" 
          @unitsChangeDynamic="unitsChangeOperatorDynamic"
          @modeChangeDynamic="forwardingCityOperator"
      />
      <div v-if="weatherDataNow && modeGlobal === 'now'" class="mt-4">
          <nowForecastDisplay v-if="weatherDataNow" :weatherNow="[weatherDataNow.degree_symbol, weatherDataNow.now]"/>
          <todaysForecst v-if="weatherDataNow" :weatherIntervalsNow="[weatherDataNow.degree_symbol, weatherDataNow.todays_forecast]" class="mt-4"/> 
          <weatherDetails v-if="weatherDataNow" :weatherDetails="weatherDataNow.now_details" class="mt-4"/>
      </div>
      <div v-else-if="modeGlobal === 'fiveDays'" class="mt-4">
          <cityLogo v-if="weatherData5Days" :cityData="[degreeSymbol, weatherData5Days.city]" class="mt-5rem"/>
          <div v-if="weatherData5Days">
              <!-- Additional content for 5-day weather forecast -->
          </div>
      </div>
  </div>
</template>


<style>
/* You can remove custom styles since Bootstrap classes are used */
.mt-5rem {
    margin-top: 5rem; /* Adjust this value as needed */
}
</style>
