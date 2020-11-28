<template>
  <div id="app">
   <Container></Container>
  </div>
</template>

<script>
import Container from './components/Container'

export default {
  name: 'App',
  components: {
    Container
  }
}
</script>

<style>
#app {
  font-family: 'Avenir', Helvetica, Arial, sans-serif;
  -webkit-font-smoothing: antialiased;
  -moz-osx-font-smoothing: grayscale;
  text-align: center;
  overflow:hidden;
}

.puerta{
    height:100px;
    width:100px;
    background-color:pink;
    margin: 10px;

}




</style>
