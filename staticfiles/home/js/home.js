/* jshint esversion: 11 */
document.addEventListener("DOMContentLoaded", () => {
    const heroImage = document.getElementById("hero-scroll"); // Hero image 
    const searchBarTransform = document.getElementById("search-transform"); // Searchbar duv

    window.addEventListener("scroll", () => {
        const scrollY = window.scrollY;

        if (!heroImage) 
            return;

        if (!searchBarTransform)
            return;

        let scale = 1 + scrollY / 1100;
        let searchScale = 1 - scrollY / 1800;

        if (scale >= 1.8) {
            heroImage.style.transform = "scale(1.8)";
        }
        else {
            heroImage.style.transform = `scale(${scale})`;
            searchBarTransform.style.transform = `
                translate(-50%, -50%) scale(${searchScale})
            `;
        }
        
    });

    const searchBtn = document.getElementById("clear-btn"); // Clear Button
    const searchBarText = document.getElementById("search-bar"); // Searchbar

    if (!searchBtn || !searchBarText) return;

    searchBtn.addEventListener("click", () => {
        searchBarText.value = "";
    });



});