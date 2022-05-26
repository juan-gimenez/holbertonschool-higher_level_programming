$(function () {
    $.get("https://swapi-api.hbtn.io/api/films/?format=json", function (display, status) {
	if (status == 'success') {
	    let film = display.results;
	    for (let i in film) {
		$('#list_movies').append('<li>' + film[x].title + '</li>');
	    }
	}})
});
