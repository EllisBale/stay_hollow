/* jshint esversion: 11 */
document.addEventListener("DOMContentLoaded", () => {
    const heroImage = document.getElementById("hero-scroll"); // Hero image 

    window.addEventListener("scroll", () => {

        const scrollY = window.scrollY;

        let scale = 1 + scrollY / 1100;

        if (!heroImage) 
            return;

        if (scale >= 1.8) {
            heroImage.style.transform = "scale(1.8)";
        }
        else {
            heroImage.style.transform = `scale(${scale})`;
        }
    });

    const searchBtn = document.getElementById("clear-btn"); // Clear Button
    const searchBarText = document.getElementById("search-bar"); // Searchbar

    if (!searchBtn || !searchBarText) return;
    
    searchBtn.addEventListener("click", () => {
        searchBarText.value = "";
    });

});