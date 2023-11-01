$(document).ready(function() {
  $("#btn_translate").click(function() {
    // Send a POST request to the API with the language code
    $.post('https://www.fourtonfish.com/hellosalut/hello/', { lang: $("#language_code").val() }, function(data) {
      // Display the translation in the HTML tag DIV#hello
      $("#hello").text(data.hello);
    });
  });
});

