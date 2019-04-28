<template>
  <v-container grid-list-md text-xs-center>
       <v-flex
        xs12
        mb-5
      >
        

        <v-layout justify-center>
            <h1>Food</h1>
          
        </v-layout>
      </v-flex>
    <v-layout row wrap>
      <v-flex v-for="i in dat" :key='i' xs6>
          <v-card >
              <v-layout>
                <v-flex xs5>
                  <v-img
                    v-bind:src=i.image
                    height="125px"
                    contain
                  ></v-img>
                </v-flex>
                <v-flex xs7>
                  <v-card-title primary-title>
                    <div>
                      <div class="headline">{{i.text}}</div>
                      <div>{{i.desc}}</div>
                      
                    </div>
                  </v-card-title>
                </v-flex>
              </v-layout>
              <v-divider light></v-divider>
            </v-card>
      </v-flex>
      <v-flex
        xs12
        mb-5
      >
        <br/>
        <v-spacer>


        </v-spacer>

        <v-layout justify-center>

             <v-btn dark
    >
      Add item
      <v-icon right dark>add</v-icon>
    </v-btn>
          
        </v-layout>
      </v-flex>

      <br/>
        <v-spacer>


        </v-spacer>

        <v-layout justify-center>

             <v-btn
      :loading="loading3"
      :disabled="loading3"
      color="blue-grey"
      class="white--text"
      @click="loader = 'loading3'"
    >
      Upload Menu
      <v-icon right dark>cloud_upload</v-icon>
    </v-btn>
          
        </v-layout>
      
      
    </v-layout>
  </v-container>
</template>
<script>
export default {
    data: () => ({
        dat:[
            {
                name: 'el',
                text : 'pizzas',
                desc: 'the 7 slices of heaven',
                image:'https://img1.cookinglight.timeinc.net/sites/default/files/styles/medium_2x/public/1523913526/sausage-and-tomato-mini-pizzas-1806-p32.jpg?itok=jbdasCb1'
            },
            {
                name: 'food',
                text:'burgers',
                desc : 'if you catch a burgler do eat a burger',
                image: 'https://www.chatelaine.com/wp-content/uploads/2017/05/Bibimbap-homemade-burgers.jpg'
            },
            {
                name: 'cl',
                text : 'hotdogs',
                desc: 'are the dogs hot',
                image:'https://media1.s-nbcnews.com/j/newscms/2017_41/1288823/giada-hot-dog-today-tease-171013_cc8ea08d065ebe92133af1c5cd1c868e.today-inline-large.jpg'

            },
            {
                name: 'ac',
                text : 'Briyani',
                desc: 'mmmmm briyani',
                image:'https://vaya.in/recipes/wp-content/uploads/2018/03/Ambur-Chicken-Biriyani.jpg',

            },
            {
                name: 'bk',
                text : 'haleem',
                desc: 'power packed-mashed chicken',
                image:'https://i1.wp.com/media.hungryforever.com/wp-content/uploads/2017/06/06205918/feature-image-haleem.jpg?resize=1075%2C605&ssl=1'

            },
            {
                name: 'gr',
                text : 'shawarma',
                desc: 'the roll which melts in mouth',
                image:'https://i.pinimg.com/originals/52/48/59/52485938a88da42e2ac0d498ce0a10e2.jpg'

            },

            
        ]

        
      
    })
}
</script>
