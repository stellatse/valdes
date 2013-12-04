function reg(){
    $.ajax({
           type: "POST",
           url: "/signup",
           data: $("#register").serialize(), // serializes the form's elements.
           success: function(data)
           {
               alert(data); // show response from the php script.
           }
         });
}
