$(document).ready(function(){
  console.log('ready')
});

/* ******************************************************* Image preview ******************************************************* */

$("#product_img").on('change', function(){
  let div_prepare = '';
  let count = document.getElementById("product_img").files.length;
   if (count <= 6) {
  let sl_no = 0;
  for(i=0; i<count; i++){
    sl_no = i+1;
    // console.log(event.target.files[i])
    // console.log(URL.createObjectURL(event.target.files[i]));
    // $("#show").append("<img src='"+URL.createObjectURL(event.target.files[i])+"'><br>")
    div_prepare+=`
      <div class="form-group col-12 col-md-3 mt-3   px-0 mx-0"> 
        <div class="card h-100" style="width: 7rem; background-color: transparent !important;  box-shadow: 0px 0px !important;" >
          <img   class="img-fluid card-img-top"  src="`+URL.createObjectURL(event.target.files[i])+`" alt="Responsive image Card image cap" style="height:25vh; >
         
          <div class="card-body" style="background-color: transparent !important; box-shadow: 0px 0px !important;">
            <div class="card-text"  style="background-color: transparent !important;">
               
              <br /> 
              <div class="form-group pb-0 mb-0"  style="background-color: transparent !important;box-shadow: 0px 0px !important;">
                <input type="number" class="form-control" name="product_sl_image" id="inputEmail4" value="`+sl_no+`" placeholder="Serial no.">
              </div>
            </div>
          </div>
        </div>
      </div>
    `;
  }
     $("#show_upload_image").html(div_prepare);
      }
  else {
    alert("Sorry You Cant set More Than 6 Images !");
  }
});

/* ******************************************************* /Image preview ******************************************************* */

/* ******************************************************* Image preview 2 ******************************************************* */

$("#product_img2").on('change', function(){
  var div_prepare = '';
  var count = document.getElementById("product_img2").files.length;
  console.log(count)
  if (count <= 6) {
     var sl_no = 0;
  for(i=0; i<count; i++){
    sl_no = i+1;
    // console.log(event.target.files[i])
    // console.log(URL.createObjectURL(event.target.files[i]));
    // $("#show").append("<img src='"+URL.createObjectURL(event.target.files[i])+"'><br>")
    div_prepare+=`
      <div class="form-group col-12 col-md-3 mt-3   px-0 mx-0"> 
        <div class="card h-100" style="width: 7rem; background-color: transparent !important;  box-shadow: 0px 0px !important;" >
          <img   class="img-fluid card-img-top"  src="`+URL.createObjectURL(event.target.files[i])+`" alt="Responsive image Card image cap" style="height:25vh; >
         
          <div class="card-body" style="background-color: transparent !important; box-shadow: 0px 0px !important;">
            <div class="card-text"  style="background-color: transparent !important;">
               
              <br /> 
              <div class="form-group pb-0 mb-0"  style="background-color: transparent !important;box-shadow: 0px 0px !important;">
                <input type="number" class="form-control" name="product_sl_image" id="inputEmail4" value="`+sl_no+`" placeholder="Serial no.">
              </div>
            </div>
          </div>
        </div>
      </div>
    `;
  }
  $("#show_upload_image2").html(div_prepare);
  }
  else {
    alert("Sorry You Cant set More Than 6 Images !");
  }
 
  
});

/* ******************************************************* /Image preview 2 ******************************************************* */





























 