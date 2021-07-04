var userNum = prompt("Enter numbers seperated by commas: ");
var arrNum = userNum.split(",");
console.log(arrNum);
var arr = [];
for( i = 0 ; i < arrNum.length ; i++){
  var num = parseInt(arrNum[i])
  arr.push(num)
}

let sum = 0

for(i = 0; i < arr.length ; i++){
  sum += arr[i];
}

console.log(sum)