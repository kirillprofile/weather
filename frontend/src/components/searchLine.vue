<script setup>
import { ref, defineEmits } from 'vue';

const emit = defineEmits(['forwardingCityInput']);

const city = ref('');

const forwardingCityInput = () => {
    emit('forwardingCityInput', city.value);
}
</script>

<template>
    <div class="container">
        <div class="d-flex justify-content-center">
            <input 
                v-model="city" 
                @keyup.enter="forwardingCityInput" 
                placeholder="What city are you interested in?" 
                class="form-control form-control-lg border-0 rounded-pill shadow-sm custom-input" 
            />
        </div>
    </div>
</template>

<style scoped>
/* Custom background color for the input field */
.custom-input {
  background-color: #e8eaf6;
  border: 1px solid transparent; /* Maintain border if needed */
}

/* Keep background color consistent when focused */
.custom-input:focus {
  background-color: #e8eaf6;
  box-shadow: none; /* Remove default focus shadow if needed */
  border-color: #e8eaf6; /* Maintain border color to match background */
}
</style>
