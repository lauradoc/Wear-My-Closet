"use strict";

$('#community-buttons').on('click', (evt) => { 
    evt.preventDefault();
    
    const formData = $('#my-community-form').serialize();

    $.get('/community.json', formData, (res) => {
        console.log(formData)
        alert(`Heading to ${formData} closet`);
    });
});

$('#community-buttons').on('click', (evt) => {
    evt.preventDefault();

    const formData = {

    }
    $.get('/community', {'item_id': evt.target.id} (res) => {
        const itemDetails =(
            <div class="item-details">
                <div class="item-thumbnail">
                    <img src="item.image_url"
                    />
                </div>

                <ul class="item-info">
                    <li><b>Item Name: </b>${item.item_name}</li>
                    <li><b>Item Name: </b>${item.item_name}</li>
                    <li><b>Item Name: </b>${item.item_name}</li>
                    <li><b>Item Name: </b>${item.item_name}</li>
                    <li><b>Item Name: </b>${item.item_name}</li>
                </ul>
            </div>
        );
    }
    )
}
)
// {/* <form action="/myaccount" id="checkout-items"></form>
// <ul>
// {% for user in community_users %}
//     <li>{{ user }}</li>
//     <input type="radio" name="community" value="{ user_items[user] }}">
//     {% for item in user_items%}
//     <label><img src={{ user_items[user] }}></label>
//     <br> 
//     <button type="submit" id="community-buttons" action="/myaccount">Select</button>
//     {% endfor %}
// {% endfor %}

// </ul>
// </form> */}