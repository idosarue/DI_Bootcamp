//1
let lastP = document.getElementsByTagName("article")[0].lastElementChild;
lastP.remove()


//2
let h2 = document.getElementsByTagName("h2")[0]
h2.addEventListener("click",function () {
    h2.style.backgroundColor = "red"
})

//3
let h1 = document.getElementsByTagName("h1")[0]
h1.addEventListener("click",function () {
    h1.style.fontSize =  Math.floor((Math.random() * 100) + 1) +"px"
})

//4
let h3 = document.getElementsByTagName("h3")[0]
h3.addEventListener("click",function () {
    h3.style.display ="none"
})

//5
let button = document.createElement("button");
button.innerHTML = "Change font"
document.body.appendChild(button)
button.addEventListener("click", changeToBold);
function changeToBold() {
    document.body.style.fontWeight = 'bold'
}

//6
let submit = document.getElementById("submit")
submit.addEventListener("click", getValues);

function getValues(event) {
    let form = document.getElementsByTagName("form")[0]
    console.log(form)
    let valueFname = form.elements.fname.value;
    console.log(valueFname)
    let valueLname = form.elements.lname.value;
    console.log(valueLname)
    if(valueFname.length < 4 || valueLname < 4){
        alert("please fill in at least 4 characters")
    }else{
        let div = document.getElementsByClassName("usersAnswer")[0];
        let table = document.createElement("table");
        let row = table.insertRow(0)
        var cell1 = row.insertCell(0);
        var cell2 = row.insertCell(1);
        cell1.innerHTML = valueFname
        cell2.innerHTML = valueLname
        div.appendChild(table)
    }
    event.preventDefault()
}

// 7
let secondP = document.getElementsByTagName("p")[1]
console.log(secondP)
secondP.addEventListener("mouseover", function () {
    secondP.style.opacity = "0.2"
    secondP.style.transition = "0.3s"
});

secondP.addEventListener("mouseout", function () {
    secondP.style.opacity = "1"
    secondP.style.transition = "0.3s"
});
