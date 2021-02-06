$(document).ready(function(){
  TurnoffAlert();
});

function TurnoffAlert(){
  $(".alert").removeClass('show');
  $(".alert").hide();
}

function TurnonAlert(){
  $(".alert").show();
  $(".alert").addClass('show');
}

function NameCheck(){
  let full_name = $("#fullname").val();

  if(full_name == ""){
    $(".error_title").text(`Error! `);
    $(".error_message").text(`Please enter full name`);
    TurnonAlert();
    return false;
  }
  return true;
}

function EmailCheck(){
  let email_id = $("#email").val();

  if(email_id == ""){
    $(".error_title").text(`Error! `);
    $(".error_message").text(`Please enter email id`);
    TurnonAlert();
    return false;
  }
  return true;
}

function PhonenoCheck(){
  let phone_no = $("#phno").val();

  if(phone_no == ""){
    $(".error_title").text(`Error! `);
    $(".error_message").text(`Please enter phone no`);
    TurnonAlert();
    return false;
  }
  return true;
}

function Password(){
  let password = $("#password").val();

  if(password == ""){
    $(".error_title").text(`Error! `);
    $(".error_message").text(`Please password`);
    TurnonAlert();
    return false;
  }
  return true;
}

function CreateAccount(){
  let full_name = $("#fullname").val();
  let email_id = $("#email").val();
  let phone_no = $("#phno").val();
  let password = $("#password").val();
  $(".signup_btn").attr("disabled", "disabled");
  $(".button_title").hide();
  $(".fa-spinner").css("display", "block");

  $.ajax({
    url: "/user/signup/",
    method: "POST",
    data: {
      "full_name": full_name,
      "email_id": email_id,
      "phone_no": phone_no,
      "passwd": password
    },
    success: function(e){
      console.log(e);
      window.location.href = "/home2/";
    },
    error: function(e){
      console.log(e);
    }
  });
}

$(".signup_btn").on('click', function(){
  TurnoffAlert();
  if(!NameCheck())
    return false;
  if(!EmailCheck())
    return false;
  if(!PhonenoCheck())
    return false;
  if(!Password())
    return false;

  CreateAccount();
});
