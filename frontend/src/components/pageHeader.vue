<script setup>
import SearchLine from './searchLine.vue';
import TemperatureToggle from './temperatureToggle.vue';
import { ref, defineEmits } from 'vue';

const emit = defineEmits(['forwardingCityInput', 'temperatureChanged']);
const temperatureType = ref('celsius');

const forwardingCityInput = (city) => {
    emit('forwardingCityInput', {
        city: city,
        type: temperatureType.value
    });
}

const temperatureChanged = (type) => {
    temperatureType.value = type;
}
</script>

<template>
    <header class="d-flex flex-column align-items-center p-3">
        <div class="header-content d-flex align-items-center w-100 justify-content-between">
            <div class="logo-title-container d-flex align-items-center me-3">
                <img src="@/assets/icons/logo.png" alt="Logo" class="logo me-2" />
                <h1 class="title mb-0">Simple Weather</h1>
            </div>
            <div class="search-toggle-container d-flex align-items-center gap-3 flex-grow-1">
                <div class="search-wrapper flex-grow-1">
                    <SearchLine @forwardingCityInput="forwardingCityInput" />
                </div>
                <TemperatureToggle @temperatureChanged="temperatureChanged" />
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