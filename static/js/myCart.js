"use strict";


$.get('/cartjson', (cart) => {
    // debugger;
    for (const item of cart) {
        // console.log(item)
        const cartDetails = (
            `<div class="card">
                <div class="row no-gutters" id="cart-details-id-${item.id}">
                    <div class="col">    
                        <div class="card-body">
                            <p class="card-text">
                                <input type="hidden" name="item-id" value="${item.id}">
                                <input type="hidden" value=${item.user} >
                                <p><label>Item Name: ${item.item_name}</p>
                                <p><label>Return Date: <input id="due-date-${item.id}" type="date" name="due-date-${item.id}"></label></p>
                                <p>Checkout Status: ${item.status}</p>
                                <input type="radio" onclick="removeFromCart(this.id)" id="${item.id}" name="remove" value="Remove Item">
                                <label>Remove item</label>
                            </p>
                        </ul>
                    </div>
                </div>
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
                `<div class="card">
                <p class="card-text">
                    <p>Item Name: ${item.item_name}</p>
                    <p>Checkout Date: ${item.checkout_date}</p>
                    <p>Due Date: ${item.due_date }</p>
                </p>
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

