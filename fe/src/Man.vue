<template>
  <div
    :class="classYellowOrPurple"
  >
    <a :href="href">
      <div class="inner">
        <div class="name">
          {{ this.name }}
        </div>
        <div class="info" style="margin-top: 20px">
          <div>
            <p class="income">
              {{ `${this.income} Р` }}
            </p>
            <p class="region">
              Москва
            </p>
          </div>
          <div style="height: 150px; width: 115px; overflow: hidden; ">
            <img :src="this.photoUrl" height="150">
          </div>
        </div>
      </div>
    </a>
  </div>
</template>

<script>
  export default {
    name: 'Man',

    props: {
      name: {
        default: 'Жириновский Владимир Вольфович'
      },
      photoUrl: {
        default: 'https://declarator.org/media/cache/43/de/43deb2166a8c3d500277420c8d1850a1.png'
      },
      declaratorUrl: {
        default: ''
      },
      income: {
        default: 1000000
      },
      index: {
        default: -1
      },
      href: {
        default: ''
      }
    },

    computed: {
      classYellowOrPurple() {
        if (this.index % 2 === 0) {
          return 'yellow';
        }

        return 'purple';
      }
    }
  };
</script>

<style scoped>
  .yellow {
    background-color: var(--yellow);
    width: 100%;
    position: relative;
    height: 16%;
    z-index: 2;
    color: var(--purple);
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
    right: 10%;
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

  .inner .name {
    font-size: 24px;
    line-height: 20px;
    font-weight: 500;
    display: inline-block;
  }

  .yellow .region {
    font-size: 14px;
    line-height: 20px;
  }

  div {
    margin-top: 30px;
    height: 150px;
  }

  .purple {
    background-color: #7765C2;
    color: #FBD08B;
  }
</style>
