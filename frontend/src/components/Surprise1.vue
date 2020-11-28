<template>
  <div v-show="value">
    <div class="container_surprise">
      <div class="titulo">TUESDAY - December 1st 2020</div>
      <hr />
      <div class="mensaje">
        Welcome to Ana’s advent’s calendar! 
        <br><br>
        2020 has been a b**ch for most of
        us, so I thought I would try to end it on a bright key. 
        <br><br>
        I decided to make my advents calendar digital and
        share it with anyone who wants to read! 
        <br><br>
        (Yeah ok, also I needed a
        project for coding school) 
      <br><br>
        For day 1: The dumbest Covid-Christmas parody I
        could find online
      </div>
      <div>
        <iframe
          width="300"
          src="https://www.youtube.com/embed/hX8MLmOjclA"
          frameborder="0"
          allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture"
          allowfullscreen
        ></iframe>
      </div>

      <div @click.prevent="close" class="back_button">CLOSE</div>
    </div>
  </div>
</template>

<script>
export default {
  name: "Surprise1",
   props: {
    value: {
      required: true,
    },
     methods: {

    close() {
      this.$emit("input", !this.value);
    },
  },
  },
};

</script>

<!-- Add "scoped" attribute to limit CSS to this component only -->
<style scoped>
.foto {
  height: 400px;
}
</style>
