<template>
  <div>
    <b-form inline>
      <div>
      <label class="sr-only" for="inlineFormInputName2">Name</label>
      <b-input class="mb-2 mr-sm-2 mb-sm-0" id="inlineFormInputName2" v-model="episodes"  />
      <b-input class="mb-2 mr-sm-2 mb-sm-0" id="inlineFormInputName2" v-model="result"  />
      <b-button variant="primary" v-on:click="login">콘솔 확인</b-button>
      </div>
    </b-form>
    <b-form inline>
      <div>
      <b-input class="mb-2 mr-sm-2 mb-sm-0" id="inlineFormInputName2" v-model="x"  />
      <b-input class="mb-2 mr-sm-2 mb-sm-0" id="inlineFormInputName2" v-model="y"  />
      <b-button variant="primary" v-on:click="post">콘솔 확인</b-button>
      </div>
    </b-form>
    <b-form inline>
      <div>
      <!-- <b-input class="mb-2 mr-sm-2 mb-sm-0" id="inlineFormInputName2" v-model="before"  /> -->
      <textarea cols="40" rows="10" autofocus required wrap="hard" v-model="before">??</textarea>
      <b-button variant="primary" v-on:click="trans">콘솔 확인</b-button>
      <div>{{after}}</div>
      </div>
    </b-form>
  </div>
</template>

<script>
import common from '../http_common'
// import axios from 'axios'
export default {
  name: 'Login',
  data () {
    return {
      episodes: '',
      result: '',
      x: '',
      y: '',
      before: '',
      after: '',
      credentials: {
        username: '',
        password: ''
      },
      error_msg: ''
    }
  },
  methods: {
    post: function () {
      common.post('/post', this.x)
        .then((res) => {
          this.y = res.data
        })
    },
    trans: function () {
      common.post('/trans', this.before)
        .then((res) => {
          this.after = res.data
        })
    },
    login: function () {
      common.get('/click')
        .then((res) => {
          this.result = res.data
        })
        .catch((error) => {
          // eslint-disable-next-line
          console.error(error);
        })
    },
    getEps () {
      common.get('/parse')
        .then((res) => {
          this.episodes = res.data
        })
        .catch((error) => {
          // eslint-disable-next-line
          console.error(error);
        })
    }
  },
  created () {
    this.getEps()
  }
}
</script>

<style scoped>

</style>
