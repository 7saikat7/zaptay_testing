/* Add Offer Form */
$(document).ready(function(){

  fetch_exist_offer_product($("#offer_id").val());

  $("#search_by_id").on("keyup", function(e){
    let search_value = e.currentTarget.value;
    $(".result_data").html(``);
    if(search_value != ""){
      $(".search_result_div").show();
      $.ajax({
        url: '/site-admin/stock/search-product',
        method: "GET",
        data: {
          "search_keyword": search_value,
          'search_by': "product_id",
        },
        success: function(e){
          e.resp.map((data, key) => {
            // console.log(data);
            Search_result_div(data);
          });
        },
        error: function(e){
          console.log(e);
        }
      });
    }
    else{
      $(".search_result_div").hide();
    }
  });

  $("#search_by_name").on("keyup", function(e){
    let search_value = e.currentTarget.value;
    $(".result_data").html(``);
    if(search_value != ""){
      $(".search_result_div").show();
      $.ajax({
        url: '/site-admin/stock/search-product',
        method: "GET",
        data: {
          "search_keyword": search_value,
          'search_by': "product_name",
        },
        success: function(e){
          e.resp.map((data, key) => {
            // console.log(data);
            Search_result_div(data);
          });
        },
        error: function(e){
          console.log(e);
        }
      });
    }
    else{
      $(".search_result_div").hide();
    }
  });
});

function Search_result_div(data){
  // console.log(data);
  $(".result_data").show();
  let tertiary_category = "";
  if(data.product_tertiary_category)
    tertiary_category = data.product_tertiary_category;

  var template = `
    <a href="javascript:void(0);" class="show_product_list" onclick="return ShowProduct('`+data.product_custom_id+`');">
      <div class="col-md-1">
        <img src="/static/site_image/135x180.png" alt="" width='60px' height="80px">
      </div>
      <div class="col-md-3 search_product_details">
        <span>`+data.product_title+`</span>
      </div>
      <div class="col-md-2 search_product_details">
        <span>`+data.product_category+`</span>
      </div>
      <div class="col-md-2 search_product_details">
        <span>`+data.product_sub_category+`</span>
      </div>
      <div class="col-md-2 search_product_details">
        <span>`+tertiary_category+`</span>
      </div>
      <div class="col-md-2 search_product_details">
        <span>`+data.product_seller+`</span>
      </div>
    </a>
  `;

  $(".result_data").append(template);
}

function ShowProduct(custom_id){
  $(".result_data").hide();
  console.log(custom_id);
  $.ajax({
    url: "/site-admin/offer/search-product-batch",
    method: "GET",
    data: {
      "product_id": custom_id
    },
    success: function(e){
      // console.log(e);
      $("#show__id").val(e.product[0]);
      $("#show_name").val(e.product[1]);
    },
    error: function(e){
      console.log(e);
    }
  })
}

function add_product(){
  var product_id = $("#show__id").val();
  var offer_id = $("#offer_id").val();
  var offer_price = $("#extraPrice").val();

  if(product_id == "" || offer_id == ""){
    alert("Product choose first!");
    return false;
  }

  $.ajax({
    url: "/zaptay-admin-login/offer/insert-offer-product",
    method: "POST",
    data:{
      "product_id":product_id,
      "offer_id":offer_id,
      "offer_price":offer_price
    },
    success: function(e){
      console.log(e);
      alert('Product added successfull');
      $("#search_by_id").val();
      fetch_exist_offer_product($("#offer_id").val());
    },
    error: function(e){
      console.log(e);
    }
  });
}


function fetch_exist_offer_product(offer_id){
  // console.log(offer_id);

  $.ajax({
    url: "/zaptay-admin-login/offer/offer-product-list",
    method: "POST",
    data:{
      "offer_id":offer_id,
    },
    success: function(e){
      // console.log(e);
      exist_product_data(e.data)
    },
    error: function(e){
      console.log(e);
    }
  })
}

function exist_product_data(data){
  $("#show_product").html('');
  console.log(data);
  data.map((d, sl_no) => {
    console.log(d);
    $("#show_product").append(`
      <tr>
        <td>`+d.product_id+`</td>
        <td>`+d.product_name+`</td>
        <td>
          <button type="button" class="close" aria-label="Close" onclick="return DeleteProduct('`+d.offer_pro_id+`');">
            <span aria-hidden="true">&times;</span>
          </button>
        </td>
      </tr>
    `);
  });
}


function CheckField(){
  let offer_title = $("#offer_title").val();
  let offer_start = $("#start_time").val();
  let offer_end = $("#end_time").val();

  if(offer_title == "" || offer_start == "" || offer_end == ""){
    $("#show_error").text(`All fields mentetory`);
    return false;
  }
  return true;
}

/* Add Offer Form End */
