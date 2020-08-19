"use strict";

$('#my-community-form').on('submit', (evt) => {
    evt.preventDefault();

    const formValues = ('#my-community-form').serialize();
    console.log(formValues)
    $.get('/communitycloset', formValues, (res) => {
        alert(`Going to ${res} closet!`);
    });
});