const viewButton1 = document.getElementById("viewButton1");

viewButton1.addEventListener("click", () => {
    // Replace 'sample.pdf' with the actual PDF file URL you want to view
    window.open("SHAIBINCV.pdf", "_blank");
});
const viewButton2 = document.getElementById("viewButton2");

viewButton2.addEventListener("click", () => {
    // Replace 'sample.pdf' with the actual PDF file URL you want to view
    window.open("SHAIBINCV.pdf", "_blank");
});
const viewButton3 = document.getElementById("viewButton3");

viewButton3.addEventListener("click", () => {
    // Replace 'sample.pdf' with the actual PDF file URL you want to view
    window.open("SHAIBINCV.pdf", "_blank");
});

const header =document.querySelector("header")

window.addEventListener("scroll",function(){
    header.classList.toggle ("sticky",window.scrolly > 120);
});

let menu = document.querySelector('#menu-icon');
let navlist = document.querySelector('.navlist');

menu.onclick = () => {
    menu.classList.toggle('bx-x');
    navlist.classList.toggle('active');
};

window.onscroll = () => {
    menu.classList.remove('bx-x');
    navlist.classList.remove('active');
};

window.onscroll


