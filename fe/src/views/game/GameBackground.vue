<template>
  <div class="root">
    <div style="position: fixed; left: 50%; transform: translate(-50%); top: 8%; font-size: 48px;
     line-height: 20px;">
      <span v-show="showTrue" style="color: #7BF5C2">
        Верно!
      </span>
      <span v-show="showFalse" style="color:#FF8880;">
        Неверно!
      </span>
    </div>
    <div :class="['yellow', 'xl-h', successPurple, failPurple]" @click="tryYellow" ref="yellow">
      <div class="yellow-border">
        {{ this.surname }}
      </div>
      <div class="yellow-inner">
        <div class="name">
          {{ this.name }}
        </div>
        <div class="info">
          <div>
            <p class="position">
              {{ this.position }}
            </p>
            <p class="income">
              {{ `${this.income} Р` }}
            </p>
            <p class="region">
              Москва
            </p>
          </div>
          <img :src="this.photoUrl" width="115" height="150">
        </div>
      </div>
    </div>
    <div :class="['purple', 'xs-h', successYellow, failYellow]" @click="tryPurple" ref="purple">
      <div class="purple-inner">

      </div>
      <div class="purple-border">

      </div>
    </div>
    <div class="question" v-show="!(showFalse || showTrue)">
      Что больше?
    </div>
  </div>
</template>

<script>
  export default {
    name: 'GameBackground',

    data() {
      return {
        successY: false,
        successP: false,
        failY: false,
        failP: false,
        showTrue: false,
        showFalse: false,
        buttonPressed: false
      };
    },

    props: {
      surname: {
        default: 'Жириновский'
      },
      name: {
        default: 'Владимир Вольфович'
      },
      position: {
        default: 'Руководитель фракции'
      },
      regionName: {
        default: 'г. Москва'
      },
      photoUrl: {
        default: 'https://declarator.org/media/cache/43/de/43deb2166a8c3d500277420c8d1850a1.png'
      },
      products: [],
      income: {
        default: 1000000
      }
    },

    methods: {
      tryYellow() {
        if (!this.buttonPressed) {
          if (this.income >= 100) {
            this.successY = true;
            setTimeout(() => {
                this.showTrue = true;
              }, 1000);
          } else {
            this.failY = true;
            setTimeout(() => this.showFalse = true, 1000);
          }
          this.buttonPressed = true;
        }
      },

      tryPurple() {
        if (!this.buttonPressed) {
          if (100 >= this.income) {
            this.successP = true;
            setTimeout(() => this.showTrue = true, 1000);
          } else {
            this.failP = true;
            setTimeout(() => this.showFalse = true, 1000);
          }
          this.buttonPressed = true;
        }
      },
    },

    computed: {
      successYellow() {
        return this.successY ? 'success-yellow' : '';
      },

      successPurple() {
        return this.successP ? 'success-purple' : '';
      },

      failYellow() {
        return this.failY ? 'fail-yellow' : '';
      },

      failPurple() {
        return this.failP ? 'fail-purple' : '';
      },
    }
  };
</script>


<style scoped>
  .root {
    background-color: black;
    width: 100%;
    height: 100%;
  }

  .purple.success-yellow, .purple.fail-yellow {
    transition: background-color 0.5s ease;
    background-color: rgb(61, 39, 85);
  }

  .success-yellow .purple-inner, .fail-yellow .purple-inner {
    transition: color 0.5s ease;
    color: rgb(108, 93, 65);
  }

  .yellow.success-purple, .yellow.fail-purple {
    transition: background-color 0.5s ease;
    background-color: rgb(140, 119, 82);
  }

  .success-purple .yellow-inner, .fail-purple .yellow-inner {
    transition: color 0.5s ease;
    color: rgb(78, 47, 110);
  }

  .success-purple .yellow-border,
  .fail-purple .yellow-border {
    transition: color 0.5s ease;
    color: rgb(140, 119, 82);
  }

  .success-purple img,
  .fail-purple img {
    transition: opacity 0.5s ease;
    opacity: 0.5;
  }


  .yellow {
    background-color: var(--yellow);
    width: 100%;
    position: absolute;
    height: 16%;
    top: 30%;
    z-index: 2;
  }

  .yellow .info {
    display: flex;
    flex-direction: row;
    align-self: flex-start;
    justify-content: space-between;
    margin-left: 19px;
    margin-right: 15px;
    text-align: left;
    margin-top: -74px;
  }

  .yellow .info div {
    margin-top: 70px;
  }

  .yellow-border {
    font-size: 48px;
    color: #FBD08B;
    transform: rotate(-12.74deg);
    top: -1.7em;
    font-weight: 500;
    right: 10%;
    position: relative;
  }

  .yellow-inner {
    color: var(--purple);
    position: relative;
    bottom: 25%;
  }

  .yellow .position {
    font-size: 14px;
    line-height: 20px;
    margin-top: -34px;
    margin-bottom: 15px;
  }

  .yellow .income {
    font-weight: 300;
    font-size: 24px;
    line-height: 20px;
    text-align: center;
    margin-bottom: 15px;
  }

  .yellow-inner .name {
    font-size: 24px;
    line-height: 20px;
    transform: rotate(-13.81deg);
    position: relative;
    top: -3.7em;
    font-weight: 500;
    right: -15%;
    display: inline-block;
  }

  .yellow .region {
    font-size: 14px;
    line-height: 20px;
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
    background-color: inherit;
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
    background-color: inherit;
    z-index: -1;
    box-shadow: 0 8px 8px -2px rgba(0, 0, 0, 0.25);
  }

  .purple {
    position: relative;
    height: 15.8%;
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
    -webkit-transform-origin: top left;
    transform-origin: top left;
    -webkit-transform: skewY(5deg);
    transform: skewY(-4.33deg);
    background-color: inherit;
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

  .question {
    color: #B6A6FC;
    font-size: 20px;
    line-height: 20px;
    position: relative;
    top: 64%;
  }
</style>
