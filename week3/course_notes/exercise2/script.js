let div = document.querySelector("#container");
console.log(div)

let div2 = document.body.firstElementChild
console.log(div2)

let lists = document.getElementsByClassName("list");
console.log(lists)

// let first = lists[0]
// console.log(first)
// let second = lists[1]
// console.log(second)

for(items of lists){
    console.log(items)
}