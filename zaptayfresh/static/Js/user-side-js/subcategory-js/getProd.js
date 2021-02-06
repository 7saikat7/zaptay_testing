 
  var visible = 12;





   const truncateString = (string, maxLength = 50) => {
  if (!string) return null;
  if (string.length <= maxLength) return string;
  return `${string.substring(0, maxLength)}...`;
};


function GetAllUnderTer() {
   $.ajax({
    type: 'GET',
    url: '/underTer/',
     success: function (response) {
      
      // console.log(response );
      var data = response.UndTer;
      var output = '';

      output =  output = "<div class='sub_category tertiary_category '> <div class='container-fluid '>  <div class='row'> <div class='col-md-12 shadow'> <div class='left_arrow exclusive_left_arrow'><i class='fas fa-caret-left'></i></div> <div class='right_arrow exclusive_right_arrow'><i class='fas fa-caret-right'></i></div> <div class='product_section' id='tertiary_category_product_section'>  <ul >"
     
        for (i = 0; i < data.length; i++){
        // console.log(data[i].under_tertiary_category_image);
        output += `<li><span><a href='javascript:void(0);'onclick='getProdByundtertiarycat( "${data[i].under_ter_category_id}")'><div class= 'mx-3 category_blog_design' ><div class= 'category_image' ><img class="card-hlight" src= '/media/${data[i].under_tertiary_category_image }' alt=''></div><div class='category_title'><span> ${data[i].under_ter_category_name} </span></div></div></a></span></li> `;
      }

       output +=  "</ul></div></div></div></div</div>"

      //  console.log(output);
       document.getElementById("undter").innerHTML = output; 

    }
  });
 
}








function getundTer(terid) {
 
    $.ajax({
    type: 'POST',
    data: {'id': terid},
    url: '/underTerspecific/',
   
      
     success: function (response) {
      
      console.log(response );
      var data = response.underTer;
      console.log(data.length)
      
      var output = '';
      if (data.length != 0){
      output = "<div class='sub_category tertiary_category'> <div class='container-fluid'>  <div class='row'> <div class='col-md-12'> <div class='left_arrow exclusive_left_arrow'><i class='fas fa-caret-left'></i></div> <div class='right_arrow exclusive_right_arrow'><i class='fas fa-caret-right'></i></div> <div class='product_section' id='tertiary_category_product_section'>  <ul >"

      for (i = 0; i < data.length; i++){
        console.log(data[i].under_tertiary_category_image);
        

        output += `<li><span><a href='javascript:void(0);'onclick='getProdByundtertiarycat( "${data[i].under_ter_category_id}")'><div class= 'mx-3 category_blog_design' ><div class= 'category_image' ><img class="card-hlight" src= '/media/${data[i].under_tertiary_category_image }' alt=''></div><div class='category_title'><span> ${data[i].under_ter_category_name} </span></div></div></a></span></li> `;
       
      }
      output +=  "</ul></div></div></div></div</div>"
        }
      //  console.log(output);
       document.getElementById("undter").innerHTML = output; 
    
    }
  });
}
































   function getallprod(catid,add){
   
     console.log(visible);

     if (add == '12') {
      visible += 12;
      console.log(visible);
     }
     else {
       visible = 12;
     }
     
     $.ajax({
    type: 'POST',
    data: {'id': catid, 'visible':visible},
    url: '/allprod/',
   
      
     success: function (response) {
       
      console.log(response );
      var data = response.prod;
      console.log(data)
      output = ''
       for (i = 0; i < data.length; i++){
        console.log(Math.trunc(3.3))
        output +=`  
        <div class="col-3" >

    <div class="exclusive_category_div  ">
        <div class="product_section" id="product_section">
          <ul style="background-color: transparent;">
              <li class="  text-center card-hlight ">
              <span>
                <div class="product_best_seller"><span>Best Seller</span></div>
                <div class="product_wish_list_icon"><i class="fas fa-heart"></i></div>

                <a href="/singleproduct/${data[i].prod_custom_id}">

                  <div class="product_design_div pl-1">
                    <div class="product_image" style="   height: 300px; ">
                      <img  src="/media/${data[i].product_image1}" style="width: 200px; height: 300px; " alt="">
                    </div>
                    <div class="product_description text-center text-truncate">
                      <div class="font-weight-bold h5 mt-2 text-truncate ">${truncateString(data[i].prod_title, 16)}</div>
                      <div class="product_view_rating text-center">
                        <div class="product_rating viewer text-center align-items-center" >
                          <span class="rating_text  ml-3 text-center">3.5 <i class="fas fa-star"></i> </span> <span>&nbsp;&nbsp;(15,000)</span>
                          <div>
                               <span class="text-center ml-3 mt-3 font-weight-bold">&#x20B9; ${Math.trunc(data[i].off_price)}</span>
                          <span class="original_price text-center" style="text-decoration: line-through;">&#8377; ${Math.trunc(data[i].m_price)}</span>  <span class="text-danger"> ${Math.trunc((100/data[i].m_price)*(data[i].m_price-data[i].off_price))}%</span>
                          </div>
                        </div>
                      </div>                         
                    </div>
                  </div>
                </a>
              </span>
            </li>            
          </ul>
        </div>
      </div>
    

  </div>`;

      }
       
      
        butan = `<button class="btn btn-primary font-weight-light"  onclick="getallprod('${catid}' ,'${12}')">See More</button>`;
       if (add == '12') {
           document.getElementById("pro").innerHTML += output; 
       } else {
         document.getElementById("pro").innerHTML = output; 
       }
       
       document.getElementById("butn").innerHTML = butan; 
    
    }
     });
     

      
}

  









 


