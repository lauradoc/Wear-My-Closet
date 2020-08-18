"use strict";

// const imageLibrary = document.querySelectorAll('img')

// for (const img of imageLibrary)
//     imageLibrary.setAttribute('src', )


// const itemForm = document.querySelector('form');

// itemForm.addEventListener('submit', (evt) => {
//     const newFile = document.querySelector('input[name="file"]')
//     const newItemName = document.querySelector('input[name="item_name"]')
//     const newCategory = document.querySelector('input[name="category"]');


// })

$('#upload-item-form').on('submit', (evt) => {
    evt.preventDefault();

    const formValues = {
        item_name: $('#item-field').val()
    };
    $.post('/mycloset', formValues, (res) => {
        alert(`${res.item_name} has been added to your closet`);
    });
});