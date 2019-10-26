<template>
  <background>
    <template #border-top>
      Buckwheat
    </template>
    <template #yellow>
      F
    </template>
    <template #purple>
      Нажмите F, чтобы начать
    </template>
    <template #border-bottom>
      salary
    </template>
  </background>
</template>

<script>
  import StartButton from './start/StartButton';
  import Background from './start/StartBackground';

  export default {
    name: 'StartScreen',

    components: {
      StartButton,
      Background
    }
  };
</script>
