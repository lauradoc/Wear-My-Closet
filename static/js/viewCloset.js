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
            <b>Item Status: </b>${item.status}
            <br>
            <label for="update-status">Update Staus:</label>
            <select name="select-status">
            <option name="Available" value= "Available">Available</option>
            <option name="Unavailable" value= "Unavailable">Unavailable</option></select>
            <br>
            <img src="${item.image_url}">  
            </p>`
        );
        $('#item-library').append(itemDetails);
    };
});

$('#item-status').on('click', (evt) => {
    evt.preventDefault();
    const formData = {
        'status': $('#item-status').val()
    };
    console.log(formData)

    $.post('/mycloset', formData)
})


