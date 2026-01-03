document.addEventListener("DOMContentLoaded", () => {
    const heroImage = document.getElementById("hero-scroll"); // Hero image 
    const searchBar = document.getElementById("search-transform"); // Searchbar

    window.addEventListener("scroll", () => {
        const scrollY = window.scrollY;
        const scale = 1 + scrollY / 1100;
        const searchScale = 1 - scrollY / 1800;
        

        heroImage.style.transform = `scale(${scale})`;
        searchBar.style.transform = `
           translate(-50%, -50%) scale(${searchScale})
        `;
        
    });



});