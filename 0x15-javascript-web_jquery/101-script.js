/* A JS script that adds, removes and clears LI elements
 * from a list when the user clicks
 * must use the JQuery API
 */

$(document).ready(function () {
  $('#add_item').click(function () {
    $('ul.my_list').append('<li>Item</li>');
  });

  $('#remove_item').click(function () {
    $('ul.my_list li:last').remove();
  });

  $('#clear_list').click(function () {
    $('ul.my_list').empty();
  });
});
