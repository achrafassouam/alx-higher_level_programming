/* A JS script that toggles the class of the <header> element
 * when the user clicks on the tag DIV#toggle_header
 * must use the JQuery API
*/
$('div#toggle_header').click(function () {
  $('header').toggleClass('green red');
});
