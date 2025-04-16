////////////////////////////////////////////////////////////////////////////  Sticky Navbar Script -

window.addEventListener("scroll", function () {
    var navbar = document.querySelector(".navbar");
    navbar.classList.toggle("sticky", window.scrollY > 50);
});

//////////////////////////////////////////////////////////////////////////// arrow animation

// let smoke = document.getElementById('smoke');

// function createSmoke(e) {
//     let elem = document.createElement('div')
//     elem.classList.add('elem');

//     elem.style.left = `${e.clientX}px`;
//     elem.style.top = `${e.clientY}px`;
//     smoke.appendChild(elem);

//     elem.addEventListener('animationend', () => {
//         elem.remove();

//     })
// }

// document.addEventListener('mousemove', createSmoke);


const circleElement = document.querySelector('.circle');

const mouse = { x: 0, y: 0 },
    circle = { x: 0, y: 0 };

window.addEventListener('mousemove', e => {
    mouse.x = e.x;
    mouse.y = e.y;
});

// Speed factor
// Between 0 and 1 (0 = smoother, 1 = instant)
const speed = 0.15;

const tick = () => {
    // (mouse.x - circle.x) calculates the difference between the current x-coordinate of the mouse and the current x-coordinate of the circle.
    // (mouse.x - circle.x) * speed multiplies the difference by the speed factor, which determines how quickly the circle should move towards the mouse position
    circle.x += (mouse.x - circle.x) * speed;
    circle.y += (mouse.y - circle.y) * speed;

    // Update circle element's position
    circleElement.style.transform = `translate(${circle.x}px, ${circle.y}px)`;

    // Call function on next frame
    window.requestAnimationFrame(tick);
}

tick();


//////////////////////////////////////////////////////////////////////////// Initialize Swiper


var swiper = new Swiper(".main_slider_swiper", {
    effect: "coverflow",
    grabCursor: true,
    centeredSlides: true,
    slidesPerView: "auto",
    loop: true,
    direction: 'horizontal',
    mousewheelControl: true,
    parallax: false,
    // spaceBetween:-20,
    speed: 600,
    coverflowEffect: {
        rotate: 0,
        stretch: 0,
        depth: 130,
        modifier: 2.5,
        slideShadows: false,
    },
    mousewheel: {
        sensitivity: 2,
    }
});


//////////////////////////////////////////////////////////////////////////// Why Choose Sliderhome

var swiper = new Swiper(".why_choose_sliderhome_swiper", {
    spaceBetween: 30,
    centeredSlides: true,
    loop: true,
    autoplay: {
        delay: 4000,
        disableOnInteraction: false,
    },
    pagination: {
        el: ".swiper-pagination",
        clickable: true,
    },
});



//////////////////////////////////////////////////////////////////////////// Form js

// Example starter JavaScript for disabling form submissions if there are invalid fields
(() => {
    'use strict'

    // Fetch all the forms we want to apply custom Bootstrap validation styles to
    const forms = document.querySelectorAll('.needs-validation')

    // Loop over them and prevent submission
    Array.from(forms).forEach(form => {
        form.addEventListener('submit', event => {
            if (!form.checkValidity()) {
                event.preventDefault()
                event.stopPropagation()
            }

            form.classList.add('was-validated')
        }, false)
    })
})()


//////////////////////////////////////////////////////////////////////////// maxlength 
function validateNumber(input) {
    if (input.value.length > 10) {
        input.value = input.value.slice(0, 10); // Restrict to 10 digits
    }
}


//////////////////////////////////////////////////////////////////////////// Counter Section

document.addEventListener("DOMContentLoaded", function () {
    const counters = document.querySelectorAll(".counter-number");

    counters.forEach(counter => {
        let target = +counter.getAttribute("data-target");
        let count = 0;
        let speed = target / 50; // Adjust speed

        function updateCounter() {
            if (count < target) {
                count += speed;
                counter.innerText = Math.ceil(count);
                setTimeout(updateCounter, 50);
            } else {
                counter.innerText = target + "+"; // Add "+" at the end
            }
        }

        updateCounter();
    });
});