"use strict";

$('#upload-item-form').on('submit', (evt) => {
    evt.preventDefault();

    const formData = $('#upload-item-form').serialize();
        console.log(formData)
        // alert(`Uploading ${formData.item_name} to your closet`);

        $.post('/mycloset', formData, (new_item) => {
            console.log(new_item);

            // for (const item of item_details) {
                // const itemDetails = (`
                //     <div>
                //         <form method="POST" action="/mycloset" id="upload-item">
                //             <ul class="item-details">
                //                 <li><b>Item Name: </b>${item.item_name}</li>
                //                 <li><b>Category: </b>${item.category}</li>
                //                 <br>
                //                 <img src="${item.image_url}">
                //                 <br>
                //             </ul>
                //         </form>
                //     </div>
                // `);
                // $('#image-library').append(itemDetails);
        });
    });
// });