$(function () {
  const url = 'https://hellosalut.stefanbohacek.dev/?lang';
  $('input#btn_translate').on('click', function () {
    const code = $('input#language_code').val();
    const finalUrl = url + '=' + code;
    // console.log(code);
    $.get(finalUrl, function (response) {
      const hello = response.hello;
      $('div#hello').text(hello);
    });
  });
});