function getProdByBrand(subid, brand,add) {
     if (add == '12') {
      visible += 12;
      console.log(visible);
     }
     else {
       visible = 12;
     }
     
  console.log('subid');
  
  console.log(subid);
  console.log(brand);

   $.ajax({
    type: 'POST',
     data: {
       'id': subid,
       'brand':brand, 'visible':visible
     },
    url: '/getprodbyBrand/',
   
      
     success: function (response) {
      
      console.log(response );
      var data = response.prod;
      console.log(data)
      output = ''
      for (i = 0; i < data.length; i++){
       output +=`  
        <div class="col-3" >

    <div class="exclusive_category_div  ">
        <div class="product_section" id="product_section">
          <ul style="background-color: transparent;">
              <li class="  text-center card-hlight">
              <span>
                <div class="product_best_seller"><span>Best Seller</span></div>
                <div class="product_wish_list_icon"><i class="fas fa-heart"></i></div>

                <a href="/singleproduct/${data[i].prod_custom_id}">

                  <div class="product_design_div pl-1">
                    <div class="product_image" style="width: 200px; height: 300px; ">
                      <img src="/media/${data[i].product_image1}" style="width: 200px; height: 300px; " alt="">
                    </div>
                    <div class="product_description text-center text-truncate">
                      <div class="font-weight-bold h5 mt-2 text-truncate ">${truncateString(data[i].prod_title, 16)}</div>
                      <div class="product_view_rating text-center">
                        <div class="product_rating viewer text-center align-items-center" >
                          <span class="rating_text  ml-3 text-center">3.5 <i class="fas fa-star"></i> </span> <span>&nbsp;&nbsp;(15,000)</span>
                          <div>
                               <span class="text-center ml-3 mt-3 font-weight-bold">&#x20B9; ${Math.trunc(data[i].off_price)}</span>
                          <span class="original_price text-center" style="text-decoration: line-through;">&#8377; ${Math.trunc(data[i].m_price)}</span>  <span class="text-danger"> ${Math.trunc((100/data[i].m_price)*(data[i].m_price-data[i].off_price))}%</span>
                          </div>
                        </div>
                      </div>                         
                    </div>
                  </div>
                </a>
              </span>
            </li>            
          </ul>
        </div>
      </div>
    

  </div>`;

      }
       
      
      
       butan = `<button class="btn btn-primary font-weight-light"  onclick="getProdByBrand('${subid}' ,'${brand}' ,'${12}')">See More</button>`;
       if (add == '12') {
           document.getElementById("pro").innerHTML += output; 
       } else {
         document.getElementById("pro").innerHTML = output; 
       }
       
       document.getElementById("butn").innerHTML = butan; 
    
    }
  });
  
}





