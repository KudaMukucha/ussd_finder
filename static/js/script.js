const btn = document.getElementById('menu-btn');
const nav = document.getElementById('menu');

btn.addEventListener('click', () => {
    nav.classList.toggle('hidden');

    // Toggle icons with transition
    if (nav.classList.contains('hidden')) {
        btn.innerHTML = "<i class='bx bx-menu bx-md transition-all duration-300'></i>"; // Change to Menu icon
    } else {
        btn.innerHTML = "<i class='bx bx-x bx-md transition-all duration-300'></i>"; // Change to X icon
    }
});