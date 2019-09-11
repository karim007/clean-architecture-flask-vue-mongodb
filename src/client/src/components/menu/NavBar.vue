<template>
  <div>


    <v-toolbar
      :extended="extended"
      :prominent="prominent"
      :dense="dense"
      :collapse="collapse"
      :flat="flat"
      :src="bg ? 'https://cdn.vuetifyjs.com/images/backgrounds/vbanner.jpg' : undefined"
      :extension-height="extensionHeight"
    >
 <v-img
                    src="../../assets/logo.jpg"
                    aspect-ratio="1"
                    class="grey lighten-2 "
                    max-width="50"
                    max-height="50"
                    ></v-img>    


      <v-toolbar-title>
                 
                <router-link class="" to="/">
                    BJJ App
                </router-link> 

</v-toolbar-title>

      <div class="flex-grow-1"></div>

      <v-toolbar-items>
          <v-btn text>            
            <router-link to="/Search">Search</router-link> 
</v-btn>        
  
                          <v-btn text>            
            <router-link to="/Secure">Secure Tab</router-link> 
</v-btn>   
          <v-btn text>            
        <v-btn v-if="isAuthenticated" @click="logOut()" text>LogOut</v-btn>
</v-btn>      
      </v-toolbar-items>

      <template v-if="$vuetify.breakpoint.smAndUp">
        <v-btn icon>
          <v-icon>mdi-export-variant</v-icon>
        </v-btn>
        <v-btn icon>
          <v-icon>mdi-delete-circle</v-icon>
        </v-btn>
        <v-btn icon>
          <v-icon>mdi-plus-circle</v-icon>
        </v-btn>
      </template>
    </v-toolbar>
  </div>
</template>
<script>
import store from '../../store'
  export default {
    data: () => ({
      extended: false,
      extendedSlot: false,
      prominent: false,
      dense: false,
      collapse: false,
      flat: false,
      bg: false,
      extensionHeight: 48,
    }),
    methods:{
      logOut(){
          store.commit('updateJWT', null)
          this.$router.push('/Search')

      }
    },
    computed:{
      isAuthenticated(){
        console.log(!!store.getters.res, "res")

        return !!store.getters.res
      }
    }
  }
</script>