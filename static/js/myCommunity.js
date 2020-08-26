"use strict";

$('#community-button').on('click', (evt) => {
    evt.preventDefault();

    const formData = {
        community: $('#community-field').val()
    };
    console.log(formData)
    alert(`Heading to ${formData.community} closet`);

    $.get('/communitycloset.json', formData, (community_items) => {
        for (const item of community_items) {
            console.log(item);
            const itemDetails = (
                `<div class="item-details">
                    <div class="item-thumbnail">
                    </div>
                    <form method="POST" action="/checkout" id="checkout-item">
                        <ul class="item-info">
                            <li><b>Owner: </b>${item.username}</li>
                            <li><b>Item Name: </b>${item.item_name}</li>
                            <li><b>Category: </b>${item.category}</li>
                            <input type="checkbox" name="community-item" value="{{ item.item_name }}">
                            <label>Borrow this item!</label>
                            <br>
                            <img src="${item.image_url}">
                            <br>
                        </ul>
                    </form>
                </div>`
            );
            $('#community-items').append(itemDetails);
        };
    });
});
