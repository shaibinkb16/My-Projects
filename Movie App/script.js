const APIURL ="https://api..othemoviedbrg/3/discover/movie?sort_by=popularity.desc&api_key=04c35731a5ee918f014970082a0088b1&page=";
const IMGPATH = "https://image.tmdb.org/t/p/w1280";
const SEARCHAPI =
    "https://api.themoviedb.org/3/search/movie?&api_key=04c35731a5ee918f014970082a0088b1&query=";
const btn=document.getElementById('bt');
const search=document.getElementById('search');
const form=document.getElementById('form');
const main=document.querySelector('.main');

getMovies(APIURL);

async function getMovies(url){ 
    const resp=await fetch(url);  
    const respData=await resp.json();
    console.log(respData);
    showMOvies(respData.results)
}

    function showMOvies(movie){
        main.innerHTML=""
         movie.forEach((movie) => {
        const {poster_path,title,vote_average}=movie;
        const movieEl=document.createElement('div');
        movieEl.classList.add('movies')
        movieEl.innerHTML=`
        <img src="${IMGPATH+ poster_path}">
        <div class="movie-name">
            <p>${title}</p>
            <span class=" ${getcolour(vote_average)}">${vote_average}</span>
        </div>`
        main.appendChild(movieEl)
        
    });
}
form.addEventListener("submit", (e) => {
    e.preventDefault();
    const searchTerm = search.value;
    if (searchTerm) {  
        getMovies(SEARCHAPI + searchTerm);
        console.log(SEARCHAPI+searchTerm)
        search.value = "";      
    }
    else
    {
        alert("Please enter Movie name...!")
    }
});

let page=1;

btn.addEventListener("click",()=>{
   geeks();
    page++;
    getMovies(APIURL+page);
    console.log(APIURL+page);
    
});

geeks(); 

   function geeks(){
    window.scroll(0,0 );
   }

function getcolour(vote){
    if(vote>=7)
    {
       return "green";
    }
    else
    if (vote>=4) {
       return "orange";
    } else {
        return "red";
    }
}
