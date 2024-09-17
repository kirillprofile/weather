<template>
    <div class="type-switch">
      <div 
        @click="setTemperature('celsius')" 
        :class="['toggle-button', { active: temperature === 'celsius', inactive: temperature !== 'celsius' }]">
        °C
      </div>
      <div 
        @click="setTemperature('fahrenheit')" 
        :class="['toggle-button', { active: temperature === 'fahrenheit', inactive: temperature !== 'fahrenheit' }]">
        °F
      </div>
    </div>
  </template>
  
  <script setup>
  import { ref, defineEmits } from 'vue';
  
  const emit = defineEmits(['temperatureChanged']);
  const temperature = ref('celsius'); 
  
  const setTemperature = (type) => {
    temperature.value = type;
    emit('temperatureChanged', type);
  }
  </script>
  
  <style>
  .type-switch {
    display: flex;
    align-items: center;
    gap: 0.5rem;
  }
  .toggle-button {
    cursor: pointer;
    padding: 0.5rem 1rem;
    border-radius: 20px;
    font-size: 16px;
    transition: background-color 0.3s, color 0.3s;
  }
  .active {
    background-color: #007bff;
    color: white;
  }
  .inactive {
    background-color: #e9ecef;
    color: #495057;
  }
  </style>
  