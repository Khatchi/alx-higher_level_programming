$(document).ready(function() {
  $("#add_item").click(function() {
    // Create a new <li> element with the text "Item"
    $("<li>Item</li>").appendTo("ul.my_list");
  });
});

