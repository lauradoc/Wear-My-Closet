"use strict";


$.get('/cartjson', (cart) => {
    for (const item of cart) {
        console.log(item)
        const cartDetails = (
            `<div class="cart-details">
                <form method="POST" id="checkout-form">
                    <ul>
                        <li id="checkout-item">Item ID: ${item.id} </li>
                        <li>User ID: ${item.user} </li>
                        <li><label>Checkout Date: <input id="checkout-date" type="date" name="checkout-date"></label></li>
                        <li><label>Due Date: <input id="due-date" type="date" name="due-date"></label></li>
                        <li>Checkout Status: ${item.status}</li>
                        <input type="radio" onclick="removeFromCart(this.id)" id="${item.id}" name="remove" value="Remove Item">
                        <label>Remove item</label>
                        </ul>
                    </ul>
                </form>
            </div>`
        );
        $('#cart-items').append(cartDetails);
    };
});

function removeFromCart(id) {
    const formInputs = {
        'item_id': id
    };
    $.post('/removecartitem', formInputs, (res) => {
        alert(res);
    });
};

