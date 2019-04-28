<template>
  <v-container grid-list-md text-xs-center>
       <v-flex
        xs12
        mb-5
      >
        

        <v-layout justify-center>
            <h1>Books</h1>
          
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
                text : 'comics',
                desc: 'best comics in town',
                image:'https://images-na.ssl-images-amazon.com/images/S/cmx-images-prod/Item/489866/Previews/6394ce2197d1f123d6cfac092d023a34._SX1280_QL80_TTD_.jpg'
            },
            {
                name: 'food',
                text:'story books',
                desc : 'mind blowing stories',
                image: 'https://3.imimg.com/data3/FA/EQ/MY-2507275/children-english-story-books-500x500.jpg'
            },
            {
                name: 'cl',
                text : 'acdemic books',
                desc: 'wide range of text books',
                image:'https://m.media-amazon.com/images/I/91-l2iv-4hL._SR500,500_.jpg'

            },
            {
                name: 'ac',
                text : 'stationary books',
                desc: 'to give a life to your writes',
                image:'https://5.imimg.com/data5/QN/PO/MY-49514633/classmate-books-500x500.jpeg',

            },

            
        ]

        
      
    })
}
</script>
