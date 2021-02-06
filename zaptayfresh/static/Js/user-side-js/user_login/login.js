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

function LoginId(){
  let id = $("#loginId").val();
  if(id == ""){
    $(".error_title").text(`Error! `);
    $(".error_message").text(`Please enter login id`);
    TurnonAlert();
    return false;
  }
  return true;
}

function PassWord(){
  let pwd = $("#password").val();
  if(pwd == ""){
    $(".error_title").text(`Error! `);
    $(".error_message").text(`Please enter password`);
    TurnonAlert();
    return false;
  }
  return true;
}

function CheckAccount(){
  let id = $("#loginId").val();
  let pwd = $("#password").val();

  $(".signup_btn").attr("disabled", "disabled");
  $(".button_title").hide();
  $(".fa-spinner").css("display", "block");

  $.ajax({
    url: "/user/signin/",
    method: "POST",
    data:{
      'id': id,
      'pwd': pwd,
    },
    success: function(e){
      console.log(e);
      if(e.status == 'Failed'){
        $(".error_title").text(`Login Error! `);
        $(".error_message").text(`Login details invalid`);
        TurnonAlert();
        $(".signup_btn").removeAttr("disabled");
        $(".button_title").show();
        $(".fa-spinner").css("display", "none");
        return false;
      }
      window.location.href = "/home2/";
    },
    error: function(e){
      console.log(e);
    }
  })
}

$(".login_btn").on('click', function(){
  TurnoffAlert();
  if(!LoginId())
    return false;
  if(!PassWord())
    return false;


  CheckAccount();
})
