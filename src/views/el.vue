<template>
  <v-container grid-list-md text-xs-center>
       <v-flex
        xs12
        mb-5
      >
        

        <v-layout justify-center>
            <h1>Electronics</h1>
          
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
                text : 'Televisions',
                desc: 'HD qwality',
                image:'https://images-na.ssl-images-amazon.com/images/I/51TFpgPBzpL._SX450_.jpg'
            },
            {
                name: 'food',
                text:'Refrigirators',
                desc : 'keep your food fresh',
                image: 'https://images-na.ssl-images-amazon.com/images/I/61SispgpBtL._SL1500_.jpg'
            },
            {
                name: 'cl',
                text : 'Air conditioners',
                desc: 'cooler than ever',
                image:'https://www.myvoltas.com/pub/media/catalog/category/SplitAC10.png'

            },
            {
                name: 'ac',
                text : 'computers',
                desc: 'the stuff that you like',
                image:'https://www.telegraph.co.uk/content/dam/recommended/2019/01/11/ASUSVivobookS15_trans_NvBQzQNjv4Bq2oUEflmHZZHjcYuvN_Gr-bVmXC2g6irFbtWDjolSHWg.png?imwidth=480',

            },
            {
                name: 'bk',
                text : 'Mobiles',
                desc: 'everything in your hands',
                image:'https://www.91-img.com/pictures/125689-v7-vivo-v9-mobile-phone-large-1.jpg'

            },
            {
                name: 'gr',
                text : 'washing machines',
                desc: 'wash everything',
                image:'https://images-na.ssl-images-amazon.com/images/I/81a3%2BQui91L._SL1500_.jpg'

            },

            
        ]

        
      
    })
}
</script>
