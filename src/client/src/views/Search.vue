<template>
  <v-parallax height="900" src="../assets/bg.jpg">
         <v-row
          align="center"
          justify="center">
          <v-col
            cols="12"
            sm="12"
            md="8">
      <v-card color="blue-grey lighten-3">
          <v-card-title class="headline grey darken-4">
            
          <div id="search" class="white--text"> Search for Techniques</div>
          </v-card-title>
          <v-card-text>
            Explore some BJJ techniques! For more information visit
            <a
              class="grey--text text--lighten-3"
              href="https://blackbeltwiki.com/"
              target="_blank"
            >this website</a>.
          </v-card-text>
          <v-card-text>
            <v-autocomplete
            
              v-model="model"
              :items="items"
              :loading="isLoading"
              :search-input.sync="search"
              color="white"
              hide-no-data
              hide-selected
              item-text="Description"
              item-value="API"
              label="Techniques"
              placeholder="Start typing to Search"
              prepend-icon="mdi-database-search"
              return-object
              
            ></v-autocomplete>
          </v-card-text>
          <v-divider></v-divider>
          <v-expand-transition>
            <v-list v-if="model" class="white lighten-3 center-text"       align="center"
          justify="center">
              <v-list-item
                v-for="(field, i) in fields"
                :key="i"
              >
                <v-list-item-content>
                  <v-list-item-title v-text="field.name"></v-list-item-title>
                     <div class="iframe" v-if='field.name==="Video description"' v-html="field.value">
                    
                    </div>
                      
                      <v-btn v-else @click="go(field.value)" text >{{field.value}}</v-btn>

                

                  <!-- <a v-else   @click="go(field.value)" ">{{field.value}}</a> -->
                </v-list-item-content>
              </v-list-item>
            </v-list>
          </v-expand-transition>
          <v-card-actions>
            <div class="flex-grow-1"></div>
            <v-btn
              :disabled="!model"
              color="grey darken-3"
              @click="model = null"
            >
              Clear
              <v-icon right>mdi-close-circle</v-icon>
            </v-btn>
          </v-card-actions>
        </v-card>
        </v-col>
        </v-row>
  </v-parallax>
</template>


<script>
import { urlApi } from '../services/urlApiService'  
  export default {
    data: () => ({
      descriptionLimit: 60,
      entries: [],
      isLoading: false,
      model: null,
      search: null,
    }),

    mounted() {

    },
    computed: {
      fields () {
        
        if (!this.model) return []
        console.log(this.model, "model")
        var data= Object.keys(this.model).filter(x=> x=="url" || x=='iframe').map(key => {
            if(key==="url") name="For more information"
            else if(key=="iframe") name="Video description"
          return {
            name,
            value: this.model[key] || 'n/a',
          }
        })
        console.log(data, "data")
      return data;
      },
      items () {
     
        return this.entries.map(entry => {
          const Description = entry.name.length > this.descriptionLimit
            ? entry.name.slice(0, this.descriptionLimit) + '...'
            : entry.name

          return Object.assign({}, entry, { Description })
        })
      },
    },
methods: {
  go(url){
    console.log(url)
        window.open(url, '_blank');
  }
},
    watch: {
      search (val) {
            // this.count = null
            // this.entries = null
        // Items have already been loaded
        if (this.items.length > 0) return

        // Items have already been requested
        if (this.isLoading) return

        this.isLoading = true

        // Lazily load input items
        fetch(`${urlApi}/filter?t=${val}`)
         .then(res => res.json())
          .then(res => {
            const {entries } = res
            this.count = entries==null?0:entries.length
            this.entries = entries
            console.log(this.count)
          })
          .catch(err => {
            console.log(err)
          })
          .finally(() => (this.isLoading = false))
      },
    },
  }
</script>

<style >
.iframe {
  position: relative;
  overflow: hidden;
  width: 50px;
  height: 300px;
}
</style>
