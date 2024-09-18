<template>
    <div class="type-switch">
      <div 
        @click="setTemperature('metric')" 
        :class="['toggle-button', { active: temperature === 'metric', inactive: temperature !== 'metric' }]">
        °C
      </div>
      <div 
        @click="setTemperature('imperial')" 
        :class="['toggle-button', { active: temperature === 'imperial', inactive: temperature !== 'imperial' }]">
        °F
      </div>
    </div>
  </template>
  
  <script setup>
  import { ref, defineEmits } from 'vue';
  
  const emit = defineEmits(['temperatureChanged']);
  const temperature = ref('metric'); 
  
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
    background-color: #5c6bc0;
    color: white;
  }
  .inactive {
    background-color: #e9ecef;
    color: #495057;
  }
  </style>
  