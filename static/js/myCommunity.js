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
                `<div class="item-details">
                    <div class="item-thumbnail">
                    </div>
                    <form method="POST" action="/cart" id="checkout-item">
                        <ul class="item-info">
                            <li id="username-field"><b>Owner: </b>${item.username}</li>
                            <li id="item_name-field"><b>Item Name: </b>${item.item_name}</li>
                            <li><b>Description: </b>${item.item_description}</li>
                            <li><b>Category: </b>${item.category}</li>
                            <li id="status-field"><b>Status: </b>${item.status}</li>
                            ${button}
                            <br>
                            <img src="${item.image_url}">
                        </ul>
                    </form>
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

// function getCartItemByUser
