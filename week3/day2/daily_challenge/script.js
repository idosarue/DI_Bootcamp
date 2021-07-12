//1  Get the value of each of the inputs in the HTML file when the button is clicked.
//2 Make sure the values are not empty
// 3 Write a story that uses each of the values.
// 4 Make sure you check the console for errors when playing the game.


let button = document.getElementById("lib-button")
button.addEventListener("click", libIt)
let span = document.getElementById("story")
let input = document.querySelectorAll("input")

function libIt() {
    let nounValue = input[0].value;
    let adjValue = input[1].value;
    let nameValue = input[2].value;
    let verbValue = input[3].value;
    let placeValue = input[4].value;
    let sentence = `${nounValue} ${adjValue} ${nameValue} ${verbValue} ${placeValue}`
    if(nounValue.length < 3 || adjValue.length < 3 || nameValue.length < 3 || verbValue.length < 3 || placeValue.length < 3){
        alert('please fill in all forms with at least 3 characters!')
    }else{
        span.innerHTML = sentence
    }
}

let newButton = document.createElement("button");
newButton.innerHTML = "Shuffle it!"
document.body.appendChild(newButton)
newButton.addEventListener('click', shuffle)
function shuffle() {
    libIt()
    let x= [];
    for(let item of input){
        let values = item.value
        x.push(values)
        x.sort(() => Math.random() - 0.5);
        
    }
    let newSent = x.join(' ')
    span.innerHTML = newSent
}

