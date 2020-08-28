"use strict";



// $('#checkout-button').on('submit', (evt) => {
//     evt.preventDefault();

//     const formData = $('#checkout-item').serialize();

    
// }

// )

const checkoutButton = document.querySelector('#select-item');
console.log('check1')
checkoutButton.addEventListener('click', () => {
    enableCheckoutButton;
});
console.log('check2')

function enableCheckoutButton() {
    let checkoutButton = document.getElementById('checkout-button');
    if (select-item.value == true) {
        checkoutButton.disabled == false;
    }
    else {
        checkoutButton.disabled == true;
    }
}

