//1
let lists = document.getElementsByClassName("list");

lists[0].lastElementChild.textContent = "Richard"
//2
for(let i = 0; i<lists.length; i++){
    lists[i].firstElementChild.textContent = "ido"
}

//3 

for(let i = 0; i <lists.length; i++){
    let newLi = document.createElement("li");
    let node = document.createTextNode("Hey students");
    newLi.appendChild(node)
    lists[i].append(newLi)
}

//4
let second = lists[1]
let sarah = second.children[1]

second.removeChild(sarah)

