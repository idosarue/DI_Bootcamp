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



let mouseDown;


elementsArray.forEach(function(elem) {
    elem.addEventListener('mousedown', function () {
        mouseDown = true
    })
    elem.addEventListener('mouseup', function () {

        mouseDown = false

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


