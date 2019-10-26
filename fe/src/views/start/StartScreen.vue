<template>
  <div>
    <router-link to="/game">
      <start-button>
        F
      </start-button>
    </router-link>
  </div>
</template>

<script>
  import StartButton from './StartButton';

  export default {
    name: 'StartScreen',

    components: {
      StartButton
    }
  };
</script>

<style scoped>

</style>
