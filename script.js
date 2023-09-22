const ratingEls=document.querySelectorAll(".rateing");
const buttonSL=document.getElementById("btn");
const containerEL=document.getElementById("container");
const imge=""
let selectedRating="";
ratingEls.forEach((ratingEl) => {
    ratingEl.addEventListener("click",(event) => {
       removeEL();  
       selectedRating=event.target.innerText; 
       selectedRating=event.target.parentNode.innerText;                                                                                                                                                
        event.target.classList.add("active")
        event.target.parentNode.classList.add("active")
    });
});

buttonSL.addEventListener("click",() => {
  if(selectedRating !== "")
  {
    containerEL.innerHTML=`<strong>Thank You!</strong>
    <br>
    <br>
    <strong> Feedback:${selectedRating}
    <p>We will try our best next time<p>`
    
    }
  })

function removeEL(){
    ratingEls.forEach((ratingEl) => {
        ratingEl.classList.remove("active");
    })
}
console.log(imge)