const questions=[{
    question:"Who is the Primeminister of India ?",
    a:"Shaibin KB",
    b:"Nibin Jacob",
    c:"Jubin BIju",
    d:"narendra modi",
    correct:"ans-a"
},
{
    question:"What is 2+2 ?",
    a:"4",
    b:'6',
    c:"5",
    d:"7",
    correct:"ans-a"
},
{
    question:"Who is the ?",
    a:"cat",
    b:"Monkey",
    c:"donkey",
    d:"elephant",
    correct:"ans-d"
}];

const questionEl=document.getElementById("question");
const A=document.getElementById("a");
const B=document.getElementById("b");
const C=document.getElementById("c");
const D=document.getElementById("d");
const submit=document.getElementById("btn");
const answers=document.querySelectorAll(".answer");
const last=document.getElementById("quiz-con")


let currentQuestion=0;
let score=0;
LoadQuestions();


function LoadQuestions(){
deselected()

    const currentquizData=questions[currentQuestion];
    questionEl.innerText=currentquizData.question;
    A.innerText=currentquizData.a
    B.innerText=currentquizData.b
    C.innerText=currentquizData.c
    D.innerText=currentquizData.d
};

function getdata(){
   let answerid="";

    answers.forEach((answer)=>{
        if(answer.checked)
        {
         answerid=answer.id;
        }
    });
    return answerid;
}

function deselected(){
    answers.forEach((answer)=>{
    answer.checked=false;
        });
}


submit.addEventListener("click",()=>{
    const answergot= getdata();

    if(answergot){
        if(answergot===questions[currentQuestion].correct)
        {score++;}
        console.log(score)
        currentQuestion++;
        if(currentQuestion < questions.length)
    {
        LoadQuestions(); 
    }
    else
    {
        last.innerHTML=`<h1>You have completed your test</h1><br><br>
        <h2>your score is ${score}/${questions.length}</h2>`

         btn.innerText=`Reload`
         btn.addEventListener("click",()=>{
            location.reload();
         })
        
    }
    
}});


