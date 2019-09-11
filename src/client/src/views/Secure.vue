<template >
  <div>
    <br/>
    <br/>
    <br/>
    <br/>
    <br/>
    <br/>
    <br/>
    <h1 id="temp">This is an secure page {{name}}</h1>
  </div>
</template>

<style scoped>
#temp{
  color: white
}
</style>

<script>
import{urlApi} from '../services/urlApiService'
import store from '../store'
export default {
  mounted() {

          fetch(`${urlApi}/protected`, {
            method: "Get",
            headers: new Headers({
              "Authorization":store.getters.header 
            })   })
            .then(res => res.text())
            .then(r=> this.name=r)
  },
    data: () => ({
      name: '',

    }),
}
</script>