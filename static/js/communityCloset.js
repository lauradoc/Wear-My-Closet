"use strict";

$('#my-community-form').on('submit', (evt) => {
    evt.preventDefault();

    // const formValues = {
    //     'community': $('#select-community').val()
    // };
    // console.log(formValues)
    $.get('/mycloset' );
});