"use strict";


// document.addEventListener('DOMContentLoaded', () => {
//     document.querySelector("input[name=checkbox]").addEventListener('click', () => {
//      enable;
//     }  ); 
// });

// var checkbox = document.querySelector("input[name=checkbox]");
// console.log('check1')

// if (checkbox.checked) {
//     checkbox.addEventListener('change', () => {
//         if(checkbox.checked) {
//             enable
//         } else {
//             disable
//         }
//     });
// };

console.log('check1')
let selectedItem = document.getElementById('select-item');
console.log(selectedItem)
if (selectedItem.checked) {
    selectedItem.addEventListener('change', enable)}
else {
            disable}


// var checkoutButton = document.getElementById('select-item');
// console.log('check1')
// if (document.getElementById("checkout-button").disabled == true) {
//     checkoutButton.addEventListener('click', console.log('enable'));
// }

function enable() {
    document.getElementById("checkout-button").disabled == false;
}

function disable() {
     document.getElementById("checkout-button").disabled= true;
}

// $("#select-item").on("click", enable);

