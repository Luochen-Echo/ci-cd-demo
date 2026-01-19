<template>
  <div id="app">
    <h1>Vue Frontend</h1>
    <div v-if="loading">Loading...</div>
    <div v-else>
      <h2>Backend Status: {{ healthStatus }}</h2>
      <h3>Data Items:</h3>
      <ul>
        <li v-for="item in items" :key="item.id">
          {{ item.name }}
        </li>
      </ul>
    </div>
  </div>
</template>

<script setup>
import { ref, onMounted } from 'vue'

const loading = ref(true)
const healthStatus = ref('')
const items = ref([])

onMounted(async () => {
  try {
    const healthRes = await fetch('/api/health')
    const healthData = await healthRes.json()
    healthStatus.value = healthData.status

    const dataRes = await fetch('/api/data')
    const data = await dataRes.json()
    items.value = data.items
  } catch (error) {
    console.error('Error:', error)
  } finally {
    loading.value = false
  }
})
</script>

<style>
#app {
  font-family: Arial, sans-serif;
  max-width: 800px;
  margin: 50px auto;
  padding: 20px;
}
</style>
