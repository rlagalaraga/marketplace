 // JavaScript function to get cookie by name
 function getCookie(name) {
    let cookieValue = null;
    if (document.cookie && document.cookie !== '') {
        const cookies = document.cookie.split(';');
        for (let i = 0; i < cookies.length; i++) {
            const cookie = cookies[i].trim();
            // Does this cookie string begin with the name we want?
            if (cookie.substring(0, name.length + 1) === (name + '=')) {
                cookieValue = decodeURIComponent(cookie.substring(name.length + 1));
                break;
            }
        }
    }
    return cookieValue;
}
const csrftoken = getCookie('csrftoken');

//Ajax Register
let namelvalCheck = false
let passvalCheck = false

$("form#regUser").submit(function(event){
    event.preventDefault()
    var email = $('input[name="email"]').val();
    var fname = $('input[name="fname"]').val();
    var lname = $('input[name="lname"]').val();
    var pass = $('input[name="password"]').val();
    var pass2 = $('input[name="password2"]').val();

    if(fname && lname && pass && email){

        valNames(fname,lname);
        valPass(pass,pass2)

        if(namelvalCheck === true && passvalCheck === true){

            $.ajax({
                type:"POST",
                url:"users/register/",
                data: {
                    'email': email,
                    'first_name': fname,
                    'last_name': lname,
                    'password': pass
                },
                beforeSend: function(xhr){
                    xhr.setRequestHeader("X-CSRFToken", csrftoken);
                },
                success:function(){
                    alert("Account Registered!")
                },
                error:function(error){
                    console.log(error.status)
                    $('#emailError').show()
                    $("#emailError").html("Email either invalid or already registered")
                }
            })

        }
    }
    else{
        $('#valError').show()
        $("#valError").html("All fields must have valid input")
    }

    //Validates names
    function valNames(fn,ln){
        let regex = /^[a-z ,.'-]+$/i
        if(fn.length>80){
            $('#fnameError').show()
            $("#fnameError").html("First Name exceeds max length please try again")
            namelvalCheck = false
            return false
        }
        if(ln.length>80){
            $('#lnameError').show()
            $("#lnameError").html("Last Name exceeds max length please try again")
            namelvalCheck = false
            return false
        }
        if(!regex.test(fn)){
            $('#fnameError').show()
            $("#fnameError").html("Invalid First Name please try again ")
            namelvalCheck = false
            return false
        }
        if(!regex.test(ln)){
            $('#lnameError').show()
            $("#lnameError").html("Invalid Last Name please try again ")
            namelvalCheck = false
            return false
        }
        $('#fnameError').hide()
        $('#lnameError').hide()
        namelvalCheck = true
        return true
     

    }

    //Validate password
    function valPass(pass1,pass2){
        if(pass1.length<8){
            $('#passError').show()
            $("#passError").html("Password should at least be 8 charachters")
            passvalCheck = false
            return false
        }
        if(pass1.length>4096){
            $('#passError').show()
            $("#passError").html("Password exceeds max length please put another password")
            passvalCheck = false
            return false
        }
        if(pass1.search(/[a-zA-Z]/) == -1){
            $('#passError').show()
            $("#passError").html("Password cannot all be numeric")
            passvalCheck = false
            return false
        }
        if(pass1!==pass2){
            $('#passError2').show()
            $("#passError2").html("Password does not match!")
            passvalCheck = false
            return false
        }
        $('#passError').hide()
        passvalCheck = true
        return true

    }

})

//Ajax Login
$("form#loginUser").submit(function(event){
    event.preventDefault()
    var email = $('input[name="email"]').val().trim();
    var pass = $('input[name="password"]').val().trim();

    if(pass && email){

        $.ajax({
            type:"POST",
            url:"users/login/",
            data: {
                'email': email,
                'password': pass
            },
            beforeSend: function(xhr, settings){
                xhr.setRequestHeader("X-CSRFToken", csrftoken);
            },
            success:function(){
                alert("Successfully Logged In")
                window.location.href = "users/"
            },
            error:function(error){
                console.log(error.status)
                $('#valError').show()
                $("#valError").html("Incorrect password or email")
            }
        })

    }
    else{
        $('#valError').show()
        $("#valError").html("All fields must have valid value")
    }
})