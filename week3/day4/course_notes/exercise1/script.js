
button.addEventListener("click", insertRow())
let button = document.querySelector("input");

function insertRow(event) {
    let element = event.target
    let table = document.querySelector("table").children[0];
    let row = document.createElement("tr")
    for(let i = 0; i < 2; i++){
        let cell = document.createElement("td")
        row.append(cell)
        cell.textContent = "hey"
    }
    
table.appendChild(row)
}

