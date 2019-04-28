<template>
    


<vs-tabs alignment="fixed" color='warning'>
      <vs-tab label="Menu">
        <div>

<v-list>
          <v-list-tile
            v-for="item in items"
            :key="item.title"
            action
            @click="gocheese"
          >
           

            <v-list-tile-content>
              <v-list-tile-title v-text="item.title"></v-list-tile-title>
            </v-list-tile-content>

             <v-list-tile-action>
            
             <v-chip v-if="item.plus" color="green" text-color="white">{{item.normval}} + {{item.pval}} </v-chip>

            <v-chip color="red" v-if="item.minus" text-color="white">{{item.normval}} - {{item.pval}}</v-chip>
             <v-chip color="primary" v-if="item.noval" text-color="white">{{item.normval}}</v-chip>

            </v-list-tile-action>
          </v-list-tile>
        </v-list>


        </div>
      </vs-tab>
      <v-spacer> </v-spacer>
      <br/>
      <vs-tab label="Trends">
        <div>
             <v-text-field
        append-icon="mic"
        class="mx-3"
        flat
        label="Search"
        v-model="search"
        prepend-inner-icon="search"
        solo-inverted
      ></v-text-field>

      <h3>Latest trends:</h3>
      <h3 v-if="searcht">{{search}}</h3>

      <br/>
      <v-spacer>

      </v-spacer>

      <v-flex 
      v-for="i in filterSearch"
      :key="i.title"
      xs12>
            <v-card 
            
            class="dark--text">
              <v-layout row>
                <v-flex xs7>
                  <v-card-title primary-title>
                    <div>
                      <div class="headline">{{i.title}}</div>
                      <div>{{i.desc}}</div>
                      <div>{{i.normval}} Rs</div>
                    </div>
                  </v-card-title>
                </v-flex>
                <v-flex xs5>
                  <v-img
                    v-bind:src=i.imag
                    height="125px"
                    contain
                  >
                    </v-img>
                </v-flex>
              </v-layout>
              

              <br/>
            </v-card>
            <br/>
          </v-flex>
        </div>
      </vs-tab>
    </vs-tabs>
</template>

<script>
  export default {
    data () {
      return {
        cheesepressed: false,
        items :[],
        search:'',
        searcht:false,
        
        items1: [
          { title: 'Aloo burger', plus:true, pval: 10, normval : 230},
          { title: 'Mexican Burger', minus:true,pval: 10, normval : 150},
          { title: 'Italian Burger', plus:true, pval: 10, normval : 200 },
          { title: 'Cheese Pizza',   minus:true,pval: 10, normval : 220},
           { title: 'Chicken Pizza', plus:true, pval: 50, normval : 200 },
            { title: 'Chicken fry',  minus:true, pval: 20, normval : 120 },
             { title: 'chicken burger', plus:true, pval: 10, normval : 150 },
              { title: 'Chcken tikka', plus:true, pval: 20, normval : 100 }
        ],
        items2: [
          { title: 'Veg Pizza', plus:true, pval: 10, normval : 230},
          { title: 'Mexican Pizza', minus:true,pval: 10, normval : 150},
          { title: 'Abc Pizza', plus:true, pval: 20, normval : 300 },
          { title: 'Cheese Pizza',   noval:true, normval : 350},
           { title: 'Chicken Pizza', plus:true, pval: 50, normval : 200 },
            { title: 'Papa john pizza',  minus:true, pval: 20, normval : 120 },
             { title: 'pizza hut', noval:true, normval : 275 },
              { title: 'Dominos pizza ', noval:true, normval : 300 },
              { title: 'farmhouse pizza ', plus:true, pval: 20, normval : 100 }
        ],
         trends: [
          { title: 'Square Pizza', desc:'timax pizza' , normval : 300, imag:'https://b.zmtcdn.com/data/pictures/8/48688/37cb24d0673b9b8065f8a1613d67e222_featured_v2.jpg'},
          { title: 'california Pizza', desc:'detrol pizzamania', normval : 250,imag:'https://www.godairyfree.org/wp-content/uploads/2008/11/resto-california-pizza-kitchen-ig.jpg'},
          { title: 'Herb pizza', desc: 'pol pizzas',normval : 400,imag:'https://4.bp.blogspot.com/-eluqUF-nKxs/U4YwDGdowUI/AAAAAAAAIyI/-id4pWkTicU/s1600/freshherbpizzalandscape.jpg' },
          {title:'candy floss',desc:'HKSK',normval:150,imag:'http://carnivalmunchies.com/wp-content/uploads/2015/09/candyfloss.jpg'},
          {title:'cookie ice cream sandwich',desc:'Aceice',normval:300,imag:'https://images-gmi-pmc.edge-generalmills.com/9b0fc8ac-11ad-46dd-a933-e7338c5f0bec.jpg'},
          {title:'Rolled icecream',desc:'Gradenia ice shop',normval:350,imag:'https://www.biggerbolderbaking.com/wp-content/uploads/2017/08/1C5A0419-1024x682.jpg'},

          
        ],


      }
    },
   created(){
    this.items = this.items1
   },
   computed:{
     filterSearch() {
      return this.trends.filter( trend => {
        //console.log(hero.nam, this.searchHero)
        this.searcht = true
        return !this.search || trend.title.toLowerCase().indexOf(this.search.toLowerCase()) > -1
      })
    }
   },


    

    methods: {
        gocheese(){
            this.items = this.items2
            //this.$router.push('/pizzas')
           // cheesepressed :true
        }
    },
  }
</script>