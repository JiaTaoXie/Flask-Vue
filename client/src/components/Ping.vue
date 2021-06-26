<template>
  <div class="container">
    <button type="button" class="btn btn-primary" onclick="getMessage()" >{{ msg }}</button>
  </div>
</template>

<script>
import axios from 'axios'

export default {
  name: 'Ping',
  data() {
    return {
      msg: 'Hello World2222!'
    }
  },
  methods: {
    getMessage() {
      const path = 'http://localhost:8100/ping'
      axios.get(path)
        .then((res) => {
          this.msg = res.data
        })
        .catch((error) => {
          // eslint-disable-next-line
          console.error(error)
        })
      // return '22222'
      this.msg = '222222'
    }
  },

  created() {
    // this.msg = this.getMessage()
  }
}
</script>
