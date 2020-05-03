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
      dead: 0,
      alive: 0,
      users: 0,
      update: false,
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
            self.users = newPeople.length;

            for (person in newPeople){
              self.thing.push(newPeople[person]["username"]);
              console.log(person);
            }
            console.log(self.thing);
          })

      },
      checkUsers() {
        let self = this;

        axios
          .get("/api/usersonline")
          .then(function(response){
          
            let newPeople = response.data.people;
            let no = newPeople.length;
            if (no != self.users) {
              console.log("WUWWJWUWIW", no, self.users);
              self.usersonline();
             
    
            }
          })

      },
      /** 
      checkDead() {
        let self = this;

        axios
          .get("/api/trees/dead")
          .then(function(response){
          
            let newDead = response.data.people;
            let no = newPeople.length;
            if (no != self.users) {
              console.log("WUWWJWUWIW", no, self.users);
              self.usersonline();
             
    
            }
          })

      },*/

      treedie() {
        let self = this;
        self.dead += 1;
        axios
          .post("/api/trees/dead", self.dead, {headers: {
            'Content-type': 'application/x-www-form-urlencoded',
          }})
          .then(r => console.log('r: ', JSON.stringify(r, null, 2)));
          
    
          

      },
      treea() {
        let self = this;
        axios
          .get("/api/trees/alive")
          .then(function(response){
            console.log(response);
            let rooms = response.data.rooms;
            console.log(rooms);

           
            self.alive = rooms.numAlive;
    
            
    
          })

      },
      treeb() {
        let self = this;
        axios
          .get("/api/trees/dead")
          .then(function(response){
            console.log(response);
            let rooms = response.data.rooms;
            console.log(rooms);

            
            self.dead = rooms.numDead;
            console.log("dead", self.dead);
    
            
    
          })

      },
      treealive() {
        let self = this;
        self.alive += 1;
        axios
          .post("/api/trees/alive", self.dead, {headers: {
            'Content-type': 'application/x-www-form-urlencoded',
          }})
          .then(r => console.log('r: ', JSON.stringify(r, null, 2)));


      }
        
    },
    
    created: function () {
        setInterval(function(){ this.checkUsers();}.bind(this), 300);
        setInterval(function(){ this.treealive();}.bind(this), 30000);

  

        self = this;

        // if (self.update === true) {
        //   console.log("whhhhh");
        //   this.usersonline();
        //   self.update = false;
        // }

        $(window).on('blur', function () {
            self.treedie();
            self.treeb();

            if(!died){
                console.log("nani");
                died = true;
                $("#main").append("<div id='dead'><em>your tree dead bro</em></div>");

            }
        });

    },

  
    
    mounted () {
      let self = this;
      self.treea();
      self.treeb();
      self.usersonline();
      
    }
  })
  