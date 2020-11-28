<template>
  <div>
   

    <!-- This is the "wrong password" -->

    <div class="container_Pop">
      

      <p>RESPUESTA ERRÓNEA</p>

       <!-- How do I pass the props?" 
      <p>{{ this.DayData.failmessage }}</p>-->

      
      <img src="./images/x1.png" alt="cerrar" @click.prevent="$parent.closeModal" class="button_close">
    </div>
  </div>
</template>

<script>
export default {
  name: "WrongAnswerPopUp",
  props: ["DayData"],
  

};
</script>

<!-- Add "scoped" attribute to limit CSS to this component only -->
<style scoped>
.modal {
  background-color: rgba(0, 0, 0, 0.7);
}

.container_Pop {
  height: 30vh;
  width: 50vh;
  background-color: #8b0000;
  border-color: beige;
  border-style: solid;
  z-index: 1;
  position: fixed;
  left: 27.5%;
  top: 25%;
  border-radius: 16px;
}

.mensaje {
  color: rgb(233, 174, 25);
  text-justify: distribute-all-lines;
  text-align: center;
  font-size: large;
  margin: 32px;
  font-family: 'Roboto', sans-serif;
  
  
}

.close_button{
  height: 4vh;
  display: flex;
  margin-left: auto;
  margin-top: 7px;
}

</style>
