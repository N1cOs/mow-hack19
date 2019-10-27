<template>
  <div class="root">

  </div>
</template>

<script>
  export default {
    name: 'HistorySreen',

    created() {
      console.log(this.$store.state.persons);
    }
  };
</script>

<style scoped>
  .root {
    width: 100%;
    height: 100%;
  }
</style>
