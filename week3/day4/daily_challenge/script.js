let listTasks = []
let input = document.getElementById('myForm').firstElementChild
let div = document.getElementsByTagName('div')[0]
console.log(input)
function addTask(event) {
    event.preventDefault();
    let inputValue = input.value
    if (inputValue < 1) {
        alert('please fill')
    }else{
        console.log(inputValue)
        let para = document.createElement('p')
        console.log(para)
        let checkBox = document.createElement('input')
        let icon = document.createElement('i')
        let hr = document.createElement('hr')
        icon.className = 'far fa-calendar-times'
        checkBox.setAttribute("type", "checkbox")
        listTasks.push(inputValue)
        para.textContent = inputValue
        div.appendChild(para)
        para.appendChild(icon)
        para.appendChild(checkBox)
        
        div.appendChild(hr)


    }
    
}
