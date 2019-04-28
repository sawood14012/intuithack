<template>
  <v-container grid-list-md text-xs-center>
       <v-flex
        xs12
        mb-5
      >
        

        <v-layout justify-center>
            <h1>Clothes</h1>
          
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
                text : 'T-shirts',
                desc: 'full sleeves or half sleeves we got all',
                image:'https://images.bewakoof.com/original/wink-new-half-sleeve-t-shirt-men-s-printed-t-shirts-197747-1538829534.jpg'
            },
            {
                name: 'Polos',
                text:'Polos',
                desc : 'for the classy ones',
                image: 'https://ae01.alicdn.com/kf/HTB18m5zSXXXXXbCXXXXq6xXFXXXP/2017-New-men-s-clothing-Brand-Polos-Mens-POLO-Shirts-slim-fit-man-Short-Sleeve-Camisas.jpg_640x640.jpg'
            },
            {
                name: 'shirts',
                text : 'shirts',
                desc: 'for the man',
                image:'https://4.imimg.com/data4/GY/AP/MY-15337359/formal-shirts-500x500.jpg'

            },
            {
                name: 'jeans',
                text : 'jeans',
                desc: 'best in class denim',
                image:'https://lsco.scene7.com/is/image/lsco/Levis/clothing/228500035-front-pdp.jpg?$grid_desktop_bottoms$',

            },
            {
                name: 'kurtas',
                text : 'kurtas',
                desc: 'best ever ethnic wear',
                image:'https://images.manyavar.com/product_images/6957/qty_30/S952642-327._WC00102-306._SHODE003-310.jpg?1548136737'

            },
            {
                name: 'hoodies',
                text : 'hoodies',
                desc: 'to hide LOL',
                image:'https://images-na.ssl-images-amazon.com/images/I/613CKZIR6nL._UX342_.jpg'

            },

            
        ]

        
      
    })
}
</script>
