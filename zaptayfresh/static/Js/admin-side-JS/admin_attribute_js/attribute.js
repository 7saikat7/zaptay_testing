$(document).ready(function(){
  $.ajax({
    url: "/zaptay-admin-login/attribute/get-cateory",
    method: "GET",
    dataType: "JSON",

    success: function(r){
      let html_content = `
        <option value="">Select Category</option>
      `;

      // let da = r.map((data, key)=> {
      //   console.log(data);
      // });
      // console.log(r.data);
      r.data.map((category, key) => {
          html_content+= `<option value="`+category[0]+`">`+category[1]+`</option>`
          // console.log(category, key)
      })
      $("#id_category_list").html(html_content);
      // console.log(html_content);
    },
    error: function(r){
      console.log(r);
    }
  });


  $.ajax({
    url: "/zaptay-admin-login/attribute/get-sub-cateory",
    method: "GET",
    dataType: "JSON",

    success: function(r){
      let html_content = `
        <option value="">Select Sub Category</option>
      `;
      // console.log(r.data);
      r.data.map((category, key) => {
          html_content+= `<option value="`+category[0]+`">`+category[1]+`</option>`
          // console.log(category, key)
      })
      $("#id_sub_category_list").html(html_content);
      // console.log(html_content);
    },
    error: function(r){
      console.log(r);
    }
  });

  $.ajax({
    url: "/zaptay-admin-login/attribute/get-tert-cateory",
    method: "GET",
    dataType: "JSON",

    success: function(r){
      let html_content = `
        <option value="">Select Tertiary Category</option>
      `;
      // console.log(r.data);
      r.data.map((category, key) => {
          html_content+= `<option value="`+category[0]+`">`+category[1]+`</option>`
          // console.log(category, key)
      })
      $("#id_tert_category_list").html(html_content);
      // console.log(html_content);
    },
    error: function(r){
      console.log(r);
    }
  });
});

function delete_attributes(attribute_type, attribute_name, id){
  let message = 'Confirm delete '+ attribute_type +': '+ attribute_name;
  let conf = confirm(message);
  if(conf){
    var token = $("input[name=csrfmiddlewaretoken]").val();
    console.log(attribute_type, id);

    $.ajax({
      url: "/zaptay-admin-login/attribute/delete-attributes/",
      method: "POST",
      dataType: "JSON",
      data: {
        'attribute_type': attribute_type,
        'attribute_id': id,
        'csrfmiddlewaretoken': token
      },
      success: function(r){
        console.log(r);
        if(r.response == "success"){
          return true;
        }
      },
      error: function(r){
        console.log(r);
      }
    });
    // return true;
  }
  else{
      return false;
  }
}


function show_image_modal(category_type, category_id){
  // console.log(category_type, category_id);
  $(".model_form_content").hide();
  $('#exampleModalCenter').modal('show');
  $("#exampleModalLongTitle").text(category_type);

  $.ajax({
    url: "/zaptay-admin-login/attribute/get-subcategory-details",
    method: "GET",
    data: {
      "sub_category_id": category_id,
      "category_type": category_type
    },
    success: function(e){
      // console.log(e);
      $(".model_form_content").show();
      $(".modal_loader").hide();
      $(".category_name").val(e.sub_category_name);
      $(".sub_category_id").val(e.sub_category_id);
      if(e.sub_category_image)
        $(".preview_img").html(`<img class="card-img-top" src="/media/`+e.sub_category_image+`" alt="Card image cap" style="width: 150px; height: 250px;">`);
      else
        $(".preview_img").html(``);
    },
    error: function(e){
      console.log(e);
    }
  });
}

$("#customFileLang").on("change", function(){
  let image = `<img class="card-img-top" src="`+URL.createObjectURL(event.target.files[0])+`" alt="Card image cap" style="width: 150px; height: 250px;">`;
  $(".preview_img").html(image);
  /*var file = this.files;
  console.log(file);*/
});

/*$("#attribute_image").on('submit', function(e){
  var formData = new FormData()
  var file = document.getElementById('customFileLang').files[0];
  formData.append("login_name", "731004167");
  console.log(formData);
  $.ajax({
    url: "/site-admin/attribute/subcategory-image/",
    method: "POST",
    data: file,
    contentType: false,
    ProceData: false,
    success: function(e){
      console.log(e);
    },
    error: function(e){
      console.log(e);
    }
  });
  return false;
});*/

$(".submit").on('click', function(){
  var form = new FormData();
  form.append('sub_category_image',$("#customFileLang")[0].files[0]);

  var token = $("input[name=csrfmiddlewaretoken]").val();
  form.append('csrfmiddlewaretoken',token);
  form.append('sub_category_id',$(".sub_category_id").val());
  form.append('sub_category_name',$(".category_name").val());
  form.append('sub_category_type',$("#exampleModalLongTitle").text());

  /*for (var key of form.entries()) {
    console.log(key);
  }*/

  // 'csrfmiddlewaretoken': token

  $.ajax({
    url: '/zaptay-admin-login/attribute/subcategory-image/',
    cache: false,
    contentType: false,
    processData: false,
    data: form,
    type: 'POST',
    success: function(response) {
      console.log(response);
      if(response.response == 'success')
        $(".message").text('Image upload successfull');
    },
    error: function(error) {
      console.log(error);
    }
  });
  return false;
})
