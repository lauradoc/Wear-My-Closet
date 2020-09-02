"use strict";


$.get('/cartjson', (cart) => {
    for (const item of cart) {
        console.log(item)
        const cartDetails = (
            `<div class="cart-details">
                <ul class="item-details-table">
                    <input type="hidden" name="item-id" value="${item.id}">
                    <input type="hidden" value=${item.user} >
                    <li><label>Checkout Date: <input id="checkout-date" type="date" name="checkout-date"></label></li>
                    <li><label>Due Date: <input id="due-date" type="date" name="due-date"></label></li>
                    <li>Checkout Status: ${item.status}</li>
                    <input type="radio" onclick="removeFromCart(this.id)" id="${item.id}" name="remove" value="Remove Item">
                    <label>Remove item</label>
                </ul>
            </div>`
        );
        $('#cart-items').append(cartDetails);
    
    };
});


$('#complete-checkout').on('click', (evt) => {
    evt.preventDefault();
    console.log('check')
    $.get('/checkoutjson', (checkout) => {
        for (const item of checkout) {
            console.log(item)
            const checkoutDetails = (
                `<div class="checkout-details>
                <ul>
                    <li>Item Name: ${item.item_name}</li>
                    <li>Checkout Date: ${item.checkout_date}</li>
                    <li>Due Date: ${item.due_date }</li>
                </ul>
                </div>`
            );
            $('#checkout-summary').append(checkoutDetails);
        };
    });
});

function removeFromCart(id) {
    const formInputs = {
        'item_id': id
    };
    $.post('/removecartitem', formInputs, (res) => {
        alert(res);
    });
};

