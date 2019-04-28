<template>
  <v-container grid-list-md text-xs-center>
       <v-flex
        xs12
        mb-5
      >
        

        <v-layout justify-center>
            <h1>Accessories</h1>
          
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
                text : 'wallets',
                desc: 'best wallets',
                image:'https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcS4T-0sK2sdG6KZM_L9CjgnGnuL1-fZI_c6Y1yqWGHpuU_QaiZ7'
            },
            {
                name: 'food',
                text:'head phones',
                desc : 'sound breaking',
                image: 'https://rukminim1.flixcart.com/image/312/312/j5r293k0/headphone/extra-bass/j/8/5/sony-mdrxb650btzbe-original-imaewd6puze6jbns.jpeg?q=70'
            },
            {
                name: 'cl',
                text : 'pendrives',
                desc: 'lighthing fast pendrives',
                image:'https://images-eu.ssl-images-amazon.com/images/G/31/Img18/DATA_STORAGE/35_32._CB496894128_.jpg'

            },
            {
                name: 'ac',
                text : 'Belts',
                desc: 'best in class leather belts',
                image:'https://images-na.ssl-images-amazon.com/images/I/71pHBQuc41L._UX385_.jpg',

            },
            {
                name: 'bk',
                text : 'power banks',
                desc: 'carry the power you  need',
                image:'https://5.imimg.com/data5/AQ/CP/MY-20343569/power-banks-500x500.png'

            },
            {
                name: 'gr',
                text : 'watches',
                desc: 'just in time',
                image:'https://images-na.ssl-images-amazon.com/images/I/61L%2BJS%2B82KL._UX569_.jpg'

            },

            
        ]

        
      
    })
}
</script>
