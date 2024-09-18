<script setup>
import { defineProps } from 'vue';
import infoIcon from '@/assets/icons/info.png' // Import the image

const props = defineProps({
    detailData: Array,
});
</script>

<template>
    <div class="detail-card d-flex align-items-center p-3">
        <div class="me-3 flex-grow-1">
            <p class="text-muted mb-1">{{ detailData[0] }}</p>
            <p class="mb-0 fw-bold">{{ detailData[1] }}</p>
        </div>
            <img 
                :src="infoIcon"
                alt="Weather Icon"
            />
    </div>
</template>

<style scoped>
.detail-card {
    background-color: #f0f0fa;
    border-radius: 8px;
    box-shadow: 0 2px 4px rgba(0, 0, 0, 0.1);
    display: flex;
    align-items: center;
}

.icon-placeholder {
    width: 24px; /* Adjust width as needed */
    height: 24px; /* Adjust height as needed */
    background-color: #e0e0e0; /* Placeholder color */
    border-radius: 50%; /* Circular placeholder */
    display: flex;
    align-items: center;
    justify-content: center;
}

.me-3 {
    margin-right: 1rem; /* Space between text and icon */
}
</style>
