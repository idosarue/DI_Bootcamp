// let boxRed = document.getElementById("box1")
let color;
let id;

let elementsArray = document.querySelectorAll(".box");


function clearB() {
    for(let i of elementsArray){
        let newColor = document.createAttribute('style')
        newColor.value = 'white';
        i.setAttributeNode(newColor)
    }
   
}

// document.getElementById("demo").addEventListener("mousedown", mouseDown);
// document.getElementById("demo").addEventListener("mouseup", mouseUp);

// function mouseDown() {
//   document.getElementById("demo").innerHTML = "The mouse button is held down.";
// }

// function mouseUp() {
//   document.getElementById("demo").innerHTML = "You released the mouse button.";
// }

let mouseDown;

// let mouseDown;
elementsArray.forEach(function(elem) {
    elem.addEventListener('mousedown', function () {
        mouseDown = true
        console.log(mouseDown)

    })
    elem.addEventListener('mouseup', function () {
        mouseDown = false
        console.log(mouseDown)
    })

    elem.addEventListener("mouseover", function() {
        let newColor = document.createAttribute('style')
        newColor.value = color;
        elem.setAttributeNode(newColor)
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


// function AppendColor(e) {
//     id = e.target.id
//     console.log(id)
//     let newColor = document.createAttribute('style')
//     box = document.getElementById(id)
//     newColor.value = color;
//     box.setAttributeNode(newColor)
//     console.log(box)
// }