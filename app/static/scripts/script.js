// $(window).on('focus', function () {
//     console.log("hello");
// });

// var died;
// $(window).on('blur', function () {
//     if(!died){
//         console.log("nani");
//         died = true;
//         $("#main").append("<div id='dead'><em>your tree dead bro</em></div>");
//     }
// });

var died = false;
var vue = new Vue({
    delimiters: ['[[',']]'],
    el: '#main',
    data: {
      thing: null,
    },
    methods: {
      usersonline(){
        let self = this;
        self.thing = [];

        axios
          .get("/api/usersonline")
          .then(function(response){
            console.log(response);
            let newPeople = response.data.people;
            console.log(newPeople);

            for (person in newPeople){
              self.thing.push(newPeople[person]["username"]);
              console.log(person);
            }
            console.log(self.thing);
          })

      }
        
      },
    
    created: function () {
        $(window).on('blur', function () {
            if(!died){
                console.log("nani");
                died = true;
                $("#main").append("<div id='dead'><em>your tree dead bro</em></div>");

            }
        });

    },

  
    
    mounted () {
      let self = this;
      self.usersonline();
    }
  })
  