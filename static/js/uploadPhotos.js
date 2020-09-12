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
            const new_item = (
                `<div class="card mb-3" style="max-width: 540px;">
                    <div class="row no-gutters">
                        <form method="POST" id="upload-item" >
                            <div class="col-md-6">
                                <img src="${item.image_url}" class="card-img-top">
                            </div>
                            <div class="col">
                                <div class="card-body">
                                    <p class="card-text">
                                        <p class="item-details">
                                            <b>Item Name: </b>${item.item_name}
                                            <b>Description: </b>${item.item_description}
                                            <b>Category: </b>${item.category}
                                            <b>Status: </b>${item.status}
                                            <br>
                                            <form method="POST" id="status-change-form">
                                                <input type="hidden" name="item-id" value="${item.id}">
                                                <input type="radio" id"${item.id}" name="item-return" value="Item Returned">
                                                <label>Item Returned</label>
                                                <button type="submit" id="status-change">submit</button>
                                            <br>
                                            <br>
                                        </p>
                                    </p>
                                </div>
                            </div>
                        </form>
                    </div>
                </div>`
            );
            $('#item-library').prepend(new_item)
        },
    });
});
