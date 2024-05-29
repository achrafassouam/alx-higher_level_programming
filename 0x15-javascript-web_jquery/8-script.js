/* A JS script that fetches and lists the title for all movies from a URL
 * must be displayed in the HTML tag UL#list_movies
 * must use the JQuery API
*/

$.getJSON('https://swapi-api.alx-tools.com/api/films/?format=json', function (data) {
  $.each(data.results, function (i, movie) {
    $('ul#list_movies').append('<li>' + movie.title + '</li>');
  });
});
