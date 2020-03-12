const PersonalPageFormInputs = document.getElementById('message-form').elements;

window.onload = function autoChoose() {
    for (var i = 0, max = PersonalPageFormInputs.length; i < max; i++) {
        if (PersonalPageFormInputs[i].type === 'checkbox')
            PersonalPageFormInputs[i].checked = true;
    }
}
