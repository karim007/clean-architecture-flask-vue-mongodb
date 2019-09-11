<template>
      <v-parallax height="900" src="../assets/lg.jpg">
  <v-row
          align="center"
          justify="center">
          <v-col
            cols="12"
            sm="12"
            md="8">
<LoginForm/>
        </v-col>
        </v-row>
      </v-parallax>
</template>


<script>
import { urlApi } from '../services/urlApiService'  
import LoginForm  from '../components/input/LoginForm'  
  export default {
      components:{LoginForm},
    data: () => ({
 
    }),

    mounted() {

    },
    computed: {


    },
     methods : {
            handleSubmit(e){
                e.preventDefault()
                if (this.password.length > 0) {
                    fetch(`${urlApi}/authenticate`, 
                    {method:'Post', body:{
                        email: this.email,
                        password: this.password
                    }})
                   then(response => {
                        let is_admin = response.data.user.is_admin
                        localStorage.setItem('user',JSON.stringify(response.data.user))
                        localStorage.setItem('jwt',response.data.token)

                        if (localStorage.getItem('jwt') != null){
                            this.$emit('loggedIn')
                            if(this.$route.params.nextUrl != null){
                                this.$router.push(this.$route.params.nextUrl)
                            }
                            else {
                                if(is_admin== 1){
                                    this.$router.push('admin')
                                }
                                else {
                                    this.$router.push('dashboard')
                                }
                            }
                        }
                    })
                    .catch(function (error) {
                        console.error(error.response);
                    });
                }
            }
        },
    
    watch: {
      
    },
  }
</script>


