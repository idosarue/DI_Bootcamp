
/*Add a “light blue” background color and some padding to the <div>.
Do not display the first name (John) in the list.
Add a border to the second name (Pete).
Change the font size of the whole body.
Bonus: If the background color of the div is “light blue”, alert “Hello x and y” (x and y are the users in the div).*/

//1
let div = document.querySelector("div")
div.style.backgroundColor = 'lightblue'
div.style.padding = '10px'
//2
let ul = document.querySelectorAll("li");
let john = ul[0]
john.style.display = 'none'
//3
let pete = ul[1]
pete.style.border="1px solid"

//4
document.body.style.backgroundColor = 'red'