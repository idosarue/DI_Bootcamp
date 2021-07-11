let first = document.body.firstElementChild
console.log(first)

let first2 = document.body.children[0]
console.log(first2)

let second = document.body.children[1]
console.log(second)

let second2 = document.body.firstElementChild.nextElementSibling
console.log(second2)

let third = second.children[1]
console.log(third)

let third2 = second.lastElementChild
console.log(third2)