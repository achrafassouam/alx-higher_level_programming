/* script that fetches and prints how to say “Hello” depending on the language
 * API service: https://www.fourtonfish.com/hellosalut/hello/
 * language code will be the value entered in the tag INPUT#language_code (ex: es, fr, en etc.)
 * translation must be fetched when the user clicks on INPUT#btn_translate
 * OR presses ENTER when the focus is on INPUT#language_code
 * must use the JQuery API
 */
$('document').ready(function () {
  const url = 'https://www.fourtonfish.com/hellosalut/?';
  $('INPUT#btn_translate').click(function () {
    $.get(url + $.param({ lang: $('INPUT#language_code').val() }), function (data) {
      $('DIV#hello').html(data.hello);
    });
  });
  $('INPUT#language_code').keypress(function (e) {
    if (e.which === 13) {
      $.get(url + $.param({ lang: $('INPUT#language_code').val() }), function (data) {
        $('DIV#hello').html(data.hello);
      });
    }
  });
});
