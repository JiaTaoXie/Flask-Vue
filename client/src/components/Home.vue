<template>
  <div class="container">
    <button type="button" class="btn btn-primary" onclick="getMessage()" >{{ msg }}</button>
  </div>
</template>

<script>

export default {
  name: 'Ping',
  data() {
    return {
      msg: 'to ping!'
    }
  },
  methods: {
    getMessage() {
      this.$router.push('/ping')
      this.msg = 'to ping222'
    }
  },

  created() {
    // this.msg = this.getMessage()
  }
}
</script>
