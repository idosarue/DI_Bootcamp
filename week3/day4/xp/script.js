// let boxRed = document.getElementById("box1")
let color;
let id;


let side = document.getElementById('side')

function addSDiv(){
  let colors = ["red", "yellow", "blue", "cyan", "black", "green", "grey","violet", "yellow", "salmon", "almond", "black", "green", "grey","red", "yellow", "blue", "almond", "black", "green", "grey"]
  for (let i = 0; i < 21; i++) {
    let div = document.createElement('div');
    let style = document.createAttribute('style');
    style.value = `background-color: ${colors[i]}`
    div.setAttribute("class", "red");
    div.setAttribute("id", colors[i]);
    div.setAttributeNode(style)
    side.appendChild(div);  

  }
}

addSDiv()

let main = document.getElementById('main')

function addDiv(){
  
  for (let i = 0; i < 1700; i++) {
    let appendDiv = document.createElement('div');
    appendDiv.setAttribute("class", "box");
    main.appendChild(appendDiv);  

  }
}

addDiv()
let elementsArray = document.querySelectorAll(".box");
function clearB() {
    for(let i of elementsArray){
        let newColor = document.createAttribute('style')
        newColor.value = 'white';
        i.setAttributeNode(newColor)
    }
   
}



let mouseDown;

window.addEventListener('mouseup', function () {
    mouseDown = false
})

elementsArray.forEach(function(elem) {
    elem.addEventListener('mousedown', function () {
        
        mouseDown = true

    })

    elem.addEventListener("mouseover", function() {
        if(mouseDown){
            let newColor = document.createAttribute('style')
            newColor.value = color;
            elem.setAttributeNode(newColor)
        }
        

    });

});


let elementsArray2 = document.querySelectorAll(".red");
elementsArray2.forEach(function(elem) {
    elem.addEventListener("click", function(e) {
    id = e.target.id
    boxRed = document.getElementById(id);
    color = boxRed.getAttribute('style')
    console.log(color)
    });
});


