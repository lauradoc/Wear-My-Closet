"use strict";

$.get('/myclosetjson', (res) => {
    const closet = res;
    for (const item of closet) {
        let button = `<button type="submit" id="status-change">submit</button>`
        if (item.status == "Available") {
            button = `<button type="submit" disabled=true id="status-change">submit</button>`
        };
        const itemDetails = (
        `<p>
            <b>Item Name: </b>${item.item_name}
            <br>
            <b>Description: </b>${item.item_description}
            <br>
            <b>Category: </b>${item.category}
            <br>
            <b id="item-status">Item Status: </b>${item.status}
            <br>
            <form method="POST" id="status-change-form">
                <input type="hidden" name="item-id" value="${item.id}">
                <input type="radio" id"${item.id}" name="item-return" value="Item Returned">
                <label>Item Returned</label>
                ${button}
                </form>
            <br>
            <img src="${item.image_url}">  
            </p>`
        );
        $('#item-library').append(itemDetails);
    };
});


$('#status-change-form').on('submit', (evt) => {
    evt.preventDefault();

    const formData = $('#status-change-form').serialize();
    console.log(formData)
    $.post('/mycloset', formData, (json_item) => {
        const item = json_item;
        const statusUpdate = (
            `<b id="item-status">Item Status: </b>${item.status}`
        );
        $('#item-status').replaceWith(statusUpdate)
    });
});

