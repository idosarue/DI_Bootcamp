//1
let divId = document.querySelector("div");
divId.setAttribute("id", "socialNetworkNavigation");
console.log(divId)

//2

//2.1
let newLi = document.createElement("li");

//2.2
let node = document.createTextNode("Logout");

//2.3
newLi.appendChild(node)
//2.4
let list = document.querySelector("ul");
list.appendChild(newLi);

//3 
let listFirst = list.firstElementChild.textContent;
console.log(listFirst)
let listLast = list.lastElementChild.textContent;
console.log(listLast)



