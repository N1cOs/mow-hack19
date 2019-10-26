<template>
  <div class="root">
    <div class="yellow xl-h">
      <div  class="yellow-border">
        Bluckwheat
      </div>
      <div class="yellow-inner">

      </div>
    </div>
    <div class="purple xs-h">
      <div class="purple-inner">

      </div>
      <div class="purple-border">
        salary
      </div>
    </div>
  </div>
</template>

<script>
  export default {
    name: 'FinalBackground'
  };
</script>

<style scoped>
  .root {
    background-color: black;
    width: 100%;
    height: 100%;
  }

  .yellow {
    background-color: var(--yellow);
    width: 100%;
    position: absolute;
    height: 16%;
    top: 30%;
    z-index: 2;
  }

  .yellow-border {
    font-size: 48px;
    /*line-height: 20px;*/
    color: #FBD08B;
    transform: rotate(-12.74deg);
    top: -1.65em;
    right: 10%;
    position: relative;
  }

  .yellow-inner {
    color: var(--purple);
    font-size: 72px;
    position: relative;
    bottom: 25%;
  }

  .yellow::before {
    position: absolute;
    content: "";
    width: 100%;
    height: 100%;
    top: 0;
    left: 0;
    transform-origin: top left;
    transform: skewY(-12.74deg);
    background-color: var(--yellow);
    z-index: -1;
  }

  .yellow::after {
    position: absolute;
    content: "";
    width: 100%;
    height: 100%;
    top: 0;
    left: 0;
    transform-origin: top left;
    transform: skewY(5deg);
    background-color: var(--yellow);
    z-index: -1;
    box-shadow: 0 8px 6px -2px rgba(0, 0, 0, 0.25);
  }

  .purple {
    position: relative;
    height: 11%;
    width: 100%;
    top: 41%;
    background-color: var(--purple);
    z-index: 1;
  }

  .purple::after {
    position: absolute;
    content: "";
    width: 100%;
    height: 100%;
    top: 61px;
    left: 0;
    transform-origin: top left;
    transform: skewY(-4.33deg);
    background-color: var(--purple);
    z-index: -1;
  }

  .purple-inner {
    font-size: 20px;
    color: #B6A6FC;
    top: 65%;
    position: relative;
  }

  .purple-border {
    color: #7765C2;
    font-size: 64px;
    top: 1.2em;
    position: relative;
    transform: rotate(-4.33deg);
    text-align: right;
    padding-right: 6%;
  }
</style>
