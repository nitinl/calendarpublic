<template>
  <div class="container_Pop">
    

    <img src="./images/x1.png" alt="cerrar" @click.prevent="$parent.closeWrongAnswerPop" class="close_button">

    <p class="mensaje">
      WRONG!
    </p>
    <div class="mensaje">{{ this.DayData.failmessage }}</div>
  </div>
</template>

<script>
export default {
  name: "WrongAnswerPopUp",
  props: ["DayData"],
  data() {
    return {
    };
  }
  
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
  z-index: 2;
  position: fixed;
  left: 35%;
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


@media only screen and (max-width: 768px) { 


.container_Pop {
  height: 30vh;
  width: 40vh;
  background-color: #8b0000;
  border-color: beige;
  border-style: solid;
  z-index: 2;
  position: fixed;
  left: 15%;
  border-radius: 16px;
}

.mensaje {
  color: rgb(233, 174, 25);
  text-justify: distribute-all-lines;
  text-align: center;
  font-size: medium;
  margin: 5px;
  font-family: 'Roboto', sans-serif;
  
  
}

}



</style>
