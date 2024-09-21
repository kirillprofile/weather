<script setup>
import SearchLine from './search/searchLine.vue';
import TemperatureToggle from './search/temperatureToggle.vue';
import ModeToggle from './search/modeToggle.vue';
import { ref, defineEmits } from 'vue';

const emit = defineEmits(['forwardingCityInput', 'unitsChangeDynamic', 'modeChangeDynamic']);
const units = ref('metric');
const modeParam = ref('now');
const cityName = ref(''); // Ref to store the city name

const forwardingCityInput = (city) => {
    cityName.value = city; // Store the city name
    emit('forwardingCityInput', {
        city: city,
        units: units.value,
        mode: modeParam.value
    });
}

const unitsChangeDynamic = (type) => {
    units.value = type;
    emit('unitsChangeDynamic', {
        units: units.value,
        city: cityName.value, // Pass the city name
        mode: modeParam.value
    });
}

const modeChangedDynamic = (mode) => {
    modeParam.value = mode;
    emit('modeChangeDynamic', {
        units: units.value,
        city: cityName.value, // Pass the city name
        mode: modeParam.value
    });
}
</script>

<template>
    <header class="d-flex flex-column align-items-center p-3">
        <div class="header-content d-flex align-items-center w-100 justify-content-between">
            <div class="logo-title-container d-flex align-items-center me-3">
                <img src="" alt="Logo" class="logo me-2" /><!--src="@/assets/icons/logo.png"-->
                <h1 class="title mb-0">Simple Weather</h1>
            </div>
            <div>
                <ModeToggle @modeChanged="modeChangedDynamic"/>
            </div>
            <div class="search-toggle-container d-flex align-items-center gap-3 flex-grow-1">
                <div class="search-wrapper flex-grow-1">
                    <SearchLine @forwardingCityInput="forwardingCityInput" />
                </div>
                <TemperatureToggle @unitsChange="unitsChangeDynamic" />
            </div>
        </div>
    </header>
</template>

<style>
/* Используем классы Bootstrap для верстки */
.logo {
    height: 40px;
    width: auto;
}

.title {
    color: rgb(51, 51, 51);
    font-weight: bold;
    font-size: 1.5rem;
}

.header-content {
    max-width: 1200px; /* Устанавливает максимальную ширину контейнера */
    width: 100%; /* Позволяет контейнеру занимать всю доступную ширину */
    margin: 0 auto; /* Центрирует блок по горизонтали */
    padding-top: 20px;
    padding-bottom: 20px;
}

.search-toggle-container {
    max-width: 550px; /* Ограничивает максимальную ширину контейнера поиска */
}

.search-wrapper {
    flex: 1; /* Дает поисковой строке использовать доступное пространство */
}
</style>