// Exercise 1 : Building Management
let building = {
    numberLevels : 4,
    numberOfAptByLevel : {
        "1": 3,
        "2": 4,
        "3": 9,
        "4": 2,
    },
    nameOfTenants : ["Sarah", "Dan", "David"],
    numberOfRoomsAndRent:  {
        "Sarah": [3, 990],
        "Dan":  [4, 1000],
        "David": [1, 500],
    },
}
console.log(building["numberLevels"]);
console.log(building["numberOfAptByLevel"]["1"],building["numberOfAptByLevel"]["3"]);
console.log(building["numberOfRoomsAndRent"]["Dan"]);
let sarahRent = building["numberOfRoomsAndRent"]["Sarah"][1];
let davidRent = building["numberOfRoomsAndRent"]["David"][1];
let danRent = building["numberOfRoomsAndRent"]["Dan"][1];

let rentSum = sarahRent + davidRent;
if(rentSum > danRent){
  danRent = 1200;
  console.log(danRent);
}