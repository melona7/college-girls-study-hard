$(window).on('focus', function () {
    console.log("hello");
});

var died;
$(window).on('blur', function () {
    if(!died){
        console.log("nani");
        died = true;
        $("#main").append("<div id='dead'><em>your tree dead bro</em></div>");
    }
});