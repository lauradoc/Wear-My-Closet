"use strict";

$('#upload-item-form').on('submit', (evt) => {
    evt.preventDefault();

    const formData = new FormData();
    formData.append('item_name', $('#name-field').val());
    formData.append('file', $('#image-field').prop('files')[0]);
    formData.append('category', $('#category-field').val());
    console.log(formData)
    alert(`Uploading ${formData.item_name} to your closet`);

    $.ajax({
        type: 'POST',
        url: '/addnewitem',
        data: formData,
        contentType: false,
        cache: false,
        processData: false,
        success: (res) => {
            const new_item = res;
            console.log('*************', new_item)
            for (const item of new_item) {
                console.log('*************', item)
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
            $('#item-library').prepend(itemDetails)};
        },
    });
});
