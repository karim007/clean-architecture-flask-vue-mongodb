
<template>
  <v-app>
    <NavBar />
    <v-content >
        <v-container id="container" fluid>
          <router-view>
            
          </router-view>
        </v-container>
    </v-content>
    <Footer/>
  </v-app>
</template>

<style >
 #container {
  background-color: black;
  margin-top: 2px;
  margin-bottom: 1px
 }

</style>
<script>
import NavBar from './components/menu/NavBar';
import Footer from './components/menu/Footer';


  export default {
      components: {
    NavBar, Footer
  }

  }

</script>
