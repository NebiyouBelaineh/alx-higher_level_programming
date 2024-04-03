$(function () {
  $.get(
    'https://swapi-api.alx-tools.com/api/films/?format=json',
    function (response) {
	    const results = response.results;
	    results.forEach(element => {
        $('ul#list_movies').append('<li>' + element.title + '</li>');
      });
    });
});
