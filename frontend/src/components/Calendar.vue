<template>
  <div>
    <TooEarlyPopUp v-show="isTooEarlyPopUpOpen"></TooEarlyPopUp>
    <CalendarModal v-show="isModalOpen" :DayData="DayData" :dia="dia" :pregunta="pregunta" :respuesta="respuesta"></CalendarModal>
    

    <div class="row">

    
      
        <div @click="openModalForDay(1)" class="puerta numbers">1</div>
      
        <div @click="openModalForDay(2)" class="puerta numbers">2</div>
      
        <div @click="openModalForDay(3)" class="puerta numbers">3</div>
     
        <div @click="openModalForDay(4)" class="puerta numbers">4</div>
      
        <div @click="openModalForDay(5)" class="puerta numbers">5</div>
      
        <div @click="openModalForDay(6)" class="puerta numbers">6</div>
      
    </div>

    <div class="row">
      
        <div @click="openModalForDay(7)" class="puerta numbers">7</div>
      
        <div @click="openModalForDay(8)" class="puerta numbers">8</div>
      
        <div @click="openModalForDay(9)" class="puerta numbers">9</div>
      
        <div @click="openModalForDay(10)" class="puerta numbers">10</div>
     
        <div @click="openModalForDay(11)" class="puerta numbers">11</div>
      
        <div @click="openModalForDay(12)" class="puerta numbers">12</div>
      
    </div>

    <div class="row">
      
        <div @click="openModalForDay(13)" class="puerta numbers">13</div>
     
        <div @click="openModalForDay(14)" class="puerta numbers">14</div>
      
        <div @click="openModalForDay(15)" class="puerta numbers">15</div>
      
        <div @click="openModalForDay(16)" class="puerta numbers">16</div>
     
        <div @click="openModalForDay(17)" class="puerta numbers">17</div>
      
        <div @click="openModalForDay(18)" class="puerta numbers">18</div>
      
    </div>

    <div class="row">
      
        <div @click="openModalForDay(19)" class="puerta numbers">19</div>
     
        <div @click="openModalForDay(20)" class="puerta numbers">20</div>
      
        <div @click="openModalForDay(21)" class="puerta numbers">21</div>
      
        <div @click="openModalForDay(22)" class="puerta numbers">22</div>
    
        <div @click="openModalForDay(23)" class="puerta numbers">23</div>
     
        <div @click="openModalForDay(24)" class="puerta numbers">24</div>
     
    </div>
  </div>
</template>

