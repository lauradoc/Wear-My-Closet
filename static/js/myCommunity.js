"use strict";


$('#community-button').on('click', (evt) => {
    evt.preventDefault();
    const formData = {
        'community': $('#community-field').val()
    };
    // alert(`Heading to ${formData.community} closet`);

    $.get('/communitycloset.json', formData, (community_items) => {
        for (const item of community_items) {
            const button = `<input type="button" onclick="addToCart(this.id)" name="add-to-cart" id="${item.id}" value="Add to cart">`
            if (item.status == "Unavailable") {
                button = `<input type="button" disabled=true onclick="addToCart(this.id)" name="add-to-cart" id="${item.id}" value="Add to cart">`
            };
            const itemDetails = (
                `<div class="item-details">
                    <div class="item-thumbnail">
                    </div>
                    <form method="POST" action="/checkout" id="checkout-item">
                        <ul class="item-info">
                            <li><b>Owner: </b>${item.username}</li>
                            <li><b>Item Name: </b>${item.item_name}</li>
                            <li><b>Description: </b>${item.item_description}</li>
                            <li><b>Category: </b>${item.category}</li>
                            <li><b>Status: </b>${item.status}</li>
                            ${button}
                            <br>
                            <img src="${item.image_url}">
                        </ul>
                    </form>
                </div>`
            );
            $('#community-items').append(itemDetails);
            document.getElementById("{item.item_name}")
        };
    });
});

// function enable() {
//     document.getElementById("checkout-button").disabled == false;
// }

function disable() {
}

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




