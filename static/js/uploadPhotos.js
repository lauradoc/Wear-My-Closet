"use strict";


$('#upload-item-form').on('submit', (evt) => {
    evt.preventDefault();

    const formValue = {
        'item_name': $('#item-field').val()
    };
        console.log('*****************', formValue)

    $.post('/mycloset', formValue, (res) => {
        alert(res);
    });
});