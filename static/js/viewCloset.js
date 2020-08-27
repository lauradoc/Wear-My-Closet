"use strict";
console.log('you here????')
// function displayCloset() {
    console.log('check!')
    $.get('/myclosetjson', (res) => {
        const closet = res;
        for (const item of closet) {
            console.log(item);
            const itemDetails = (
            `<p>
                <li><b>Item Name: </b>${item.item_name}</li>
                <li><b>Category: </b>${item.category}</li>
                <img src="${item.image_url}">  
              </p>`
            );
            $('#item-library').append(itemDetails);
        };
    });
// };


