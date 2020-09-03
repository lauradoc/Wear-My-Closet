"use strict";


$.get('/cartjson', (cart) => {
    // debugger;
    for (const item of cart) {
        console.log(item)
        const cartDetails = (
            `<div class="cart-details" id="cart-details-id-${item.id}">
                <ul class="item-details-table">
                    <input type="hidden" name="item-id" value="${item.id}">
                    <input type="hidden" value=${item.user} >
                    <li><label>Item Name: ${item.item_name}</li>
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
    console.log('check')
    $.get('/checkoutjson', (checkout_item) => {
        for (const item of checkout_item) {
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
    $.post('/removecartitem', formInputs, (res) => {
        alert(res);
    });
    const removeItem = document.querySelector(`#cart-details-id-${id}`)
    console.log(removeItem)
    removeItem.innerHTML = ''
    const formInputs = {
        'item_id': id
    };
};

