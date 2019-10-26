<template>
  <background @getnext="getData"/>
</template>

<script>
  import Background from './game/GameBackground';
  import axios from 'axios';

  const SERVER_ADDRESS = '/bws';

  const myAxios = axios.create({ baseURL: SERVER_ADDRESS });

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

    methods: {
      getData() {
        myAxios.get('/official')
          .then(res => {
            this.name = res.name;
            this.photoUrl = res.photo_url;
            this.regionName = res.region_name;
            this.position = res.position;
            this.income = res.income;
            this.declaratorUrl = res.declarator_url;

            this.$store.commit('addPerson', res);
          })
          .then(res => {

          });
      },
    },

    mounted() {
     this.getData();
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
