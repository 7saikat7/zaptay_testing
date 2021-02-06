$(document).ready(function(){
  // alert();
});

function ImagePreviewShow(image_section_id){
  console.log(image_section_id);
  let count = document.getElementById(image_section_id+"_banner_img").files.length;
  console.log(count);
  var prepare_div = ``;
  prepare_div+=`<div class="form-group col-md-12">Image preview</div>`;
  for(i=0; i<count; i++){
    prepare_div+=`
      <div class="form-group col-md-4">
        <div class="card" style="width: 18rem;">
          <img class="card-img-top" style="height: 110px;" src="`+URL.createObjectURL(event.target.files[i])+`" alt="Card image cap">
          <div class="card-body">
            <div class="row">
              <div class="col-md-12">
                <div class="form-group">
                  <input type="link" name="banner_link" class="form-control" id="banner_link" placeholder="Link">
                </div>
              </div>
            </div>
          </div>
        </div>
      </div>
    `
  }
  $("#"+image_section_id+"_upload_preview").html(prepare_div);
}

$("#men_banner_img").on('change', function(){
  var prepare_div = ``;
  let count = document.getElementById("men_banner_img").files.length;
  prepare_div+=`<div class="form-group col-md-12">Image preview</div>`;
  for(i=0; i<count; i++){
    prepare_div+=`
      <div class="form-group col-md-4">
        <div class="card" style="width: 18rem;">
          <img class="card-img-top" style="height: 110px;" src="`+URL.createObjectURL(event.target.files[i])+`" alt="Card image cap">
          <div class="card-body">
            <div class="row">
              <div class="col-md-12">
                <div class="form-group">
                  <input type="link" name="banner_link" class="form-control" id="banner_link" placeholder="Link">
                </div>
              </div>
            </div>
          </div>
        </div>
      </div>
    `
  }
  $("#men_upload_preview").html(prepare_div);
});

$("#women_banner_img").on('change', function(){
  var prepare_div = ``;
  let count = document.getElementById("women_banner_img").files.length;
  prepare_div+=`<div class="form-group col-md-12">Image preview</div>`;
  for(i=0; i<count; i++){
    prepare_div+=`
      <div class="form-group col-md-4">
        <div class="card" style="width: 18rem;">
          <img class="card-img-top" style="height: 110px;" src="`+URL.createObjectURL(event.target.files[i])+`" alt="Card image cap">
          <div class="card-body">
            <div class="row">
              <div class="col-md-12">
                <div class="form-group">
                  <input type="link" name="banner_link" class="form-control" id="banner_link" placeholder="Link">
                </div>
              </div>
            </div>
          </div>
        </div>
      </div>
    `
  }
  $("#women_upload_preview").html(prepare_div);
});

/*  BAby & Kids  */

$("#baby_kid_banner_img").on('change', function(){
  var prepare_div = ``;
  let count = document.getElementById("baby_kid_banner_img").files.length;
  prepare_div+=`<div class="form-group col-md-12">Image preview</div>`;
  for(i=0; i<count; i++){
    prepare_div+=`
      <div class="form-group col-md-4">
        <div class="card" style="width: 18rem;">
          <img class="card-img-top" style="height: 110px;" src="`+URL.createObjectURL(event.target.files[i])+`" alt="Card image cap">
          <div class="card-body">
            <div class="row">
              <div class="col-md-12">
                <div class="form-group">
                  <input type="link" name="banner_link" class="form-control" id="banner_link" placeholder="Link">
                </div>
              </div>
            </div>
          </div>
        </div>
      </div>
    `
  }
  $("#baby_kid_upload_preview").html(prepare_div);
});

/*  Mobile  */

$("#mobile_banner_img").on('change', function(){
  var prepare_div = ``;
  let count = document.getElementById("mobile_banner_img").files.length;
  prepare_div+=`<div class="form-group col-md-12">Image preview</div>`;
  for(i=0; i<count; i++){
    prepare_div+=`
      <div class="form-group col-md-4">
        <div class="card" style="width: 18rem;">
          <img class="card-img-top" style="height: 110px;" src="`+URL.createObjectURL(event.target.files[i])+`" alt="Card image cap">
          <div class="card-body">
            <div class="row">
              <div class="col-md-12">
                <div class="form-group">
                  <input type="link" name="banner_link" class="form-control" id="banner_link" placeholder="Link">
                </div>
              </div>
            </div>
          </div>
        </div>
      </div>
    `
  }
  $("#mobile_upload_preview").html(prepare_div);
});

