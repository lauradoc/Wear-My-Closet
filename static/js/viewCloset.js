"use strict";

$.get('/myclosetjson', (res) => {
    const closet = res;
    for (const item of closet) {
        let button = `<button type="submit" id="status-change">submit</button>`
        if (item.status == "Available") {
            button = `<button type="submit" disabled=true id="status-change">submit</button>`
        };
        const itemDetails = (
        `<div class="card mb-3" style="max-width: 540px;">
            <div class="row no-gutters">
                <div class="col-md-6">
                    <img src="${item.image_url}" class="card-img-top">
                </div>
                <div class="col-md-6">
                    <div class="card-body">
                        <p class="card-text">
                            <b>Item Name: </b>${item.item_name}
                            <br>
                            <b>Description: </b>${item.item_description}
                            <br>
                            <b>Category: </b>${item.category}
                            <br>
                            <b id="item-status">Status: </b>${item.status}
                            <br>
                            <form method="POST" id="status-change-form">
                                <input type="hidden" name="item-id" value="${item.id}">
                                <input type="radio" id"${item.id}" name="item-return" value="Item Returned">
                                <label>Item Returned</label>
                                ${button}
                            </form>
                        </p>
                    </div>
                </div>
            </div>
        </div>`
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