function getProdBySize(subid, Size,add) {
   if (add == '12') {
      visible += 12;
      console.log(visible);
     }
     else {
       visible = 12;
     }
  console.log('subid');
  
  console.log(subid);
  console.log(Size);

   $.ajax({
    type: 'POST',
     data: {
       'id': subid,
       'siz':Size , 'visible':visible
     },
    url: '/getprodbySize/',
   
      
     success: function (response) {
      
      console.log(response );
      var data = response.prod;
       console.log(data);
       output = '';
      for (i = 0; i < data.length; i++){
        for (j = 0; j < data[i].length; j++){
       output +=`  
        <div class="col-3" >

    <div class="exclusive_category_div  ">
        <div class="product_section" id="product_section">
          <ul style="background-color: transparent;">
              <li class="  text-center card-hlight">
              <span>
                <div class="product_best_seller"><span>Best Seller</span></div>
                <div class="product_wish_list_icon"><i class="fas fa-heart"></i></div>

                <a href="/singleproduct/${data[i][j].prod_custom_id}">

                  <div class="product_design_div pl-1">
                    <div class="product_image" style="width: 200px; height: 300px; ">
                      <img src="/media/${data[i][j].product_image1}" style="width: 200px; height: 300px; " alt="">
                    </div>
                    <div class="product_description text-center text-truncate">
                      <div class="font-weight-bold h5 mt-2 text-truncate ">${truncateString(data[i][j].prod_title, 16)}</div>
                      <div class="product_view_rating text-center">
                        <div class="product_rating viewer text-center align-items-center" >
                          <span class="rating_text  ml-3 text-center">3.5 <i class="fas fa-star"></i> </span> <span>&nbsp;&nbsp;(15,000)</span>
                          <div>
                               <span class="text-center ml-3 mt-3 font-weight-bold">&#x20B9; ${Math.trunc(data[i][j].off_price)}</span>
                          <span class="original_price text-center" style="text-decoration: line-through;">&#8377; ${Math.trunc(data[i][j].m_price)}</span>  <span class="text-danger"> ${Math.trunc((100/data[i][j].m_price)*(data[i][j].m_price-data[i][j].off_price))}%</span>
                          </div>
                        </div>
                      </div>                         
                    </div>
                  </div>
                </a>
              </span>
            </li>            
          </ul>
        </div>
      </div>
    

  </div>`;
}
      }
       
      
     
      
       butan = `<button class="btn btn-primary font-weight-light"  onclick="getProdBySize('${subid}' ,'${Size}' ,'${12}')">See More</button>`;
       if (add == '12') {
           document.getElementById("pro").innerHTML += output; 
       } else {
         document.getElementById("pro").innerHTML = output; 
       }
       
       document.getElementById("butn").innerHTML = butan; 
    
    
    }
  });
  
}




 

