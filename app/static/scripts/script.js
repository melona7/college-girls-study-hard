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
    el: '#main',
    data: {
      
    },
    methods: {

        
  
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
      //
    }
  })
  