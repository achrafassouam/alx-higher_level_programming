/* script that updates the text color of the <header> element to red (#FF0000):
 * must use document.querySelector to select the HTML
 * can’t use the jQuery API
 * script must be imported from the <head> tag, not at the end of the HTML
 */

document.addEventListener('DOMContentLoaded', function () {
  document.querySelector('header').style.color = '#FF0000';
});
