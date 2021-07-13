// timeout
setTimeout(wait, 2000)// func, miliseconds

function wait(){
    console.log('from a wait function')
}

// something.adddEventListenet('click', function(){
//     setTimeout(wait,3000)
// })
let id;

function wait2() {
    console.log('berfore waiting')
    id = setTimeout(function () {
        console.log('helooooo after 2')
    },2000)
}

function cancel() {
    clearTimeout(id)
}