  <script setup>
  import pageHeader from './components/pageHeader.vue';
  import nowForecastDisplay from './components/nowForecastDisplay.vue';
  import { ref } from 'vue';

  const weatherData = ref(null);
  const showNowForecastDisplay = ref(false);

  const forwardingCityOperator = (city) => {
    // api implementation
    weatherData.value = {
        'now': {
          'city': city.city,
          'temperature_max': 12,
          'temperature_min': -3
        },
        'now_details': {
          'sunrise': '8:18',
          'sunset': '18:40',
          'chance_of_rain': 21,
          'pressure': 1023
        },
        'todays_forecast': {
          '6:00': '',
          '9:00': '',
          '12:00': '',
          '15:00': '',
        }
    }
  }

  </script>


  <template>
    -><div v-if="showNowForecastDisplay">{{ weatherData.now }}</div>
    <pageHeader @forwardingCityInput="forwardingCityOperator"/>
    <nowForecastDisplay v-if="weatherData" :weatherNow="weatherData.now"/>
  </template>

  <style>

  </style>
