$(document).ready(function(){
  // alert();
});


function ChangeSlider(slider_type, classname){
  $("#mens_fashion_image").hide();
  $("#womens_fashion_image").hide();
  $("#baby_kid_fashion_image").hide();
  $("#mobile_image").hide();
  $("#electronic_image").hide();
  $("#office_appliance_image").hide();
  $(".fashion_tab").removeClass('active');
  $("."+classname).addClass('active');
  $("#"+slider_type).show();
}


/*$(document).ready(function(){

  var countDownDate = new Date($(".time_left").text()).getTime();
  // Update the count down every 1 second
  var x = setInterval(function() {
    // Get today's date and time
    var now = new Date().getTime();
    // Find the distance between now and the count down date
    var distance = countDownDate - now;
    // Time calculations for days, hours, minutes and seconds
    var days = Math.floor(distance / (1000 * 60 * 60 * 24));
    var hours = Math.floor((distance % (1000 * 60 * 60 * 24)) / (1000 * 60 * 60));
    var minutes = Math.floor((distance % (1000 * 60 * 60)) / (1000 * 60));
    var seconds = Math.floor((distance % (1000 * 60)) / 1000);
    // Output the result in an element with id="demo"
    // document.getElementById("demo").innerHTML = days + "d " + hours + "h " + minutes + "m " + seconds + "s ";
    // console.log(days + "d " + hours + "h " + minutes + "m " + seconds + "s ");
    $(".time_left").html(days+` d `+hours+` : `+minutes+` : `+seconds);
    // If the count down is over, write some text
    if (distance < 0) {
      clearInterval(x);
      // document.getElementById("demo").innerHTML = "EXPIRED";
      console.log("EXPIRED");
      $(".time_left").html(`EXPIRED`);
    }
  }, 1000);
})*/

$('.exclusive_left_arrow').on("click", () => {
  document.getElementById('product_section').scrollLeft -= 600;
});

$('.exclusive_right_arrow').on("click", () => {
  document.getElementById('product_section').scrollLeft += 600;
});

$('.weekly_dreals_left_arrow').on("click", () => {
  document.getElementById('weekly_dreals_product_section').scrollLeft -= 600;
});

$('.weekly_dreals_right_arrow').on("click", () => {
  document.getElementById('weekly_dreals_product_section').scrollLeft += 600;
});

$('.featured_category_left_arrow').on("click", () => {
  document.getElementById('fetured_category_section').scrollLeft -= 600;
});

$('.featured_category_right_arrow').on("click", () => {
  document.getElementById('fetured_category_section').scrollLeft += 600;
});

 