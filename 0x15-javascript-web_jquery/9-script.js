$(function () {
    $.get("https://fourtonfish.com/hellosalut/?lang=fr", function (display) {
	$('#hello').text(display.hello)
    });
});
