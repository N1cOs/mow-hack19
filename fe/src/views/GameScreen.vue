<template>
    <background />
</template>

<script>
  import Background from './game/GameBackground';

  export default {
    name: 'BackgroundGame',

    components: {
      Background,
    },

    data() {
      return {
        name: '',
        photoUrl: '',
        regionName: null,
        position: null,
        products: [],
        income: 0
      };
    },

    methods: {},

    mounted() {
      // axios
      //   .get('official')
      //   .then(res => {
      //     this.name = res.name;
      //     this.photoUrl = res.photoUrl;
      //     this.regionName = res.regionName;
      //     this.position = res.position;
      //     this.income = res.income;
      //     this.declaratorUrl = res.declaratorUrl;
      //
      //     this.$store.commit('addPerson', res);
      //   });
      //
      // axios
      //   .get('item')
      //   .then(res => {
      //
      //   });
    },

    computed: {
      surname() {
        return name.split(' ')[0];
      },

      nameAndSecondName() {
        const nameSplitted = name.split(' ');
        return `${nameSplitted[1]} ${nameSplitted[2]}`;
      }
    }
  };
</script>
