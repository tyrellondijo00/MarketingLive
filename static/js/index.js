const hamburger = document.querySelector(".hamburger");
const navLink = document.querySelector(".nav-links");

hamburger.addEventListener("click", () =>{
    hamburger.classList.toggle("active");
    navLink.classList.toggle("active");
})

document.querySelectorAll(".link").forEach(n => n.addEventListener("click", () => {
    hamburger.classList.remove("active");
    navLink.classList.remove("active");
}))

// OUR CLIENTS CAROUSEL  
$(document).ready(function () {
    $(".logo-carousel").slick({
        slidesToShow: 6,
        slidesToScroll: 1,
        autoplay: true,
        autoplaySpeed: 1000,
        arrows: true,
        dots: false,
        pauseOnHover: false,
        responsive: [
            {
                breakpoint: 768,
                settings: {
                    slidesToShow: 4,
                },
            },
            {
                breakpoint: 520,
                settings: {
                    slidesToShow: 2,
                },
            },
        ],
    });
});
// OUR CLIENTS CAROUSEL


// PAGINATION
$(document).ready(function () {
	$("[href]").each(function () {
		if (this.href == window.location.href) {
			$(this).addClass("active");
		}
	});
});
// PAGINATION