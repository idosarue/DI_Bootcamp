// Exercise 3 : Playing With Numbers
let age = [20,5,12,43,98,55];
let sum = 0;
for(let x in age){
    sum += age[x]
}
console.log(sum)

let largest = age[1]
for(let i = 0; i<= largest; i++ ){
    if(age[i]> largest){
        largest = age[i]
    }
}
console.log(largest)