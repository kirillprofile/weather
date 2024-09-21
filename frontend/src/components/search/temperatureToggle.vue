<template>
    <div class="type-switch">
      <div 
        @click="setUnits('metric')" 
        :class="['toggle-button', { active: units === 'metric', inactive: units !== 'metric' }]">
        °C
      </div>
      <div 
        @click="setUnits('imperial')" 
        :class="['toggle-button', { active: units === 'imperial', inactive: units !== 'imperial' }]">
        °F
      </div>
    </div>
  </template>
  
  <script setup>
  import { ref, defineEmits } from 'vue';
  
  const emit = defineEmits(['unitsChange']);
  const units = ref('metric'); 
  
  const setUnits = (type) => {
    units.value = type;
    emit('unitsChange', type);
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
  