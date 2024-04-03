$(function() {
    const url = 'https://hellosalut.stefanbohacek.dev/?lang';
    
    function fetchTranslation() {
        const code = $("input#language_code").val();
        const final_url = url + '=' + code;
        // console.log(code);
        $.get(final_url, function(response) {
            const hello = response.hello;
            $("div#hello").text(response.hello);
        });
    }

    // Fetch translation when the user clicks the button
    $("input#btn_translate").on("click", fetchTranslation);

    // Fetch translation when the user presses ENTER in the language_code input field
    $("input#language_code").keypress(function(event) {
        if (event.which === 13) { // Check if the ENTER key is pressed
            fetchTranslation();
        }
    });
});
