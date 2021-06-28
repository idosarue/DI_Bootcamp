

function changeBackground() {
    var main = document.querySelector(".main");
    var button = document.querySelector("button");
    var heading = document.querySelector("h1");
    if(button.innerText == "Suit Up") {
        heading.innerHTML = "Iron man";
        button.innerText = "Remove suit";
        main.style.backgroundImage = "url('https://thumbor.forbes.com/thumbor/960x0/https%3A%2F%2Fblogs-images.forbes.com%2Falishagrauso%2Ffiles%2F2016%2F05%2FIron-Man-Robert-Downey-Jr-Interview-1200x600.jpg')";
        
    }else if(button.innerText == "Remove suit") {
        button.innerText = "Suit Up";
        heading.innerHTML = "Tony Stark";
        main.style.backgroundImage = "url('https://wallup.net/wp-content/uploads/2018/03/20/195534-Iron_Man-Tony_Stark-Robert_Downey_Jr.-748x421.jpg')";
    }
}

