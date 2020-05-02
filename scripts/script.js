$(window).on('focus', function () {
    console.log("hello");
});

$(window).on('blur', function () {
    console.log("nani");
    $("#main").append("<div id='dead'><em>your tree dead bro</em></div>");
});