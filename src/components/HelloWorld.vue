<template>
  <v-container>
    <v-layout
      text-xs-center
      wrap
    >
      <v-flex xs12>
        <v-img
          :src="require('../assets/logo.png')"
          class="my-3"
          contain
          height="200"
        ></v-img>
      </v-flex>

      <v-flex mb-4>
        <h1 class="display-2 font-weight-bold mb-3">
          Welcome to MTA
        </h1>
        
      </v-flex>

      <v-flex
        mb-5
        xs12
      >
       

        <v-layout justify-center>
           <v-btn color="primary" v-bind:to="{name : 'login'}" dark large>Sign in</v-btn>

        </v-layout>
      </v-flex>

      <v-flex
        xs12
        mb-5
      >
       

        <v-layout justify-center>
          <v-btn color="error" v-bind:to="{name : 'register'}" dark large>Register</v-btn>
        </v-layout>
      </v-flex>

      <v-flex
        xs12
        mb-5
      >
        

        <v-layout justify-center>
          
        </v-layout>
      </v-flex>
    </v-layout>
  </v-container>
</template>

<script>
  export default {
    data: () => ({
      
    })
  }
</script>

<style>

</style>
