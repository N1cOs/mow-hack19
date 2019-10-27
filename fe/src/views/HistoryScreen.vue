<template>
  <div class="root">
    <a
      v-for="(person, index) in guys"
      :key="person.name"
      :href="person.declaratorUrl"
    >
      <man
        :photoUrl="person.photoUrl"
        :name="person.name"
        :income="person.income"
        :index="index"
        :href="person.declarationUrl"
      />
    </a>
  </div>
</template>

<script>
  import Man from '../Man';

  export default {
    name: 'History',

    components: {
      Man
    },

    data() {
      return {
        guys: [],
      }
    },

    created() {
      this.guys = this.$store.state.persons;
      console.log(this.guys)
    }
  };
</script>


<style scoped>
  .root {
    background-color: black;
    width: 100%;
    height: 100%;
    overflow: scroll;
    padding: 20px;
    padding-top: 40px;
  }
</style>
