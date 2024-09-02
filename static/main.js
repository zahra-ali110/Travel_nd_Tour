let menu=document.querySelector('#menu-btn');
let navbar=document.querySelector('.header .navbar');

menu.onclick = () =>{
	menu.classList.toggle('fa-times');
	navbar.classList.toggle('active');
}

window.onscroll = () =>{
	menu.classList.remove('fa-times');
	navbar.classList.remove('active');
};

var swiper = new Swiper(".home-slider", {
      loop:true,
      navigation: {
        nextEl: ".swiper-button-next",
        prevEl: ".swiper-button-prev",
      },
    });

var swiper = new Swiper(".reviews-slider", {
       grabCursor:true,
       loop:true,
       spaceBetween: 20,
       breakpoints: {
        0: {
          slidesPerView: 1,
          spaceBetween: 20,

        },
        700: {
          slidesPerView: 2,
          spaceBetween: 20,
        },
        1000: {
          slidesPerView: 3,
          spaceBetween: 20,
        },
      },
    });

let loadMoreBtn = document.querySelector('#loadmore button'); // Adjusted selector
let currentItem = 3;

loadMoreBtn.onclick = (event) => {
    event.preventDefault(); // Prevent default action
    let boxes = [...document.querySelectorAll('.home-packagess .box-container .boxx')];
    for (var i = currentItem; i < currentItem + 3; i++) {
        if (i < boxes.length) {
            boxes[i].style.display = 'inline-block';
        }
    }
    currentItem += 3;
    if (currentItem >= boxes.length) {
        loadMoreBtn.style.display = 'none';
    }
}


