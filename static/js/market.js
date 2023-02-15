// JavaScript function to get cookie by name
function getCookie(name) {
    let cookieValue = null;
    if (document.cookie && document.cookie !== '') {
        const cookies = document.cookie.split(';');
        for (let i = 0; i < cookies.length; i++) {
            const cookie = cookies[i].trim();
            // Does this cookie string begin with the name we want?
            if (cookie.substring(0, name.length + 1) === (name + '=')) {
                cookieValue = decodeURIComponent(cookie.substring(name.length + 1));
                break;
            }
        }
    }
    return cookieValue;
}
const csrftoken = getCookie('csrftoken');

//Get all products

$(document).ready(function(){

    let temp = ""
    $.ajax({
        type:"GET",
        url:"/list/",
        success: function(data){
            $.each(data, function(i,product){
                var prodOwner = product.owner.split('/')[0]
                var ownerID = product.owner.split('/')[1]
                temp += "<div class='col-4'>"
                temp += "<div class='card border-primary mb-3' style='max-width: 20rem;'>"
                temp += "<div class='card-header'>" + prodOwner + "</div>"
                temp += "<div class='card-body'>"
                temp += "<h4 class='card-title'>" + product.product_name +"</h4>"
                if(product.prod_pic){
                    temp += "<img src='" + product.prod_pic + "' class='img-fluid' id='prodPic'></img>"
                }
                else{
                    temp += "<img src='{% get_media_prefix %}defaultProdPic.png' id='prodPic'></img>"
                }

                temp += "<a href='users/profile-page/" + ownerID + "/' class='card-link'>Product seller details</a><br>"
                temp += "<p><strong> " + product.price + " php</strong></p>"

                if(product.status === 1){
                    temp += "<p style='color:green;'><strong style='color:grey;'>Status: </strong>" + product.status_name + "</p>"
                }
                else if(product.status === 2){
                    temp += "<p style='color:red;'><strong style='color:grey;'>Status: </strong>" + product.status_name + "</p>"
                }

                if(product.stock > 0 && product.status == 2){
                    //update status
                    $.ajax({
                        type: "PATCH",
                        url: "product-detail/" + product.id + "/",
                        data:{
                            'status': 1
                        },
                        beforeSend: function(xhr){
                            xhr.setRequestHeader("X-CSRFToken", csrftoken);
                        },
                        success:function(){
                            console.log("Stock updated")
                            location.reload(true);
                        },
                        error:function(error){
                            console.log(error)
                        }
                    })
                }
                else if(product.stock < 1 && product.status == 1){
                    //update status
                    $.ajax({
                        type: "PATCH",
                        url: "product-detail/" + product.id + "/",
                        data:{
                            'status': 2
                        },
                        beforeSend: function(xhr){
                            xhr.setRequestHeader("X-CSRFToken", csrftoken);
                        },
                        success:function(){
                            console.log("Stock updated")
                            location.reload(true);
                        },
                        error:function(error){
                            console.log(error)
                        }
                    })
                }

                temp += "<p><strong>Category: </strong>" + product.category_name + "</p>"
                temp += "</div><div class='card-footer'>"
                temp += "<a href='/product-view/" + product.id + "/' class='btn btn-outline-dark' data-mdb-ripple-color='dark' style='z-index: 1;'>Details</a></div></div></div>"
            })
            $("#prodContainer").append(temp);
        }
    })
})

//Search dashboard

