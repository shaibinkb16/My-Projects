const btnEL= document.getElementById("btn");
const jokeEL = document.getElementById('joke');

const apiKey = "Va251JHzY0voum4LT/Sj4A==SyW2WVBosOpCVg8R";

const options= {
    method :"GET",
    headers : {
        "X-Api-Key":apiKey
    },
};

const apiURL = "https://api.api-ninjas.com/v1/dadjokes?limit=1" ;

 async function getJoke()
{
    jokeEL.innerText="Updating...";
    btnEL.disabled=true;
    btnEL.innerText="Loading...";
    const response =  await fetch(apiURL,options);
    const data = await  response.json();

    btnEL.disabled=false;
    btnEL.innerText="TELL ME A JOKE";

    jokeEL.innerText = data[0].joke;
}

btnEL.addEventListener("click",getJoke);