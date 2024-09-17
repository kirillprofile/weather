<script setup>
import { defineProps } from 'vue';

// Определение пропсов
const props = defineProps({
    weatherNow: Object,
});
</script>

<template>
  <div class="container mt-4">
    <div class="weather-card d-flex align-items-center p-3">
      <!-- Блок с текстом -->
      <div class="weather-text d-flex flex-column flex-grow-1 me-3">
        <h1 class="city-name mb-2">{{ weatherNow?.city }}</h1>
        <div class="d-flex align-items-baseline">
          <div class="temperature-max me-2">{{ weatherNow?.temperature_max }}°C</div>
          <div class="temperature-min">{{ weatherNow?.temperature_min }}°C</div>
        </div>
      </div>

      <!-- Картинка справа -->
      <img 
        src="@/assets/icons/weather.png" 
        alt="Weather Icon"
        class="weather-icon"
      />
    </div>
  </div>
</template>

<style>
/* Используем шрифт из Google Fonts или другого источника */
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
  font-size: rem; /* Увеличиваем размер шрифта для названия города */
  font-weight: 600; /* Убираем жирное начертание */
  color: #333;
  margin-bottom: 0.5rem;
}

.temperature-max {
  font-family: 'Open Sans', sans-serif;
  font-size: 3rem; /* Устанавливаем размер шрифта для максимальной температуры */
  font-weight: normal;
  color: #333;
}

.temperature-min {
  font-family: 'Open Sans', sans-serif;
  font-size: 2rem; /* Устанавливаем размер шрифта для минимальной температуры */
  font-weight: 300;
  color: #888;
}

.weather-icon {
  height: 100%; 
  width: auto; 
  object-fit: cover;
}
</style>
