//1  Create a function called getBold_items() that takes no parameter.
//  This function should collect all the bold items inside the paragraph.

//2 Create a function called highlight() that changes the color of all the bold text to blue.

//3 Create a function called return_normal() that changes the color of all the bold text back to black.

//4 Call the function highlight() onmouseover (ie. when the mouse pointer is moved onto the paragraph),
//  and the function return_normal() onmouseout
//  (ie. when the mouse pointer is moved out of the paragraph). Look at this example----

let para = document.getElementsByTagName("p")[0]

let arr = [];
function getBold_items() {
    
    let strong = para.querySelectorAll("Strong");
    let strongTag;
    for(let i = 0; i<strong.length; i++){
        strongTag = strong[i]
        arr.push(strongTag)
    }

return arr
}

para.addEventListener("mouseover", highlight)
function highlight(){
    getBold_items()
    for(const element of arr){
        element.style.color = "blue"
    }
}


para.addEventListener("mouseout", return_normal)

function return_normal(){
    getBold_items()
    for(const element of arr){
        element.style.color = "black"
    }
}