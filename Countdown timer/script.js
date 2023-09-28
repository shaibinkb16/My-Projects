
const day=document.getElementById("days")
const hour=document.getElementById("hours")
const minute=document.getElementById("minutes")
const second=document.getElementById("seconds")

function read(){
    const dataEnterd=document.getElementById("btn").value

function newYear(){
    setInterval(() => {
        var deadline =new Date(dataEnterd)
        var now=new Date();
        var timeLeft=deadline-now;
        var days =Math.floor(timeLeft/(1000*60*60*24));
        var hours=Math.floor((timeLeft%(1000*60*60*24)/(1000*60*60)));
        var minutes=Math.floor((timeLeft%(1000*60*60)/(1000*60)));
        var seconds=Math.floor((timeLeft%(1000*60)/1000)); 

/*  */
        day.innerText=days;
        hour.innerText=hours;
        minute.innerText=minutes
        second.innerText=seconds
    
    }, 1000)
   
}
newYear();

}