/*  Electronics  */

$("#electronics_banner_img").on('change', function(){
  var prepare_div = ``;
  let count = document.getElementById("electronics_banner_img").files.length;
  prepare_div+=`<div class="form-group col-md-12">Image preview</div>`;
  for(i=0; i<count; i++){
    prepare_div+=`
      <div class="form-group col-md-4">
        <div class="card" style="width: 18rem;">
          <img class="card-img-top" style="height: 110px;" src="`+URL.createObjectURL(event.target.files[i])+`" alt="Card image cap">
          <div class="card-body">
            <div class="row">
              <div class="col-md-12">
                <div class="form-group">
                  <input type="link" name="banner_link" class="form-control" id="banner_link" placeholder="Link">
                </div>
              </div>
            </div>
          </div>
        </div>
      </div>
    `
  }
  $("#electronics_upload_preview").html(prepare_div);
});

/*  Office Appliance  */

$("#office_appliance_banner_img").on('change', function(){
  var prepare_div = ``;
  let count = document.getElementById("office_appliance_banner_img").files.length;
  prepare_div+=`<div class="form-group col-md-12">Image preview</div>`;
  for(i=0; i<count; i++){
    prepare_div+=`
      <div class="form-group col-md-4">
        <div class="card" style="width: 18rem;">
          <img class="card-img-top" style="height: 110px;" src="`+URL.createObjectURL(event.target.files[i])+`" alt="Card image cap">
          <div class="card-body">
            <div class="row">
              <div class="col-md-12">
                <div class="form-group">
                  <input type="link" name="banner_link" class="form-control" id="banner_link" placeholder="Link">
                </div>
              </div>
            </div>
          </div>
        </div>
      </div>
    `
  }
  $("#office_appliance_upload_preview").html(prepare_div);
});


/*  Home Advatice Banner 1  */

$("#advatice_banner_1_img").on('change', function(){
  var prepare_div = ``;
  let count = document.getElementById("advatice_banner_1_img").files.length;
  prepare_div+=`<div class="form-group col-md-12">Image preview</div>`;
  for(i=0; i<count; i++){
    prepare_div+=`
      <div class="form-group col-md-4">
        <div class="card" style="width: 18rem;">
          <img class="card-img-top" style="height: 110px;" src="`+URL.createObjectURL(event.target.files[i])+`" alt="Card image cap">
          <div class="card-body">
            <div class="row">
              <div class="col-md-12">
                <div class="form-group">
                  <input type="link" name="banner_link" class="form-control" id="banner_link" placeholder="Link">
                </div>
              </div>
            </div>
          </div>
        </div>
      </div>
    `
  }
  $("#advatice_banner_1_upload_preview").html(prepare_div);
});

/*  Home Advatice Banner 2  */

$("#advatice_banner_2_img").on('change', function(){
  var prepare_div = ``;
  let count = document.getElementById("advatice_banner_2_img").files.length;
  prepare_div+=`<div class="form-group col-md-12">Image preview</div>`;
  for(i=0; i<count; i++){
    prepare_div+=`
      <div class="form-group col-md-4">
        <div class="card" style="width: 18rem;">
          <img class="card-img-top" style="height: 110px;" src="`+URL.createObjectURL(event.target.files[i])+`" alt="Card image cap">
          <div class="card-body">
            <div class="row">
              <div class="col-md-12">
                <div class="form-group">
                  <input type="link" name="banner_link" class="form-control" id="banner_link" placeholder="Link">
                </div>
              </div>
            </div>
          </div>
        </div>
      </div>
    `
  }
  $("#advatice_banner_2_upload_preview").html(prepare_div);
});

/*  Home Advatice Banner 3  */

