<template>
  <div>
    <b-form inline>
      <label class="sr-only" for="inlineFormInputName2">Name</label>
      <b-input class="mb-2 mr-sm-2 mb-sm-0" id="inlineFormInputName2" v-model="episodes" placeholder="coupang ldap id" />
      <b-button variant="primary" v-on:click="login">콘솔 확인</b-button>
    </b-form>
  </div>
</template>

<script>
import axios from 'axios'
export default {
  name: 'Login',
  data () {
    return {
      episodes: '',
      credentials: {
        username: '',
        password: ''
      },
      error_msg: ''
    }
  },
  methods: {
    login: function () {
      console.log(this.episodes)
    },
    getEps () {
      const path = 'http://localhost:5000/parse'
      axios.get(path)
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