<script>
//cada anio puedo cambiar el contenido del calendario cambiando sólo esta parte!
let DaysData = {
  1: {
    dateCode: "2020-12-01",
    date: "Martes 1 de diciembre 2020",
    question:
      "Cómo se llamaba el primer coche del abuelo? Ese que Jose estrelló intentando venderlo: ",
    answer: "lujoso" || "el lujoso" || "anabanana",
    successmessage: "Eres un Montalvo!",
    failmessage: "Come on... either you spelled it wrong or you have no taste for cookies",
    img_url: "#.jpg",
    dailyMessage: "Welcome to Ana’s advent’s calendar!   For day 1: The dumbest Covid-Christmas parody I could find online  ",
    audiovisual: " ",
    video:"https://www.youtube.com/embed/hX8MLmOjclA",
  },
  2: {
    dateCode: "2020-12-02",
    date: "Miércoles 2 de diciembre 2020",
    question: "Cómo llamamos en la familia al Parque Reina Sofía de Guardamar?",
    answer: "parque de los patos" || "el parque de los patos" || "parque de patos" || "anabanana",
    successmessage: "Exacto!",
    failmessage: "Yes they were! They were on a break!!!",
    img_url: "#.jpg",
    dailyMessage: "Today: A reminder that the Holidays can be celebrated with anyone you have around, not just family",
    audiovisual:" " ,
    video:"https://www.youtube.com/embed/tlYY8tCQk3c",
  },
  3: {
    dateCode: "2020-12-03",
    date: "Jueves 3 de diciembre 2020",
    question: "Cómo se llama la vecina de Raquel en Guardamar?",
    answer: "yoli" || "la yoli" || "anabanana",
    successmessage: "Efectivamente! (además quería con Carlos clarisimamente",
    failmessage: "Oh come on... try again",
    img_url: "#.jpg",
    dailyMessage: "I said no saggy mainstream Christmas videos… I lied… This one stole my heart",
    audiovisual: " ",
    video:" https://www.youtube.com/embed/V5QPXhStb5I",
  },
  4: {
    dateCode: "2020-12-04",
    date: "Viernes 4 de diciembre 2020",
    question: "Cuál es el nombre de el/la menor de la familia?",
    answer: "maría" || "anabanana",
    successmessage: "Efectivamente!",
    failmessage: "What are you... German? Try again",
    img_url: "#.jpg",
    dailyMessage: "My past self thought this is what I will want to listen to today while getting ready to start the weekend.",
    audiovisual: " ",
    video:"https://www.youtube.com/embed/gvd_rqU3lm8",
  },
  5: {
    dateCode: "2020-12-05",
    date: "Sábado 5 de diciembre 2020",
    question: "Cómo se llama la viejita de la mecedora en Guardamar? ",
    answer: "nieves"|| "anabanana",
    successmessage: "Así es! siempre con su mecedora",
    failmessage: "What is wrong with you?",
    img_url: "#.jpg",
    dailyMessage: "Sending love to anyone who is spending the Holidays away from home",
    audiovisual: " ",
    video:"https://www.youtube.com/embed/nl5YBoeKKn4 ",
  },
  6: {
    dateCode: "2020-12-06",
    date: "Domingo 6 de diciembre 2020",
    question:
      "Dónde estuvimos a punto de pasar el puente de la Hispanidad antes de que Ayuso nos confinara?",
    answer: "guardamar" || "anabanana",
    successmessage: "Eres un Montalvo!",
    failmessage: "Come on! Blair was way more human, Serena was an ice queen!",
    img_url: "#.jpg",
    dailyMessage: "You should give a fuck, you really should. But only about things that set your soul on fire . Save your fucks for magical shit. Today: For anyone who has any talent for anything",
    audiovisual: " ",
    video:" https://www.youtube.com/embed/FSCo5dZ42v8",
  },
  7: {
    dateCode: "2020-12-07",
    date: "Lunes 7 de diciembre 2020",
    question:
      "Qué app usaban Teresa y María para hacer videos? (nombre antiguo) ",
    answer: "musically" || "musicali" || "musicalli" || "anabanana",
    successmessage: "Eres un Montalvo!",
    failmessage: "Come on...",
    img_url: "#.jpg",
    dailyMessage: "Today: A little laugh for anyone who might feel lazy about starting the week. Go get a  brownie to go with that coffee, you deserve it, it’s Monday",
    audiovisual: " ",
    video:" https://www.youtube.com/embed/b2cVkHJmhtw",
  },
  8: {
    dateCode: "2020-12-08",
    date: "Martes 8 de diciembre 2020",
    question: "De los hermanos Montalvo Sánchez, quién canta peor? ",
    answer: "jose" || "tio jose" || "el tio jose" || "anabanana",
    successmessage: "Obviamente",
    failmessage: "I know it's not an easy decision... but you still got it wrong",
    img_url: "#.jpg",
    dailyMessage: "This video made me think: sure, this year has been bad, but not as bad as that school talent show was for the brunette in Mean Girls",
    audiovisual: " ",
    video:" https://www.youtube.com/embed/h81UOjlFmMs",
  },
  9: {
    dateCode: "2020-12-09",
    date: "Miércoles 9 de diciembre 2020",
    question: "Quién tiene el pelo más largo en la familia? ",
    answer: "raquel" || "anabanana",
    successmessage: "Aunque Teresa se va acercando...",
    failmessage: "You are clearly a robot... no one likes Pepsi",
    img_url: "#.jpg",
    dailyMessage: " If you are able to make today better for someone, do it we all deserve a bit of extra love this time of the year!  ",
    audiovisual: " ",
    video:"https://www.youtube.com/embed/r9D-uvKih_k",
  },
  10: {
    dateCode: "2020-12-10",
    date: "Jueves 10 de diciembre 2020",
    question: "Color del coche de Santiago ",
    answer: "azul" || "cian" || "cyan" || "anabanana",
    successmessage: "Esta era fácil",
    failmessage: "007 is not meant to sweat. Try again",
    img_url: "#.jpg",
    dailyMessage: " When life shuts a door, open it again it's a door that is how they work",
    audiovisual: " ",
    video:"https://www.youtube.com/embed/eo9sUiS4Z-g",
  },
  11: {
    dateCode: "2020-12-11",
    date: "Viernes 11 de diciembre 2020",
    question: "De qué color es el caballo blanco de Santiago?",
    answer:
      "blanco" ||
      "marron porque se cayo a un charco" ||
      "marrón porque se cayó a un charco" || "anabanana",
    successmessage: "qué tontá, pero no me resistí",
    failmessage: "only one word",
    img_url: "#.jpg",
    dailyMessage: "A cute video to remind us all to stay glamorous (so put on that pearl necklace, I am sure it matches your pajamas).",
    audiovisual: " ",
    video:"https://www.youtube.com/embed/6bbuBubZ1yE",
  },
  12: {
    dateCode: "2020-12-12",
    date: "Sábado 12 de diciembre 2020",
    question: "Quién esta aprendiendo a tocar la guitarra?  ",
    answer: "maría" || "maria" || "anabanana",
    successmessage: "estas navidades nos tocará un villancico o algo no?",
    failmessage: "only one word",
    img_url: "#.jpg",
    dailyMessage: "Somedays I wake up feeling like Santa and some days I wake up feeling like the Grinch. For the second kind of days, here is a parody of Christmas and of every value the Holidays stand for",
    audiovisual: " ",
    video:" https://www.youtube.com/embed/U3P_uNXGPwk",
  },
  13: {
    dateCode: "2020-12-13",
    date: "Domingo 13 de diciembre 2020",
    question: "De los hermanos Montalvo Sánchez; quién es el/la mayor?  ",
    answer: "jose" || "tio jose" || "anabanana",
    successmessage: "Esta era fácil",
    failmessage: "WHAT IS WRONG WITH YOU???",
    img_url: "#.jpg",
    dailyMessage: "Yes you may still have a long way to go, but today take a break to acknowledge how far you've come",
    audiovisual: " ",
    video:"https://www.youtube.com/embed/1jyUtnvZg80",
  },
  14: {
    dateCode: "2020-12-14",
    date: "Lunes 14 de diciembre 2020",
    question: "De qué color son las paredes de la habitación de Raquel? ",
    answer: "rosa" ||  "anabanana",
    successmessage: "Esta era fácil",
    failmessage: "I hope no one will ever read this message... who would pick Digimon?",
    img_url: "#.jpg",
    dailyMessage: "Whatever you are doing today, do it with the confidence of a 4-year-old in a Batman suit. Today: I will give you the soundtrack to get the week started in a high note. Keeping it high is up to you",
    audiovisual: " ",
    video:" https://www.youtube.com/embed/J-8VCL4uSUc ",
  },
  15: {
    dateCode: "2020-12-15",
    date: "Martes 15 de diciembre 2020",
    question: "Qué artefacto de cocina colecciona la tia Marisú? ",
    answer: "cafetera" || "cafeteras" || "anabanana",
    successmessage: "I might",
    failmessage: "Ok, I might be partial here...",
    img_url: "#.jpg",
    dailyMessage: "Today: the most disrespectful Christmas Parody so far (sorry ahead to any native English speakers, the swearing might sound harsher to you)",
    audiovisual: " ",
    video:"https://www.youtube.com/embed/BjbeOa4uKik",
  },
  16: {
    dateCode: "2020-12-16",
    date: "Miércoles 16 de diciembre 2020",
    question:
      "Qué persona en la familia tiene dos cuentas de instagram, una de ellas privada y una pública ",
    answer: "teresa" || "ana" || "anabanana",
    successmessage: "Esta era fácil",
    failmessage: "Road Runner, said no one ever",
    img_url: "#.jpg",
    dailyMessage: "You already have what it takes . Today: A reminder to go out in the world and share your talent, whatever your talent might be",
    audiovisual: " ",
    video:"https://www.youtube.com/embed/afpq-KHvo9I",
  },
  17: {
    dateCode: "2020-12-17",
    date: "Jueves 17 de diciembre 2020",
    question:
      "Qué animal tuvo como mascota la tía Marisú? (Pista: no duró mucho) ",
    answer: "pez" || "anabanana",
    successmessage: "No duró mucho no?",
    failmessage: "I know this one was not easy... still...",
    img_url: "#.jpg",
    dailyMessage: "If there are any children/young students reading this: Classes must be almost over! Good luck with the last exams of the year!",
    audiovisual: " ",
    video:"https://www.youtube.com/embed/w8vxuZ3bjrA ",
  },
  18: {
    dateCode: "2020-12-18",
    date: "Viernes 18 de diciembre 2020",
    question: "Quién pinta camisetas y ropita de bebé en la famlia?",
    answer: "carolina" || "carol" || "caroli" || "carola" || "anabanana",
    successmessage: "Y le quedan preciosas oye!",
    failmessage: "Go open the first Harry Potter book NOW",
    img_url: "#.jpg",
    dailyMessage: " Lower expectations, relax, enjoy. Today: A reminder not to put toooooo much meaning into Christmas traditions and presents. ",
    audiovisual: " ",
    video:"https://www.youtube.com/embed/ecWqzWaBFrc",
  },
  19: {
    dateCode: "2020-12-19",
    date: "Sábado 19 de diciembre 2020",
    question: "Quién se cree el más guapo Y HUMILDE de la familia? ",
    answer: "carlos" || "anabanana",
    successmessage: "jajaja, Flipado...",
    failmessage: "Oh come on!",
    img_url: "#.jpg",
    dailyMessage: "This song might be meant for children, but what the heck, they do enjoy         the Holidays more than the rest of mortals.",
    audiovisual: " ",
    video:"https://www.youtube.com/embed/QbnB5npEc7g",
  },
  20: {
    dateCode: "2020-12-20",
    date: "Domingo 20 de diciembre 2020",
    question: "Dónde fueron de viaje de novios Bego y Juanan? ",
    answer: "cuba" || "anabanana",
    successmessage: "habéis tenido que pedir ayuda para contestar esta?",
    failmessage: "Go rent Casablanca please",
    img_url: "#.jpg",
    
    dailyMessage: "This is the sign you were looking for to rent Love Actually and spend the afternoon drinking hot chocolate and indulging into the Christmas spirit",
    audiovisual: " ",
    video:"https://www.youtube.com/embed/zcgxBHBsl-4",
  },

  21: {
    dateCode: "2020-12-21",
    date: "Lunes 21 de diciembre 2020",
    question: "Medio de transporte favorito de Santiago",
    answer: "bicicleta" || "bici" || "anabanana",
    successmessage: "Obvio",
    failmessage: "Freak... try again",
    img_url: "#.jpg",
    dailyMessage: "I was researching for international/intercultural traditions for the Holidays. I loved it",
    audiovisual: " ",
    video:"https://www.youtube.com/embed/BBcsBFAIc-k",
  },
  22: {
    dateCode: "2020-12-22",
    date: "Martes 22 de diciembre 2020",
    question: "Quién cumple años hoy?",
    answer: "ana" || "anabanana",
    successmessage: "Siii! 29 de nada...",
    failmessage: "Oh come on... CAT; the answer is CAT",
    img_url: "#.jpg",
    dailyMessage: "It is my birthday today and this is what I want to watch when I wake up.",
    audiovisual: " ",
    video:"https://www.youtube.com/embed/GqOvxbFLwjY",
  },
  23: {
    dateCode: "2020-12-23",
    date: "Miércoles 23 de diciembre 2020",
    question: "Quién aspiraba a ser presidente?",
    answer: "carlos" || "anabanana",
    successmessage: "yo le hubiese votado!",
    failmessage: "Not if you are drinking it with me",
    img_url: "#.jpg",
    dailyMessage: "Today: A short Medley that hopefully cheers up your day! ",
    audiovisual: " ",
    video:"https://www.youtube.com/embed/Evt3PWx57WY ",
  },
  24: {
    dateCode: "2020-12-24",
    date: "Jueves 24 de diciembre 2020",
    question: "Feliz Navidad, Feliz Navidad, próspero año y .... ",
    answer: "felicidad" ,
    successmessage: "Felices fiestas a todos!",
    failmessage: "How do you dare...",
    img_url: "#.jpg",
    dailyMessage: "You were probably wondering when was this video going to come up... There you go! enjoy!",
    audiovisual: " ",
    video:"https://www.youtube.com/embed/pLg9I4E2x7o ",
  },
};

