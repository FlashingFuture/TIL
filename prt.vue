<template>
  <div>
    <p class="greeting">{{ msg }}</p>
  </div>
</template>

<script setup>
// setup function 
import { ref } from 'vue'

const msg = ref('Hello, Vue3!')
</script>

<style scoped>
.greeting {
  color: #888844;
}
</style>