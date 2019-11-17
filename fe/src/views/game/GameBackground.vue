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
    <div
      :class="['yellow', 'xl-h', successPurple, failPurple]"
      @click="tryYellow"
      ref="yellow"
    >
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
              {{ `${this.incomeFormatted} Р` }}
            </p>
            <p class="region">
              {{ `${this.regionName}` }}
            </p>
          </div>
          <div style="height: 150px; width: 115px; overflow: hidden; margin-top: -10px">
            <img :src="this.photoUrl" height="150">
          </div>
        </div>
      </div>
    </div>
    <div
      :class="['purple', 'xs-h', successYellow, failYellow, 'p-1']"
      @click="tryPurple"
      v-if="items.items"
    >
      <div class="purple-inner">
        {{ items.items[0].item_count + ' ' + items.items[0].item_unit }}
      </div>
      <div class="purple-border">
        {{ items.items[0].item_name }}

      </div>
    </div>
    <div
      :class="['purple', 'xs-h', successYellow, failYellow, 'p-2']"
      @click="tryPurple"
      v-if="this.items.items ? this.items.items[1] : false"
    >
      <div class="purple-inner">
        {{ items.items[1].item_count + ' ' + items.items[1].item_unit }}
      </div>
      <div class="purple-border">
        {{ items.items[1].item_name }}
      </div>
    </div>
    <div
      :class="['purple', 'xs-h', successYellow, failYellow, 'p-3']"
      @click="tryPurple"
      v-if="this.items.items ? this.items.items[2] : false"
    >
      <div class="purple-inner">
        {{ items.items[2].item_count + ' ' + items.items[2].item_unit }}
      </div>
      <div class="purple-border">
        {{ items.items[2].item_name }}
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
      items: {
        default: {}
      },
      income: {
        default: 1000000
      },
      incomeFormatted: {
        default: ''
      },
    },

    methods: {
      init() {
        this.successY = false;
        this.successP = false;
        this.failY = false;
        this.failP = false;
        this.showTrue = false;
        this.showFalse = false;
        this.buttonPressed = false;
      },

      tryYellow() {
        if (!this.buttonPressed) {
          if (this.income >= this.items.totalSum) {
            this.successY = true;
            setTimeout(() => {
              this.showTrue = true;
            }, 1000);
            this.$store.commit('addPoint');
            setTimeout(() => this.$emit('getnext'), 2000);
          } else {
            this.failY = true;
            setTimeout(() => this.showFalse = true, 1000);
            setTimeout(() => this.$router.push('/final'), 2000);
          }

          this.buttonPressed = true;
        }
      },

      tryPurple() {
        if (!this.buttonPressed) {
          if (this.items.totalSum >= this.income) {
            this.successP = true;
            setTimeout(() => this.showTrue = true, 1000);
            setTimeout(() => this.$emit('getnext'), 2000);
            this.$store.commit('addPoint');
          } else {
            this.failP = true;
            setTimeout(() => this.showFalse = true, 1000);
            setTimeout(() => this.$router.push('/final'), 2000);
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
    },

    watch: {
      photoUrl() {
        this.init();
        console.log(this.items);
      }
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

  .p-2::after {
    box-shadow: 0px 24px 29px 12px rgba(0, 0, 0, 0.55);

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
    margin-top: 60px;
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
    margin-bottom: 4px;
  }

  .yellow .income {
    font-weight: 300;
    font-size: 24px;
    line-height: 20px;
    text-align: center;
    margin-bottom: 0px;
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
    height: 15%;
    width: 100%;
    top: 34%;
    background-color: var(--purple);
  }

  .purple::after {
    position: absolute;
    content: "";
    width: 100%;
    height: 100%;
    top: 61px;
    left: 0;
    transform-origin: top right;
    transform: skewY(-4.33deg);
    background-color: inherit;
    z-index: 1;
  }

  .p-1 .purple-border {
    top: 121px;
  }

  .p-1 .purple-inner {
    top: 120px;
    right: 176px;
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
    position: fixed;
    top: 91%;
    left: 50%;
    transform: translate(-50%);
  }

  .p-3::after {
    box-shadow: 0px 24px 29px 12px rgba(0, 0, 0, 0.55);
    position: absolute;
    content: "";
    width: 100%;
    height: 100%;
    top: 61px;
    left: 0;
    transform-origin: top right;
    transform: skewY(4.33deg);
    background-color: inherit;
    z-index: 1;
  }

  .purple .purple-inner, .purple .purple-border {
    color: #FBD08B;
    font-size: 36px;
    line-height: 20px;;
    z-index: 2;
  }

  .p-2 .purple-inner {
    top: 92px;
    position: relative;
    right: -123px;
  }

  .p-2 .purple-border {
    transform: rotate(4.33deg);
    top: 98px;
    right: -13px;
    text-align: left;
  }

  .p-3 .purple-border {
    top: 97px;
    transform: rotate(4.33deg);
  }

  .p-3 .purple-inner {
    position: relative;
    left: -176px;
    top: 70px;
  }

  .purple .purple-inner {
    display: inline-block;
  }

  .p-1 .purple-inner {
    left: -176px;
  }
</style>
