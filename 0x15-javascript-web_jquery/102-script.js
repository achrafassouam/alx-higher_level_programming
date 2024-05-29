/* A JS script that fetches and prints how to say “Hello”
 * depending on the language
 * API service: https://www.fourtonfish.com/hellosalut/hello/
 * translation must be fetched when the user clicks on INPUT#btn_translate
 * must use the JQuery API
 */

$('document').ready(function () {
  const url = 'https://www.fourtonfish.com/hellosalut/?';
  $('INPUT#btn_translate').click(function () {
    $.get(url + $.param({ lang: $('INPUT#language_code').val() }), function (data) {
      $('DIV#hello').html(data.hello);
    });
  });
});
