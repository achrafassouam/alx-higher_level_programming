/* A JS script that fetches the character name from a URL
 * must be displayed in the HTML tag DIV#character
 * must use the JQuery API
*/

$.getJSON('https://swapi-api.alx-tools.com/api/people/5/?format=json', function (data) {
  $('div#character').text(data.name);
});
