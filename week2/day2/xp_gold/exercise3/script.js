let verb = prompt("Enter a verb: ")
let verbLen = verb.length;
let verbSub = verb.substr(-3, verbLen);
let end ="ing"
console.log(verbSub)

if(verbLen >= 3 && verbSub != end){
    console.log(`${verb}${end}`);
}else if(verbLen >= 3 && verbSub == end){
    console.log(`${verb}ly`)
}else {
    console.log(verb);
}