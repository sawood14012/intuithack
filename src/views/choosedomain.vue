<template>
  <v-container grid-list-md text-xs-center>
       <v-flex
        xs12
        mb-5
      >
        

        <v-layout justify-center>
            <h1> Choose Your Domain</h1>
          
        </v-layout>
      </v-flex>
    <v-layout row wrap>
      <v-flex v-for="i in dat" :key='i' xs6>
          <v-card color="cyan darken-2" class="white--text">
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
               <v-card-actions>
                <v-btn v-bind:to="i.name" flat dark>Go</v-btn>
              </v-card-actions>
            </v-card>
      </v-flex>
      
    </v-layout>
  </v-container>
</template>
<script>
export default {
    data: () => ({
        dat:[
            {
                name: 'el',
                text : 'Electronics',
                desc: 'best electronics in town',
                image:'https://images.yourstory.com/production/document_image/mystoryimage/sqf45pwe-Save-Money-on-Home-Electronic-Appliances-Shopping.jpg?fm=png&auto=format'

            },
            {
                name: 'food',
                text:'Food',
                desc : 'tastiest food in the world',
                image: 'https://i.kinja-img.com/gawker-media/image/upload/s--vHt6tbFa--/c_scale,f_auto,fl_progressive,q_80,w_800/xjmx1csashjww8j8jwyh.jpg'
            },
            {
                name: 'cl',
                text : 'Clothes',
                desc: 'trending fashion in town',
                image:'https://i.ytimg.com/vi/-dww7OoGvc4/maxresdefault.jpg'

            },
            {
                name: 'ac',
                text : 'Accessories',
                desc: 'best in class accessories',
                image:'https://i0.wp.com/www.theunstitchd.com/wp-content/uploads/2015/08/10-Accessories-Every-Man-must-have.png?fit=960%2C499',

            },
            {
                name: 'bk',
                text : 'Books',
                desc: 'Trending reads from the best',
                image:'https://martijnscheijbeler.com/wp-content/uploads/2018/01/books.jpg'

            },
            {
                name: 'gr',
                text : 'Grocery',
                desc: 'Fresh groceries in town',
                image:'https://s3.amazonaws.com/btoimage/prism-thumbnails/articles/20171030-2048-SeafoodCity6.jpg-resize_then_crop-_frame_bg_color_FFF-h_1365-gravity_center-q_70-preserve_ratio_true-w_2048_.webp'

            },

            
        ]

        
      
    })
}
</script>