function getProdBycolor(subid, color, add) {
   if (add == '12') {
      visible += 12;
      console.log(visible);
     }
     else {
       visible = 12;
     }
 
  console.log('color');
  
    
  console.log(subid);
  console.log(color);

   $.ajax({
    type: 'POST',
     data: {
       'id': subid,
       'col': color,
       'visible': visible
     },
    url: '/getprodbycolor/',
   
      
     success: function (response) {
      
      console.log(response );
      var data = response.prod;
      console.log(data)
      output = ''
      for (i = 0; i < data.length; i++){
       output +=`  
        <div class="col-3" >

    <div class="exclusive_category_div  ">
        <div class="product_section" id="product_section">
          <ul style="background-color: transparent;">
              <li class="  text-center card-hlight">
              <span>
                <div class="product_best_seller"><span>Best Seller</span></div>
                <div class="product_wish_list_icon"><i class="fas fa-heart"></i></div>

                <a href="/singleproduct/${data[i].prod_custom_id}">

                  <div class="product_design_div pl-1">
                    <div class="product_image" style="width: 200px; height: 300px; ">
                      <img src="/media/${data[i].product_image1}" style="width: 200px; height: 300px; " alt="">
                    </div>
                    <div class="product_description text-center text-truncate">
                      <div class="font-weight-bold h5 mt-2 text-truncate ">${truncateString(data[i].prod_title, 16)}</div>
                      <div class="product_view_rating text-center">
                        <div class="product_rating viewer text-center align-items-center" >
                          <span class="rating_text  ml-3 text-center">3.5 <i class="fas fa-star"></i> </span> <span>&nbsp;&nbsp;(15,000)</span>
                          <div>
                               <span class="text-center ml-3 mt-3 font-weight-bold">&#x20B9; ${Math.trunc(data[i].off_price)}</span>
                          <span class="original_price text-center" style="text-decoration: line-through;">&#8377; ${Math.trunc(data[i].m_price)}</span>  <span class="text-danger"> ${Math.trunc((100/data[i].m_price)*(data[i].m_price-data[i].off_price))}%</span>
                          </div>
                        </div>
                      </div>                         
                    </div>
                  </div>
                </a>
              </span>
            </li>            
          </ul>
        </div>
      </div>
    

  </div>`;

      }
       
      
     
       butan = `<button class="btn btn-primary font-weight-light"  onclick="getProdBycolor('${subid}' ,'${color}' ,'${12}')">See More</button>`;
       if (add == '12') {
           document.getElementById("pro").innerHTML += output; 
       } else {
         document.getElementById("pro").innerHTML = output; 
       }
       
       document.getElementById("butn").innerHTML = butan; 
    
    }
  });
  
}




function getProdByundtertiarycat(undterid,add) {
   if (add == '12') {
      visible += 12;
      console.log(visible);
     }
     else {
       visible = 12;
     }
 
  console.log('undter');
  
  
  console.log(undterid);

   $.ajax({
    type: 'POST',
     data: {
       'id': undterid,
       'visible': visible
       
     },
    url: '/underTerprod/',
   
      
     success: function (response) {
      
      console.log(response );
      var data = response.underTer;
      console.log(data)
      output = ''
      for (i = 0; i < data.length; i++){
       output +=`  
        <div class="col-3" >

    <div class="exclusive_category_div  ">
        <div class="product_section" id="product_section">
          <ul style="background-color: transparent;">
              <li class="  text-center card-hlight">
              <span>
                <div class="product_best_seller"><span>Best Seller</span></div>
                <div class="product_wish_list_icon"><i class="fas fa-heart"></i></div>

                <a href="/singleproduct/${data[i].prod_custom_id}">

                  <div class="product_design_div pl-1">
                    <div class="product_image" style="width: 200px; height: 300px; ">
                      <img src="/media/${data[i].product_image1}" style="width: 200px; height: 300px; " alt="">
                    </div>
                    <div class="product_description text-center text-truncate">
                      <div class="font-weight-bold h5 mt-2 text-truncate ">${truncateString(data[i].prod_title, 16)}</div>
                      <div class="product_view_rating text-center">
                        <div class="product_rating viewer text-center align-items-center" >
                          <span class="rating_text  ml-3 text-center">3.5 <i class="fas fa-star"></i> </span> <span>&nbsp;&nbsp;(15,000)</span>
                          <div>
                               <span class="text-center ml-3 mt-3 font-weight-bold">&#x20B9; ${Math.trunc(data[i].off_price)}</span>
                          <span class="original_price text-center" style="text-decoration: line-through;">&#8377; ${Math.trunc(data[i].m_price)}</span>  <span class="text-danger"> ${Math.trunc((100/data[i].m_price)*(data[i].m_price-data[i].off_price))}%</span>
                          </div>
                        </div>
                      </div>                         
                    </div>
                  </div>
                </a>
              </span>
            </li>            
          </ul>
        </div>
      </div>
    

  </div>`;

      }
       
      
      
       butan = `<button class="btn btn-primary font-weight-light"  onclick="getProdByundtertiarycat('${undterid}'   ,'${12}')">See More</button>`;
       if (add == '12') {
           document.getElementById("pro").innerHTML += output; 
       } else {
         document.getElementById("pro").innerHTML = output; 
       }
       
       document.getElementById("butn").innerHTML = butan; 
    
    }
  });
  
}









