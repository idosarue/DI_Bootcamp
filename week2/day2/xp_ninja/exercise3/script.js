let userWord = prompt("enter a word: ")
let a = /[a]/g;
let e = /[e]/g;
let i = /[i]/g;
let o = /[o]/g;
let u = /[u]/g;

let newW = userWord.replace(a, "1").replace(e, 2).replace(i,3).replace(o, 4).replace(u, 5);
console.log(newW)

