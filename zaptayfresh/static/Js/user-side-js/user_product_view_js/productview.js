  function describ(des){
    console.log(des);
       document.getElementById("DR").innerHTML = des;
   }


function review(rev) {


  rebeu = `
  <div class="container shadowO">
    <form action="" class="my-2">
     <div class="form-group">
    <label for="exampleFormControlTextarea1" class="h3">Review</label>
    <textarea class="form-control" id="exampleFormControlTextarea1" rows="3"></textarea>
  </div>
  <button class="btn btn-primary font-weight-light" type="submit">Post</button>
    </form>

    <div class="scrol shadow" style="overflow: scroll; height: 300px;   overflow-x: hidden;">
    <div class="list-group">
  <a href="#" class="list-group-item list-group-item-action flex-column align-items-start ">
    <div class="d-flex w-100 justify-content-between">
      <h5 class="mb-1">Vivek Dubey</h5>
     
    </div>
    <p class="mb-1">Nice Product</p>
  
  </a>
  <a href="#" class="list-group-item list-group-item-action flex-column align-items-start">
    <div class="d-flex w-100 justify-content-between">
      <h5 class="mb-1">Priti Arora</h5>
    
    </div>
    <p class="mb-1">Loved the print,fabric,color, design .10/10 in budget 💓💓💓. Fine stitching. Only complain with the pants. That's not palazzo. It's more kind of pant. Go a size bigger as It is little tight may be after a wash it can be shrink.</p>
 
  </a>


  <a href="#" class="list-group-item list-group-item-action flex-column align-items-start">
    <div class="d-flex w-100 justify-content-between">
      <h5 class="mb-1">Binod</h5>
    
    </div>
    <p class="mb-1">Awsome !</p>
 
  </a>


</div>
    </div>
  </div>`

  document.getElementById("DR").innerHTML = rebeu;
}

/* Colour image */
 