import Surprise1 from "./Surprise1";
import CalendarModal from "./CalendarModal";
import TooEarlyPopUp from "./TooEarlyPopUp";
import axios from "axios";

export default {
  name: "Calendar",
  components: {
    Surprise1,
    CalendarModal,
    TooEarlyPopUp,
  },

  data() {
    return {
      isModalOpen: false,
      isTooEarlyPopUpOpen: false,
      dia: {},  
      pregunta: {},  
      respuesta: {},  
       
      mensaje: "",
       DayData: {},
    };
  },

  methods: {
    
 getDay(DayID) {
      axios.get('http://localhost:5000/day' + '/' + DayID).then( (response) => {
        console.log(response.data[0][1])
        this.dia = response.data[0][1]        
      });
    },

 getQuestion(DayID) {
      axios.get('http://localhost:5000/day' + '/' + DayID).then( (response) => {
        console.log(response.data[0][2])
        this.pregunta = response.data[0][2]          
      });
    }, 

getAnswer(DayID) {
      axios.get('http://localhost:5000/day' + '/' + DayID).then( (response) => {
        console.log(response.data[0][3])
        this.respuesta = response.data[0][3]          
      });
    }, 


    openTooEarlyPop() {
      this.isTooEarlyPopUpOpen = true;
    },

    closeTooEarlyPop() {
      this.isTooEarlyPopUpOpen = false;
    },

    closeModal() {
      this.isModalOpen = false;
    },

    openModalForDay(DayInteger) {
      const today = new Date();
      const date =
        today.getFullYear() +
        "-" +
        (today.getMonth() + 1) +
        "-" +
        today.getDate();

      if (date >= "this.dateData.dateCode") {
        console.log("date is fine");
            this.getDay(DayInteger);
            this.getQuestion(DayInteger);
            this.getAnswer(DayInteger);

        this.isModalOpen = true;
        this.DayData = DaysData[DayInteger];
      } else {
        console.log("too early to open");
        this.openTooEarlyPop();
      }

    },
  },

  created: function () {
            console.log('created');

    
  }
};
</script>

<!-- Add "scoped" attribute to limit CSS to this component only -->
<style scoped>

</style>
