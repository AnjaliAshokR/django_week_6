$(document).ready(function(){
    $("#signup-form").validate({
        rules:{
            first_name:{
                required:true,
                minlength:4
            },
            last_name:{
                required:true,
                minlength:4
            },
            email:{
                required:true,
                email:true
            },
            password:{
                required:true,
                minlength:6
            }
        }

    })
})

$(document).ready(function(){
    $("#login-form").validate({
        rules:{
            user_name:{
                required:true,
                minlength:4
            },
            password:{
                required:true,
                minlength:6
            }
        }
    })
})