$(document).ready(function(){
  $(".login").on('click', function(){
    $(".my_login_modal_div").css("display", "flex");
  });

  $(".login_close").on("click", function(){
    $(".my_login_modal_div").css("display", "none");
  });

  $(".register").on("click", function(){
    $(".my_reg_modal_div").css("display", "flex");
  });

  $(".reg_close").on("click", function(){
    $(".my_reg_modal_div").css("display", "none");
  });

  $(".error_message").hide();
  $(".login_error_message").hide();
});


/* ------------------ Check registration  ------------------------------ */
function CheckDetails(){
  $(".error_message").slideUp(200);
  let f_name = $("input[name=f_name]").val();
  let l_name = $("input[name=l_name]").val();
  let gender = $("input[name=gender]:checked").val();
  let email = $("input[name=email]").val();
  let passwd = $("input[name=pwd]").val();
  let c_passwd = $("input[name=c_pwd]").val();

  /*if(f_name == "" || l_name == "" || email == "" || passwd == "" || c_passwd == ""){
    $(".e_message").html(`All fields are mentetory`);
    $(".error_message").slideDown(200);
    return false;
  }*/
  if(f_name == "" || l_name == ""){
    $(".e_message").html(`Enter your full name`);
    $(".error_message").slideDown(200);
    return false;
  }
  if($("input[name=gender]").prop('checked') == false){
    $(".e_message").html(`Enter your gender`);
    $(".error_message").slideDown(200);
    return false;
  }
  if(email == ""){
    $(".e_message").html(`Enter your email id`);
    $(".error_message").slideDown(200);
    return false;
  }
  if(passwd == ""){
    $(".e_message").html(`Enter your password`);
    $(".error_message").slideDown(200);
    return false;
  }
  if(c_passwd == ""){
    $(".e_message").html(`Enter your confirm password`);
    $(".error_message").slideDown(200);
    return false;
  }

  $.ajax({
    url: "/user/signup/",
    method: "POST",
    data: {
      'f_name': f_name,
      'l_name': l_name,
      'gender': gender,
      'email': email,
      'passwd': passwd
    },
    success: function(e){
      console.log(e);

      if(e.status == "Success"){
        $(".e_message").html(`Registration successfull`);
        $(".error_message").slideDown(200);
        return false;
      }
    },
    error: function(e){
      console.log("Error ", e);
    }
  })
  return false;
}
/* ------------------ Check registration end  ------------------------------ */

/* --------------------  Check login  ------------------------------------ */
function CheckLogin(){
  $(".login_error_message").slideUp(200);
  let email_id = $("input[name=email_id]").val();
  let passwd = $("input[name=password]").val();

  if(email_id == "" || passwd == ""){
    $(".login_message").html(`Enter your account details`);
    $(".login_error_message").slideDown(200);
    return false;
  }
  else{
    $.ajax({
      url: "/user/signin/",
      method: "POST",
      data: {
        "email": email_id,
        "passwd": passwd
      },
      success: function(e){
        console.log(e);
        if(e.status == "Success"){
          $(".login_message").html(`Login successfull`);
          $(".login_error_message").slideDown(200);
          location.reload();
          return false;
        }
      },
      error: function(e){
        console.log(e);
      }
    });
  }
  return false;
}
/* --------------------  Check login end  ------------------------------------ */


/* ---------------------  Add to wishlist  ----------------------------------- */
$(".add_to_wish_list").on("click", function(){
  let product_id = $("input[name=product_id]").val();
  AddItemWishlist(product_id);
});

function AddItemWishlist(product_id){
  $.ajax({
    url: "/product/add-wish-list/",
    method: "POST",
    data: {
      "product_id": product_id
    },
    success: function(e){
      console.log(e);
      if(e.status == "success"){
        alert("Item into wish list");
      }
    },
    error: function(e){
      console.log(e);
    }
  });
}

$(".add_cart").on("click", function(){
  let product_id = $("input[name=cart_product_id]").val();
  AddItemCart(product_id);
});

function AddItemCart(product_id){
  $.ajax({
    url: "/product/add-to-cart/",
    method: "POST",
    data: {
      "product_id": product_id
    },
    success: function(e){
      console.log(e);
      if(e.status == "success"){
        alert("Item into cart");
      }
    },
    error: function(e){
      console.log(e);
    }
  });
}
/* ---------------------  Add to wishlist end  ----------------------------------- */
