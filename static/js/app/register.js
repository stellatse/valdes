$(document).ready(function(){

$("#register").validate({
    rules:{
    phone:"required",
    email:{
    required:true,
    email: true
    },
    password:{
    required:true,
    minlength: 8
    },
    password_again:{
    required:true,
    equalTo: "#password"
    }
    },

    errorClass: "help-inline"

});
});