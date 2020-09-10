"use strict";

$('#community-button').on('click', (evt) => {
    evt.preventDefault();
    const formData = {
        'community': $('#community-field').val()
    };
    console.log(formData)

    $.get('/communitycloset.json', formData, (community_items) => {
        $('#community-items').empty();
        for (const item of community_items) {
            let button = `<input type="button" onclick="addToCart(this.id)" name="add-to-cart" id="${item.id}" value="Add to cart">`
            if (item.status == "Unavailable") {
                button = `<input type="button" disabled=true onclick="addToCart(this.id)" name="add-to-cart" id="${item.id}" value="Add to cart">`
            };
            // else if (item in already in cart)
            const itemDetails = (
                `<div class="card mb-3">
                    <div class="row no-gutters">
                        <div class="col-md-6">
                            <img src="${item.image_url}" class="card-img-top">
                        </div>
                        <form method="POST" action="/cart" id="checkout-item">
                        <div class="col-md-6">
                            <div class="card-body">
                                <p class="card-text">
                                    <p id="username-field"><b>Owner: </b>${item.username}</p>
                                    <p id="item_name-field"><b>Item Name: </b>${item.item_name}</p>
                                    <p><b>Description: </b>${item.item_description}</p>
                                    <p><b>Category: </b>${item.category}</p>
                                    <p id="status-field"><b>Status: </b>${item.status}</p>
                                    ${button}
                                    <br>
                                </p>
                            </div>
                        </div>
                        </form>
                    </div>
                </div>`
            );
            $('#community-items').append(itemDetails);
        };
    });
});


function addToCart(id) {
    console.log(id)
    const itemInput = {
        'item_id': id
    };

    $.post('/addtocart', itemInput, (res) => {
        alert(res);
    });
    document.getElementById(id).disabled= true;
}

// `<div class="item-details">
//                     <div class="item-thumbnail">
//                     </div>
//                     <form method="POST" action="/cart" id="checkout-item">
//                         <ul class="item-info">
//                             <li id="username-field"><b>Owner: </b>${item.username}</li>
//                             <li id="item_name-field"><b>Item Name: </b>${item.item_name}</li>
//                             <li><b>Description: </b>${item.item_description}</li>
//                             <li><b>Category: </b>${item.category}</li>
//                             <li id="status-field"><b>Status: </b>${item.status}</li>
//                             ${button}
//                             <br>
//                             <img src="${item.image_url}">
//                         </ul>
//                     </form>
//                 </div>`
