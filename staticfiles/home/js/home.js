document.addEventListener("DOMContentLoaded", () => {
    const heroImage = document.getElementById("hero-scroll"); // Hero image 

    window.addEventListener("scroll", () => {
        const scrollY = window.scrollY;
        const scale = 1 + scrollY / 1100;

        heroImage.style.transform = `scale(${scale})`;
    });



});