<template>
  <div class="container" >
  <center>  <img alt="Vue logo" src="../assets/backendsiebawi.png">
        <h1> Witaj młody byku, wszedłeś na terytorium testowania backendu <br>
        Zachowaj spokój, otwórz kustosza i kontynuuj swoją podróż</h1>    
      <h1 v-if="username">{{username}}</h1>
        <PostFetchComponent/>

        <PostFormComponent/>
    </center>
  </div>
</template>

<script>
// @ is an alias to /src

import PostFetchComponent from '@/components/Posts/PostFetchComponent.vue'
import PostFormComponent from '@/components/Posts/PostFormComponent.vue';

export default {
  name: 'Posts',
  components: {
      PostFetchComponent,
      PostFormComponent,
  },
  data(){
    return{
      username : "" 
    }

  },
  created(){
    if(window.sessionStorage.getItem("username")){
      this.username = window.sessionStorage.getItem("username");
    }
  }

}
</script>
