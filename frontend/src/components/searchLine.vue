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
                class="form-control form-control-lg border-0 rounded-pill shadow-sm" 
            />
        </div>
    </div>
</template>
