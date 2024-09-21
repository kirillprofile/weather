<template>
    <div class="container">
        <div class="d-flex justify-content-center position-relative">
            <input 
                v-model="city" 
                @keyup.enter="forwardingCityInput" 
                placeholder="What city are you interested in?" 
                class="form-control form-control-lg border-0 rounded-pill shadow-sm custom-input" 
            />
            <button 
                @click="forwardingCityInput" 
                class="btn search-button position-absolute">
                Search
            </button>
        </div>
    </div>
</template>

<script setup>
import { ref, defineEmits } from 'vue';

const emit = defineEmits(['forwardingCityInput']);

const city = ref('');

const forwardingCityInput = () => {
    emit('forwardingCityInput', city.value);
}
</script>

<style scoped>
.custom-input {
    background-color: #e8eaf6;
    border: 1px solid transparent;
    padding-right: 4rem; /* Add padding to accommodate the button */
}

.custom-input:focus {
    background-color: #e8eaf6;
    box-shadow: none;
    border-color: #e8eaf6;
}

.search-button {
    background-color: #5c6bc0; /* Button background color */
    color: white; /* Button text color */
    border: none; /* Remove border */
    border-radius: 20px; /* Make the button more rounded */
    padding: 0.5rem 1rem; /* Adjust button padding */
    height: 80%; /* Make button fill the height of the input */
    width: auto; /* Adjust width as needed */
    top: 50%; /* Center vertically */
    transform: translateY(-50%); /* Adjust vertical alignment */
    right: 7px; /* Increase this value to move the button further right */
    cursor: pointer; /* Change cursor to pointer */
}
</style>
