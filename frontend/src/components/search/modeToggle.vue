<template>
    <div class="mode-switch">
      <div 
        @click="setMode('now')" 
        :class="['toggle-button', { active: mode === 'now', inactive: mode !== 'now' }]">
        Today & Now
      </div>
      <div 
        @click="setMode('fiveDays')" 
        :class="['toggle-button', { active: mode === 'fiveDays', inactive: mode !== 'fiveDays' }]">
        5 Days
      </div>
    </div>
  </template>
  
  <script setup>
  import { ref, defineEmits } from 'vue';
  
  const emit = defineEmits(['modeChanged']);
  const mode = ref('now');
  
  const setMode = (newMode) => {
    mode.value = newMode;
    emit('modeChanged', newMode);
  }
  </script>
  
  <style>
  .mode-switch {
    display: flex;
    align-items: center;
    gap: 1rem;
    background-color: #e8eaf67c;
    border-radius: 20px;

    min-width: 200px; /* Set a minimum width as needed */
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
    background-color: transparent;
    color: #495057;
  }
  </style>
  