"use strict";

$('#cart-button').on('click', (evt) => {
    evt.preventDefault();
    console.log('check')
    $.get('/cartjson', (cart) => {
        for (const item of cart) {
            console.log(item)
            const cartDetails = (
                `<div class="cart-details">
                <form method="POST" action="/checkout" id="checkout-form">
                    <ul>
                        <li>Item ID: ${item.item_id}</li>
                        <li>User ID: ${item.user_id}</li>
                        <li>Checkout Date</li>
                        <li>Due Date</li>
                        <li>Return Date</li>
                        <li>Checkout Status: ${item.status}</li>
                        <button type="submit" name="checkout-form" action="/checkout">Checkout</button>
                        </ul>
                    </ul>
                </form>
                </div>`
            );
            $("cart-items").append(cartDetails);
        };
    });
});
