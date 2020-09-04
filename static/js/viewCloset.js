"use strict";

$.get('/myclosetjson', (res) => {
    const closet = res;
    for (const item of closet) {
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
                Update Status:
                <input type="hidden" name="item-id" value="${item.id}">
                <select name="select-status">
                <option name="Available" value= "Available">Available</option>
                <option name="Unavailable" value= "Unavailable">Unavailable</option></select>
                <button type="submit" id="status-change">submit change</button>
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



