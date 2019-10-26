<template>
  <button>
    <slot></slot>
  </button>
</template>

<script>
  export default {
    name: 'StartButton'
  };
</script>

<style scoped>
  button {
    border-radius: 15px;
    border-width: 2px;
    border-color: white;
    color: white;
    background-color: #59ac51;
    padding-right: 30px;
    margin-top: 10px;
    margin-bottom: 10px;
    width: 200px;
    height: 40px;
  }

  button::before {
    content: " ";
    display: block;
    width: 13px;
    height: 15px;
    position: absolute;
    top: 13px;
    right: 23px;
    background-size: 13px 15px;
    background: url("../../assets/arrow.png");
  }
</style>
