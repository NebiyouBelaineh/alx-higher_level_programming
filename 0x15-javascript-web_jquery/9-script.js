$(function () {
  $.get(
    'https://hellosalut.stefanbohacek.dev/?lang=fr',
    function (response) {
      const hello = response.hello;
      $('div#hello').text(hello);
    });
});
