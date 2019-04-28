<template>
  <v-app>
   

    
  

    <v-navigation-drawer
      v-model="drawer"
      absolute
      temporary
    >
      <v-list class="pa-1">
        <v-list-tile avatar>
          <v-list-tile-avatar>
            <img src="https://randomuser.me/api/portraits/men/85.jpg">
          </v-list-tile-avatar>

          <v-list-tile-content>
            <v-list-tile-title>MTA</v-list-tile-title>
          </v-list-tile-content>
        </v-list-tile>
      </v-list>

      <v-list class="pt-0" dense>
        <v-divider></v-divider>

        <v-list-tile
          v-for="item in items"
          :key="item.title"
          :to="item.path"
        >
          <v-list-tile-action>
            <v-icon>{{ item.icon }}</v-icon>
          </v-list-tile-action>

          <v-list-tile-content>
            <v-list-tile-title>{{ item.title }}</v-list-tile-title>
          </v-list-tile-content>
        </v-list-tile>
      </v-list>
    </v-navigation-drawer>
 


    <v-toolbar dark color="warning" app>
      <v-toolbar-title class="headline text-uppercase" >
        
        <v-toolbar-side-icon 
        @click.stop="drawer = !drawer"
      ></v-toolbar-side-icon>
      <span>MTA</span>
      
        
      </v-toolbar-title>
      
      <v-spacer></v-spacer>

     <!-- <v-btn flat v-bind:to="{name:'home'}">home</v-btn>
  
       
      <v-btn flat v-bind:to="{name:'about',params: { id:randomNumber() }}">about</v-btn>
      <v-btn flat v-bind:to="{name:'login'}">login</v-btn>-->
     
    
    </v-toolbar>

    <v-content>
      
      
      <router-view/>
    </v-content>
  </v-app>
</template>

<script>
import HelloWorld from './components/HelloWorld'

export default {
  name: 'App',
  components: {
    HelloWorld
  },
  data () {
    return {
      
      drawer: null,
        items: [
          { title: 'Home', icon: 'dashboard',path:'/' },
          { title: 'Login', icon: 'input' ,path:'/login'}
        ]
      //
      
    }
  },
}
</script>
