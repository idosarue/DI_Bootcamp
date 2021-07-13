const dragElement = document.getElementById('box')
const area = document.getElementById('drop-area')

dragElement.addEventListener('dragstart', dragstart_handler)

area.addEventListener('dragover', dragover_handler)

area.addEventListener('drop', drop_handler)


function dragstart_handler(e) {
    e.dataTransfer.setData('text/plain', e.target.id)//getting id from the element
    console.log(e.target.id)
}

function dragover_handler(e) {
    e.preventDefault();
    e.dataTransfer.dropEffect ='move'
    area.classList.add('highlight')
}


function drop_handler(e) {
    e.preventDefault()
    area.classList.remove('highlight')
    const data = e.dataTransfer.getData('text/plain')
    console.log(data)
    e.target.appendChild(document.getElementById(data))
}