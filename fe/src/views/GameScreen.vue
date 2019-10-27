<template>
  <div>
    <background
      :surname="surname"
      :name="nameAndSecondName"
      :position="computedPosition"
      :regionName="regionName || 'Российская Федерация'"
      :photoUrl="photoUrl"
      :items="itemsObject"
      :income="flooredIncome"
      @getnext="getData"
    />
  </div>
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
        income: 0,
        itemsObject: {}
      };
    },

    methods: {
      getData() {
        myAxios.get('/official')
          .then(res => {
            console.log('official', res);
            this.name = res.data.name;
            this.photoUrl = res.data.photo_url;
            this.regionName = res.data.region_name;
            this.position = res.data.position;
            this.income = res.data.income;
            this.declaratorUrl = res.data.declarator_url;

            this.$store.commit('addPerson', {
              name: this.name,
              photoUrl: this.photoUrl,
              regionName: this.regionName,
              position: this.position,
              income: this.income,
              declarationUrl: this.declaratorUrl
            });
          })
          .then(res => {
            myAxios.get(`/item?income=${Math.floor(this.flooredIncome)}`)
              .then(res => {
                console.log('item', res.data);
                this.itemsObject = res.data;
              });
          });
      },
    },

    mounted() {
      this.getData();
    },

    computed: {
      surname() {
        return this.name.split(' ')[0];
      },

      nameAndSecondName() {
        const nameSplitted = this.name.split(' ');
        return `${nameSplitted[1]} ${nameSplitted[2]}`;
      },

      computedPosition() {
        return this.position ?
          this.position.length > 48
            ? (() => {
            const position = this.position.substr(0, 48);
            let continuePos = this.position.substr(48);
            console.log(position, continuePos);
            continuePos = continuePos.split(' ')[0];
            return `${position + continuePos}...`;
          })() :
          this.position : '';
      },

      flooredIncome() {
        return Math.floor(this.income);
      }
    }
  };
</script>

<style scoped>
  div {
    width: 100%;
    height: 100%;
  }
</style>
