$("#search_number").on('keyup', function(e){
  // console.log(e)
  let search_value = e.currentTarget.value;
  let prefix = "SELLER-";
  if(search_value != ""){
    $("#seller_table_content").hide();
    $("#seller_search_result").show();
    $.ajax({
      url: '/site-admin/seller/search-seller/',
      method: "GET",
      data: {
        "search_keyword": search_value
      },
      success: function(e){
        // console.log(e);
        search_template(e.resp);
      },
      error: function(e){
        console.log(e);
      }
    });
  }else{
    $("#seller_table_content").show();
    $("#seller_search_result").hide();
  }
});

function search_template(resp){
  let template ='';
  console.log(resp);
  if(resp.length == 0){
    template = `<th scope="row" colspan="7" style="text-align: center;">No seller found</th>`;
  }
  else{
    let response = resp.map((data, key) => {
      let seller_is_active = data.active ? `<a href="javascript:void(0);" title="Active" class="btn btn-success btn-circle btn-sm"><i class="fas fa-check"></i></a>`:`<a href="javascript:void(0);" title="Active" class="btn btn-danger btn-circle btn-sm"><i class="fas fa-times"></i></a>`
      template+= `
        <tr>
          <th scope="row">${key+1}</th>
          <td style="font-size: 13px; font-weight: bold;">`+data.seller_id+`</td>
          <td>${data.seller_title}</td>
          <td>${data.seller_email_id}</td>
          <td>${data.seller_phone_no}</td>
          <td>
            ${seller_is_active}
          </td>
          <td>
            <a href="/site-admin/seller/seller-view/${data.seller_id}" class="btn btn-info btn-sm">
              <i class="fas fa-eye"></i>
              View
            </a>
            <a href="javascript:void(0);" class="btn btn-warning btn-sm">
              <i class="fas fa-edit"></i>
              Edit
            </a>
          </td>
        </tr>
      `;
    });
  }
  $("#seller_search_result").html(template);
}
