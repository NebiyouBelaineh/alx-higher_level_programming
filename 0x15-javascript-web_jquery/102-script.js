$(function() {
    const url = 'https://hellosalut.stefanbohacek.dev/?lang';
    $("input#btn_translate").on("click", function() {
        const code = $("input#language_code").val();
        final_url = url + '=' + code;
        // console.log(code);
        $.get(final_url, function(response) {
            const hello = response.hello;
            $("div#hello").text(response.hello);
        });
    });
});