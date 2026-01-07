document.addEventListener("DOMContentLoaded", () => {
    const heroImage = document.getElementById("hero-scroll"); // Hero image 
    const searchBar = document.getElementById("search-transform"); // Searchbar

    window.addEventListener("scroll", () => {
        const scrollY = window.scrollY;

        if (!heroImage) 
            return;

        let scale = 1 + scrollY / 1100;
        let searchScale = 1 - scrollY / 1800;

        if (scale >= 1.8) {
            scale = 1.8;
        }
        else {
            heroImage.style.transform = `scale(${scale})`;
            searchBar.style.transform = `
                translate(-50%, -50%) scale(${searchScale})
            `;
        }
        
    });



});
