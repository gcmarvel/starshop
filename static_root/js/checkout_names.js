const NameStarFormInputs = document.getElementById('name-star-form').elements;

window.onload = function makeRequired() {
    for (var i = 0; i < NameStarFormInputs.length; i += 1) {
        NameStarFormInputs[i].required = true;
    }
};



