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
                    <li><label>Due Date: <input id="due-date-${item.id}" type="date" name="due-date-${item.id}"></label></li>
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

    const formValues = $('#cart-details-form').serialize();
    $.post('/checkout', formValues, (checkout_items) => {
        console.log(checkout_items)
        for (const item of checkout_items) {
            const checkoutItemDetails = 
                `<div class="checkout-details">
                <ul>
                    <li>Item Name: ${item.item_name}</li>
                    <li>Checkout Date: ${item.checkout_date}</li>
                    <li>Due Date: ${item.due_date }</li>
                </ul>
                </div>`
            ;
            $('#cart-details-form').empty();
            $('#checkout-summary').append(checkoutItemDetails);
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
    const removeItem = document.querySelector(`#cart-details-id-${id}`)
    removeItem.innerHTML = ''
};

