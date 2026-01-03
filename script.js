let slides = document.querySelectorAll(".slide");
let index = 0;

function nextSlide() {
    slides[index].classList.remove("active");
    index++;
    slides[index].classList.add("active");
}
