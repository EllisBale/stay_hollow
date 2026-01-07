$(document).ready(function () {

    $("#btn-to-top").on("click", function() {
        window.scrollTo({ top: 0, behavior: "smooth"})
    })


    /*const toast = document.getElementById(alerts)

    if (toast) {
        console.log(toast)
    } else {
        console.log("Toast not found")
    }*/



    const scrollDistance = 500;
    const desktopWidth = 992;

    function backToTop() {
        const $btn = $(".back-to-top");

        if (window.innerWidth >= desktopWidth) {
            $btn
                .addClass("is-desktop")
                .removeClass("is-hidden")
                .show();
            return;
        }

        $btn.removeClass("is-desktop");

        if ($(window).scrollTop() > scrollDistance) {
            $btn.removeClass("is-hidden");

        }

        else {
            $btn.addClass("is-hidden");
        }
    }

    $(window).on("scroll resize", backToTop);
    backToTop();

});