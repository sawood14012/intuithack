<template>
  <div class="login">
    
    
   <center>

       <v-form
    ref="form"
    class="ma-5"
    v-model="valid"
    lazy-validation
  >

    <v-text-field
      v-model="email"
      :rules="emailRules"
      label="E-mail"
      required
    ></v-text-field>

    <v-text-field v-model="password" :rules="Passwordr" type="password"  label="Password" required ></v-text-field>

  

    <v-checkbox
      v-model="checkbox"
      :rules="[v => !!v || 'You must agree to continue!']"
      label="Do you agree?"
      required
    ></v-checkbox>

    <v-btn
      :disabled="!valid"
      color="success"
      @click="validate"
    >
      Login
    </v-btn>

    <v-snackbar
      v-model="snackbar"
      :bottom="y === 'bottom'"
      :left="x === 'left'"
      :multi-line="mode === 'multi-line'"
      :right="x === 'right'"
      :timeout="timeout"
      :top="y === 'top'"
      :vertical="mode === 'vertical'"
    >
      hi!..{{ email }}
      <v-btn
        color="pink"
        flat
        @click="snackbar = false"
      >
        Close
      </v-btn>
    </v-snackbar>


  </v-form>

   <v-flex
        mb-5
        xs12
      >
       
 <h5>or sign in with google</h5>
        <v-layout justify-center>
           
           <v-btn v-bind:to="{name : 'login'}"  dark large>
             <img alt="gsignin" src="https://cdn.freebiesupply.com/logos/large/2x/google-icon-logo-png-transparent.png" height="20px" width="20px"/>
           </v-btn>

        </v-layout>
      </v-flex>
   </center>
    
    

  
  </div>
</template>
<script>
import {auth} from '/Users/sawood/vueapp/hackaman/src/components/firebaseconf'
export default {
    data: () => ({
      googleicon : 'https://cdn.freebiesupply.com/logos/large/2x/google-icon-logo-png-transparent.png',
      snackbar :false,


      valid: true,
      password: '',
      Passwordr: [
        v => !!v || 'password is required'
      ],
      email: '',
      emailRules: [
        v => !!v || 'E-mail is required',
        v => /.+@.+/.test(v) || 'E-mail must be valid'
      ],
      checkbox: false
    }),

    methods: {
      validate () {
        if (this.$refs.form.validate()) {
            let v = false
            auth.signInWithEmailAndPassword(this.email,this.password).then(
                function(user)
                {
                   v = true
                },
                function(err){
                    v=false
                    console.log(err)
                   

                }
            )
          this.snackbar = true
          this.$router.push('/goodfood')
        }
      }
    }
  }

</script>
<style lang="scss">
#about { 
  font-family: 'Avenir', Helvetica, Arial, sans-serif;
  -webkit-font-smoothing: antialiased;
  -moz-osx-font-smoothing: grayscale;
  text-align: center;
  color: #2c3e50;
  margin-top: 60px;
}

h1, h2 {
  font-weight: normal;
}

ul {
  list-style-type: none;
  padding: 0;
}

li {
  display: inline-block;
  margin: 0 10px;
}

a {
  color: #42b983;
}
</style>
