<template>
  <form  >

    <v-text-field class="wh"
      v-model="email"
      :error-messages="emailErrors"
      label="E-mail"
      required
      @input="$v.email.$touch()"
      @blur="$v.email.$touch()"
    ></v-text-field>


        <v-text-field  class="wh"
      v-model="password"
      :error-messages="passwordErrors"
      label="Password"
      required
       type="password"

    ></v-text-field>



    <v-btn class="mr-4" @click="submit">submit</v-btn>
    <v-btn @click="clear">clear</v-btn>
  </form>
</template>


<script>
  import { validationMixin } from 'vuelidate'
  import { required, maxLength, email } from 'vuelidate/lib/validators'
  import { urlApi } from '../../services/urlApiService'  
  import  store  from '../../store'

  export default {
    mixins: [validationMixin],

    validations: {
      password: { required},
      email: { required, email },

    },

    data: () => ({
      email: 'karim@template.be',
      password: 'pass',

    }),

    computed: {

      emailErrors () {
        const errors = []
        if (!this.$v.email.$dirty) return errors
        !this.$v.email.email && errors.push('Must be valid e-mail')
        !this.$v.email.required && errors.push('E-mail is required')
        return errors
      },
        passwordErrors () {
        const errors = []
        if (!this.password) errors.push('Password is required')
        return errors
      },
    },

    methods: {
      submit () {
        this.$v.$touch()

   
        fetch(`${urlApi}/auth`, {
            method: "POST",
            // credentials: "include",
            body: JSON.stringify({"username":this.email, "password":this.password}),
            // cache: "no-cache", 
            headers: new Headers({
              "content-type": "application/json"
            })
          })
          .then(res => res.json())
          .then(res => {


            if(res.access_token)
            {
              store.commit('updateJWT', res)
              this.$router.push('Secure')
            }
            else
            alert(res.description)
          })
          .catch(err => {
            console.log(err)
          })
          .finally(() => {})

      },
      clear () {
        this.$v.$reset()
        this.name = ''
        this.password = ''

      },
    },
  }
</script>

<style >
.wh input{  background-color: white
}
form{
  width: 30%;
  justify-content: center;
align-items:center;
margin:auto
}
</style>