$.get("https://swapi-api.hbtn.io/api/people/5/?", function (display) {
    $('DIV#character').text(display.name);
});
