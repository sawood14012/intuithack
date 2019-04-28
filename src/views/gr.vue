<template>
  <v-container grid-list-md text-xs-center>
       <v-flex
        xs12
        mb-5
      >
        

        <v-layout justify-center>
            <h1>Grocries</h1>
          
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
                text : 'fruits and veggies',
                desc: 'best ever fresh veggies',
                image:'https://www.eatthis.com/wp-content/uploads//media/images/ext/781897626/veggies-fruit.jpg'
            },
            {
                name: 'food',
                text:'spices',
                desc : 'mouth warming',
                image: 'https://storage.googleapis.com/ehimages/2017/10/30/img_833718c7b5f92ac73f93b6378da73326_1509345464515_processed_original.jpg'
            },
            {
                name: 'cl',
                text : 'staples',
                desc: 'best ever organic satples',
                image:'http://allarrivals.in/image/cache/Categories/Grocery-and-Staples-600x315.jpg'

            },
            {
                name: 'ac',
                text : 'bevrages',
                desc: 'just drink it',
                image:'https://www.organicfacts.net/wp-content/uploads/vegetablejuice.jpg',

            },
            {
                name: 'bk',
                text : 'household needs',
                desc: 'everything to keep your house good',
                image:'https://i.dailymail.co.uk/1s/2018/11/19/00/6359408-6404121-image-a-1_1542588168431.jpg'

            },
            {
                name: 'gr',
                text : 'welness',
                desc: 'to make you feel alive',
                image:'https://greencurewellness.com/assets/image/products.png'

            },

            
        ]

        
      
    })
}
</script>
