"use strict";

$.get('/myclosetjson', (res) => {
    const closet = res;
    for (const item of closet) {
        const itemDetails = (
        `<p>
            <li><b>Item Name: </b>${item.item_name}</li>
            <li><b>Description: </b>${item.item_description}</li>
            <li><b>Category: </b>${item.category}</li>
            <img src="${item.image_url}">  
            </p>`
        );
        $('#item-library').append(itemDetails);
    };
});