$("#advatice_banner_3_img").on('change', function(){
  var prepare_div = ``;
  let count = document.getElementById("advatice_banner_3_img").files.length;
  prepare_div+=`<div class="form-group col-md-12">Image preview</div>`;
  for(i=0; i<count; i++){
    prepare_div+=`
      <div class="form-group col-md-4">
        <div class="card" style="width: 18rem;">
          <img class="card-img-top" style="height: 110px;" src="`+URL.createObjectURL(event.target.files[i])+`" alt="Card image cap">
          <div class="card-body">
            <div class="row">
              <div class="col-md-12">
                <div class="form-group">
                  <input type="link" name="banner_link" class="form-control" id="banner_link" placeholder="Link">
                </div>
              </div>
            </div>
          </div>
        </div>
      </div>
    `
  }
  $("#advatice_banner_3_upload_preview").html(prepare_div);
});

/*  Home Advatice Banner 4  */

$("#advatice_banner_4_img").on('change', function(){
  var prepare_div = ``;
  let count = document.getElementById("advatice_banner_4_img").files.length;
  prepare_div+=`<div class="form-group col-md-12">Image preview</div>`;
  for(i=0; i<count; i++){
    prepare_div+=`
      <div class="form-group col-md-4">
        <div class="card" style="width: 18rem;">
          <img class="card-img-top" style="height: 110px;" src="`+URL.createObjectURL(event.target.files[i])+`" alt="Card image cap">
          <div class="card-body">
            <div class="row">
              <div class="col-md-12">
                <div class="form-group">
                  <input type="link" name="banner_link" class="form-control" id="banner_link" placeholder="Link">
                </div>
              </div>
            </div>
          </div>
        </div>
      </div>
    `
  }
  $("#advatice_banner_4_upload_preview").html(prepare_div);
});

/*  Home Advatice Banner 5  */

$("#advatice_banner_5_img").on('change', function(){
  var prepare_div = ``;
  let count = document.getElementById("advatice_banner_5_img").files.length;
  prepare_div+=`<div class="form-group col-md-12">Image preview</div>`;
  for(i=0; i<count; i++){
    prepare_div+=`
      <div class="form-group col-md-4">
        <div class="card" style="width: 18rem;">
          <img class="card-img-top" style="height: 110px;" src="`+URL.createObjectURL(event.target.files[i])+`" alt="Card image cap">
          <div class="card-body">
            <div class="row">
              <div class="col-md-12">
                <div class="form-group">
                  <input type="link" name="banner_link" class="form-control" id="banner_link" placeholder="Link">
                </div>
              </div>
            </div>
          </div>
        </div>
      </div>
    `
  }
  $("#advatice_banner_5_upload_preview").html(prepare_div);
});

/*  Home Advatice Banner 6  */

$("#advatice_banner_6_img").on('change', function(){
  var prepare_div = ``;
  let count = document.getElementById("advatice_banner_6_img").files.length;
  prepare_div+=`<div class="form-group col-md-12">Image preview</div>`;
  for(i=0; i<count; i++){
    prepare_div+=`
      <div class="form-group col-md-4">
        <div class="card" style="width: 18rem;">
          <img class="card-img-top" style="height: 110px;" src="`+URL.createObjectURL(event.target.files[i])+`" alt="Card image cap">
          <div class="card-body">
            <div class="row">
              <div class="col-md-12">
                <div class="form-group">
                  <input type="link" name="banner_link" class="form-control" id="banner_link" placeholder="Link">
                </div>
              </div>
            </div>
          </div>
        </div>
      </div>
    `
  }
  $("#advatice_banner_6_upload_preview").html(prepare_div);
});

/*  Home Advatice Banner Right  */

$("#advatice_banner_right_img").on('change', function(){
  var prepare_div = ``;
  let count = document.getElementById("advatice_banner_right_img").files.length;
  prepare_div+=`<div class="form-group col-md-12">Image preview</div>`;
  for(i=0; i<count; i++){
    prepare_div+=`
      <div class="form-group col-md-4">
        <div class="card" style="width: 18rem;">
          <img class="card-img-top" style="height: 110px;" src="`+URL.createObjectURL(event.target.files[i])+`" alt="Card image cap">
          <div class="card-body">
            <div class="row">
              <div class="col-md-12">
                <div class="form-group">
                  <input type="link" name="banner_link" class="form-control" id="banner_link" placeholder="Link">
                </div>
              </div>
            </div>
          </div>
        </div>
      </div>
    `
  }
  $("#advatice_banner_right_upload_preview").html(prepare_div);
});

