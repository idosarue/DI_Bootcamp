const numbers = [5,0,9,1,7,4,2,6,3,8];
let str = numbers.toString();
console.log(str);
let newArr = numbers.join("+");
console.log(newArr)

let temp = 0;
let a = numbers[0];
let n = [];
for(let num = 0; num <= a; num++){
    if(numbers[num]> a){
        a = numbers[num];
        numbers[0] = a;
        


    }else if(numbers[num] < a){

    }
    for(let i = 0; i < numbers.length; i++){
        if(numbers[i] < a){
            n.push(numbers[i])
        }
    }
   
}
console.log(a)
console.log(numbers)
