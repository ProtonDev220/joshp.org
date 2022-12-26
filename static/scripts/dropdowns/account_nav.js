const dropdown_toggle = document.getElementById('account-dropdown-toggle');
const dropdown_body = document.getElementById('account-dropdown-body');

dropdown_toggle.addEventListener('click', function () {
    if (dropdown_body.style.display == 'none') {
        dropdown_body.style.display = 'flex';
    } else {
        dropdown_body.style.display = 'none';
    }
});