/*  Home Advatice Banner Left  */

$("#advatice_banner_left_img").on('change', function(){
  var prepare_div = ``;
  let count = document.getElementById("advatice_banner_left_img").files.length;
  prepare_div+=`<div class="form-group col-md-12">Image preview</div>`;
  for(i=0; i<count; i++){
    prepare_div+=`
      <div class="form-group col-md-4">
        <div class="card" style="width: 18rem;">
          <img class="card-img-top" style="height: 110px;" src="`+URL.createObjectURL(event.target.files[i])+`" alt="Card image cap">
          <div class="card-body">
            <div class="row">
              <div class="col-md-12">
                <div class="form-group">
                  <input type="link" name="banner_link" class="form-control" id="banner_link" placeholder="Link">
                </div>
              </div>
            </div>
          </div>
        </div>
      </div>
    `
  }
  $("#advatice_banner_left_upload_preview").html(prepare_div);
});

/*  Header logo  */

$("#header_logo_img").on('change', function(){
  var prepare_div = ``;
  let count = document.getElementById("header_logo_img").files.length;
  prepare_div+=`<div class="form-group col-md-12">Image preview</div>`;
  for(i=0; i<count; i++){
    prepare_div+=`
      <div class="form-group col-md-4">
        <div class="card" style="width: 18rem;">
          <img class="card-img-top" style="height: 110px;" src="`+URL.createObjectURL(event.target.files[i])+`" alt="Card image cap">
          <div class="card-body">
            <div class="row">
              <div class="col-md-12">
                <div class="form-group">
                  <input type="link" name="banner_link" class="form-control" id="banner_link" placeholder="Link">
                </div>
              </div>
            </div>
          </div>
        </div>
      </div>
    `
  }
  $("#header_logo_upload_preview").html(prepare_div);
});

/*  Footer logo  */

$("#footer_logo_image").on('change', function(){
  var prepare_div = ``;
  let count = document.getElementById("footer_logo_image").files.length;
  prepare_div+=`<div class="form-group col-md-12">Image preview</div>`;
  for(i=0; i<count; i++){
    prepare_div+=`
      <div class="form-group col-md-4">
        <div class="card" style="width: 18rem;">
          <img class="card-img-top" style="height: 110px;" src="`+URL.createObjectURL(event.target.files[i])+`" alt="Card image cap">
          <div class="card-body">
            <div class="row">
              <div class="col-md-12">
                <div class="form-group">
                  <input type="link" name="banner_link" class="form-control" id="banner_link" placeholder="Link">
                </div>
              </div>
            </div>
          </div>
        </div>
      </div>
    `
  }
  $("#footer_logo_upload_preview").html(prepare_div);
});

/*  Delete Images  */
function DeleteImage(image_id="", image_custom_id=""){
  let conf = confirm(`Are you sure to delete the image (id: ${image_id})`);
  if (conf){
    /*console.log(image_custom_id, typeof(image_custom_id));
    var del_image_id = (image_custom_id=='None')? image_id : image_custom_id;
    console.log(del_image_id);*/
    $.ajax({
      url: "/zaptay-admin-login/banner/banner-delete/",
      method: "POST",
      data: {
        'image_id': image_id
      },
      success: function(e){
        console.log(e);
        if(e.status == 'success'){
          window.location.reload();
        }
      },
      error: function(e){
        console.log(e);
      }
    })
  }
}



function DeleteadImage(image_id="", image_custom_id=""){
  let conf = confirm(`Are you sure to delete the image (id: ${image_id})`);
  if (conf){
    /*console.log(image_custom_id, typeof(image_custom_id));
    var del_image_id = (image_custom_id=='None')? image_id : image_custom_id;
    console.log(del_image_id);*/
    $.ajax({
      url: "/zaptay-admin-login/banner/banner-ad-delete/",
      method: "POST",
      data: {
        'image_id': image_id
      },
      success: function(e){
        console.log(e);
        if(e.status == 'success'){
          window.location.reload();
        }
      },
      error: function(e){
        console.log(e);
      }
    })
  }
}
