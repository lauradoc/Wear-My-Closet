"use strict";

$('#upload-item-form').on('submit', (evt) => {
    evt.preventDefault();

    const form_data = new FormData();
    form_data.append('item_name', $('#name-field').val());
    form_data.append('file', $('#image-field').prop('files')[0]);
    form_data.append('category', $('#category-field').val());
    console.log(formData)
    alert(`Uploading ${form_data} to your closet`);

    $.ajax({
        type: 'POST',
        url: '/addnewitem',
        data: form_data,
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
