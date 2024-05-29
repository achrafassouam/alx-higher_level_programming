/* A JS script that fetches from https://hellosalut.stefanbohacek.dev/?lang=fr
 * must be displayed in the HTML tag DIV#hello
 * must use the JQuery API
 */
$.getJSON('https://hellosalut.stefanbohacek.dev/?lang=fr', function (data) {
  $('div#hello').text(data.hello);
});
