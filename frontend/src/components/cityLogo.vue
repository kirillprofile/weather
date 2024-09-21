<template>
    <!-- Parent container with customizable height -->
    <div class="custom-height d-flex justify-content-center align-items-center flex-column flex-md-row">
        <!-- City and coordinates block with vertical padding -->
        <div v-if="cityData.length" class="text-center py-3 me-4">
            <h1 class="display-2 fw-semibold city-name">{{ cityData[1].name }}</h1>
            <p class="text-muted city-coordinates">
                {{ cityData[1].coord.lat }}° N, {{ cityData[1].coord.lon }}° E
            </p>
        </div>

        <!-- Google Maps with marker based on city coordinates -->
        <iframe 
            v-if="cityData.length"
            :src="googleMapsUrl(cityData[1].coord.lat, cityData[1].coord.lon)"
            class="map-iframe" 
            allowfullscreen="false"
            loading="eager">
        </iframe>
    </div>
</template>

<script setup>
import { defineProps } from 'vue';

const props = defineProps({
    cityData: Array,
});

// Generate Google Maps URL with marker based on latitude and longitude
const googleMapsUrl = (lat, lon) =>
    `https://www.google.com/maps?q=${lat},${lon}&z=4&t=m&output=embed`;
</script>

<style scoped>
/* Example of how to customize height through CSS */
.custom-height {
    height: 20vh; /* Change this value as needed */
    padding: 20px; /* Add some padding for better spacing */
}

/* Font styling for city name and coordinates */
.city-name {
    font-family: 'Roboto', sans-serif; /* Font for city name */
    margin-bottom: -0.5rem;
}

.city-coordinates {
    font-family: 'Open Sans', sans-serif; /* Font for coordinates */
}

/* Center and control map size */
.map-iframe {
    width: 400px; /* Fixed width */
    height: 100%; /* Full height of the parent */
    border: 0; /* Remove border */
    margin-left: 200px; /* Add left margin for spacing */
}
</style>
