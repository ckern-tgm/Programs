<template>
  <div>
    <input id ="vname" v-model="vname" placeholder="Vorname"/>
    <input id="nname" v-model="nname" placeholder="Nachname"/>
    <button id="add" v-on:click="postUser()">Hinzufuegen</button>
    <div v-for="u in users">
      {{u.vname}}
      {{u.nname}}
    </div>
  </div>
</template>

<script>
  import axios from 'axios';
  export default {
    name: 'HelloWorld',
    data(){
      return{
       users: null,
       vname: null,
       nname: null,
      }
    },

    methods:{
      postUser(){
        const path = 'http://localhost:5000/?vname='+this.vname+'&nname='+this.nname;
        axios.post(path).then(() => {
          this.getUsers()
        })
      },


      getUsers(){
        const path = 'http://localhost:5000/'
        axios.get(path).then((res) => {
          this.users = res.data;
        }).catch((error) => {
          console.error(error)
        })
      }
    },
    created(){
      this.getUsers()
    }
  }

</script>
