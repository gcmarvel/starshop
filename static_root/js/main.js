// Cart Screen js

const cart = document.getElementsByClassName('cart-fixed')[0];
const overall = document.getElementsByClassName('overall')[0];
const basketText = document.getElementById('basket-text');

window.onscroll = function CartAnimation() {
    if (window.innerWidth > 480){
        if (document.documentElement.scrollTop !== 0) {
            cart.style.transform = 'translate(45%, 0)';
            basketText.style.opacity = '0';
            overall.style.opacity = '1';
        } else {
            cart.style.transform = 'translate(0, 0)';
            basketText.style.opacity = '1';
            overall.style.opacity = '0';
        }
    }
}
