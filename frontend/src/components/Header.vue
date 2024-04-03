<script setup>

import Hero from "./Hero.vue";
</script>

<template>
  <header class="test p-2.5 ">
    <!--    <nav class="container lg mx-auto flex justify-between">-->
    <nav class="container mx-auto max-w-screen-xl flex justify-between p-2.5">
      <div class="font-extrabold text-2xl">WebCrafters</div>
      <ul class="flex gap-8">
        <li>Home</li>
        <li>Product</li>
        <li>About us</li>
        <li>Contact</li>
      </ul>
      <div>
        <button type="button">basket</button>
      </div>
    </nav>
    <Hero/>
  </header>
</template>

<style scoped>

</style>