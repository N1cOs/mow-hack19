<template>
  <div>
    <loading
      :active.sync="isLoading"
      :opacity="1"
      background-color="#000"
      color="#fff"
      :is-full-page="true"></loading>
    <background
      :surname="surname"
      :name="nameAndSecondName"
      :position="computedPosition"
      :regionName="regionName || 'Российская Федерация'"
      :photoUrl="photoUrl"
      :items="itemsObject"
      :income="flooredIncome"
      :incomeFormatted="incomeFormatted"
      @getnext="getData"
    />
  </div>
</template>

<script>
  import Loading from 'vue-loading-overlay';
  import 'vue-loading-overlay/dist/vue-loading.css';
  import Background from './game/GameBackground';
  import axios from 'axios';

  const SERVER_ADDRESS = '/bws';

  const myAxios = axios.create({ baseURL: SERVER_ADDRESS });

  export default {
    name: 'BackgroundGame',

    components: {
      Background,
      Loading
    },

    data() {
      return {
        name: '',
        photoUrl: '',
        regionName: null,
        position: null,
        income: 0,
        itemsObject: {},
        isLoading: false,
        incomeFormatted: ''
      };
    },

    methods: {
      getData() {
        this.isLoading = true;
        myAxios.get('/official')
          .then(res => {
            console.log(res.data.incomeStr);
            this.name = res.data.name;
            this.photoUrl = res.data.photo_url;
            this.regionName = res.data.region_name;
            this.position = res.data.position;
            this.income = res.data.income;
            this.declaratorUrl = res.data.declarationUrl;
            this.incomeFormatted = res.data.incomeStr;

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
                this.itemsObject = res.data;
                this.isLoading = false;
              });
          })
          .catch(err => {
            console.log('Error occured');
            this.isLoading = false;
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
