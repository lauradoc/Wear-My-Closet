"use strict";

$('#upload-item-form').on('submit', (evt) => {
    evt.preventDefault();
    // console.log(evt)
    const form_data = new FormData();
    form_data.append('file', $('#image-field').prop('files')[0]);
    form_data.append('item_name', $('#name-field').val());
    form_data.append('item_description', $('#description-field').val());
    form_data.append('category', $('#category-field').val());
    console.log(form_data)
    // alert(`Uploading ${form_data.item_name} to your closet`);

    $.ajax({
        type: 'POST',
        url: '/addnewitem',
        data: form_data,
        contentType: false,
        cache: false,
        processData: false,
        success: (res) => {
            const item = res;
            console.log('*************', item)
            const new_item = (`
                <div>
                    <form method="POST" id="upload-item">
                        <ul class="item-details">
                            <li><b>Item Name: </b>${item.item_name}</li>
                            <li><b>Description: </b>${item.item_description}</li>
                            <li><b>Category: </b>${item.category}</li>
                            <li><b>Status: </b>${item.status}</li>
                            <br>
                            <input type="hidden" name="item-id" value="${item.id}">
                            <select name="select-status">
                            <option name="Available" value= "Available">Available</option>
                            <option name="Unavailable" value= "Unavailable">Unavailable</option></select>
                            <button type="submit" id="status-change">submit change</button>
                            <br>
                            <img src="${item.image_url}">
                            <br>
                        </ul>
                    </form>
                </div>
            `);
            $('#item-library').prepend(new_item)
        },
    });
});