function rangePriceFilter() {
  var myRange = document.querySelector('#formControlRange');
  console.log(myRange);
var myValue = document.querySelector('#myValue');
  var myUnits = '₹';
  var off = myRange.offsetWidth / (parseInt(myRange.max) - parseInt(myRange.min));
var px =  ((myRange.valueAsNumber - parseInt(myRange.min)) * off) - (myValue.offsetParent.offsetWidth / 2);

  myValue.parentElement.style.left = px + 'px';
  myValue.parentElement.style.top = myRange.offsetHeight + 'px';
  myValue.innerHTML =  myUnits + ' ' + myRange.value;

  myRange.oninput =function(){
    var px = ((myRange.valueAsNumber - parseInt(myRange.min)) * off) - (myValue.offsetWidth / 2);
    myValue.innerHTML =  myUnits + ' ' + myRange.value;
    myValue.parentElement.style.left = px + 'px';
  };
}



function getpricerangeprod(catid,add) {
   var myRange = document.querySelector('#formControlRange');
 
  

  console.log(visible);

     if (add == '12') {
      visible += 12;
      console.log(visible);
     }
     else {
       visible = 12;
     }
     
     $.ajax({
    type: 'POST',
    data: {'id': catid, 'visible':visible},
    url: '/allprod/',
   
      
     success: function (response) {
       console.log(myRange.value)
       if (myRange.value <= 300) {
         console.log('yes')
       }
      console.log(response );
      var data = response.prod;
      console.log(data)
      output = ''
       for (i = 0; i < data.length; i++){
         
     if (myRange.value >= Math.trunc(data[i].off_price)){
       output +=`  
        <div class="col-3" >

    <div class="exclusive_category_div  ">
        <div class="product_section" id="product_section">
          <ul style="background-color: transparent;">
              <li class="  text-center card-hlight">
              <span>
                <div class="product_best_seller"><span>Best Seller</span></div>
                <div class="product_wish_list_icon"><i class="fas fa-heart"></i></div>

                <a href="/singleproduct/${data[i].prod_custom_id}">

                  <div class="product_design_div pl-1">
                    <div class="product_image" style="width: 200px; height: 300px; ">
                      <img src="/media/${data[i].product_image1}" style="width: 200px; height: 300px; " alt="">
                    </div>
                    <div class="product_description text-center text-truncate">
                      <div class="font-weight-bold h5 mt-2 text-truncate ">${truncateString(data[i].prod_title, 16)}</div>
                      <div class="product_view_rating text-center">
                        <div class="product_rating viewer text-center align-items-center" >
                          <span class="rating_text  ml-3 text-center">3.5 <i class="fas fa-star"></i> </span> <span>&nbsp;&nbsp;(15,000)</span>
                          <div>
                               <span class="text-center ml-3 mt-3 font-weight-bold">&#x20B9; ${Math.trunc(data[i].off_price)}</span>
                          <span class="original_price text-center" style="text-decoration: line-through;">&#8377; ${Math.trunc(data[i].m_price)}</span>  <span class="text-danger"> ${Math.trunc((100/data[i].m_price)*(data[i].m_price-data[i].off_price))}%</span>
                          </div>
                        </div>
                      </div>                         
                    </div>
                  </div>
                </a>
              </span>
            </li>            
          </ul>
        </div>
      </div>
    

  </div>`;
 }
      }
       
      
   
        butan = `<button class="btn btn-primary font-weight-light"  onclick="getallprod('${catid}' ,'${12}')">See More</button>`;
       if (add == '12') {
           document.getElementById("pro").innerHTML += output; 
       } else {
         document.getElementById("pro").innerHTML = output; 
       }
       
       document.getElementById("butn").innerHTML = butan; 
    
    }
     });
     

}