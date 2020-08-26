"use strict";

$('#upload-item-form').on('submit', (evt) => {
    evt.preventDefault();

    const formData = {
        'item_name': $('#name-field').val(),
        'file': document.getElementById('image-field').files[0],
        'category_name': $('#category-field').val()
    };

    const jsonFormData = JSON.stringify(formData)
    // let formData = new FormData();

    // formData.append('item_name', $('#name-field').val());
    // formData.append('file', document.getElementById('image-field').files[0]);
    // formData.append('category_name', $('#category-field').val());
    console.log(jsonFormData)
    alert(`Uploading ${formData.item_name} to your closet`);

    $.post('/mycloset', jsonFormData, (new_item) => {
        console.log(new_item);

        for (const item of new_item) {
            const itemDetails = (`
                <div>
                    <form method="POST" id="upload-item">
                        <ul class="item-details">
                            <li><b>Item Name: </b>${item.item_name}</li>
                            <li><b>Category: </b>${item.category}</li>
                            <br>
                            <img src="${item.image_url}">
                            <br>
                        </ul>
                    </form>
                </div>
            `);
            $('#image-library').append(itemDetails);
        };
    });
});