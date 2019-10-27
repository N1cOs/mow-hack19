<template>
  <div
    class="yellow xl-h"
  >
    <div class="yellow-border">
      {{ this.surname }}
    </div>
    <div class="yellow-inner">
      <div class="name">
        {{ this.name }}
      </div>
      <div class="info">
        <div>
          <p class="position">
            {{ this.position }}
          </p>
          <p class="income">
            {{ `${this.items.totalSumStr} Р` }}
          </p>
          <p class="region">
            Москва
          </p>
        </div>
        <div style="height: 150px; width: 115px; overflow: hidden; margin-top: -10px">
          <img :src="this.photoUrl" height="150">
        </div>
      </div>
    </div>
  </div>
</template>

<script>
  export default {
    name: 'Purple'
  };
</script>

<style scoped>

</style>
