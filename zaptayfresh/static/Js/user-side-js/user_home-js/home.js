


/* ================================   Carousel ======================================================================== */
function home() {
     $.ajax({
    type: 'GET',
    url: '/bannerjson/',
    success: function (response) {
      console.log(response.banerdata);
      var data = response.banerdata;
      var output = '';
      for (i = 0; i < data.length; i++){
        console.log(data[i].banner_image);
        if (i == 0) {
         output += '<a href="'+data[i].banner_link +'"><div class="carousel-item active"><img class="d-block w-100" src="/media/' + data[i].banner_image + '" height="300px" alt="First slide"></div></a>';
        }else {
          output += '<a href="'+data[i].banner_link +'"><div class="carousel-item  "><img class="d-block w-100" src="/media/' + data[i].banner_image + '" height="300px" alt="First slide"></div></a>';
        }
       
      }
      console.log(output)
       document.getElementById("caro").innerHTML = output;

    }
  });
 
       
}
 
function specific(banName) {


     $.ajax({
       type: 'POST',
       data: {'banname': banName},
       url: '/bannerjsonspecific/',
    success: function (response) {
      console.log(response.banerdata);
      var data = response.banerdata;
      var output = '';
      for (i = 0; i < data.length; i++){
        console.log(data[i].banner_image);
        console.log(data[i].banner_name);
        if (i == 0) {
         output += '<a href="'+data[i].banner_link +'"><div class="carousel-item active"><img class="d-block w-100" src="/media/' + data[i].banner_image + '" height="300px" alt="First slide"></div></a>';
        }else {
          output += '<a href="'+data[i].banner_link +'"><div class="carousel-item  "><img class="d-block w-100" src="/media/' + data[i].banner_image + '" height="300px" alt="First slide"></div></a>';
        }
       
      }
      console.log(output)
      document.getElementById("caro").innerHTML = output;

    }
  });
 
       
}
 


/* ================================   Carousel end ======================================================================== */