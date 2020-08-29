"use strict";


$('#community-button').on('click', (evt) => {
    evt.preventDefault();
    const formData = {
        'community': $('#community-field').val()
    };
    alert(`Heading to ${formData.community} closet`);

    $.get('/communitycloset.json', formData, (community_items) => {
        for (const item of community_items) {
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
                            <input type="checkbox" name="checkbox" onchange="checkStatus(this)" id="${item.item_name}" value="${item.item_name }">
                            <label>Select</label>
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

function enable() {
    document.getElementById("checkout-button").disabled == false;
}

function disable() {
     document.getElementById("checkout-button").disabled= true;
}

function checkStatus(item) {
    console.log(item)
}
