// Exercise 1 : Your Favorite Colors
let counter = 0;
let colors = ["red", "blue", "green", "brown"];
let suf = ["1st", "2nd" ,"3rd", "4th"]
for(i=0; i < colors.length; i++){
    counter++
    console.log(`my #${counter} choice is ${colors[i]}`);
    console.log(`my ${suf[i]} choice is ${colors[i]}`);
}

// Exercise 2 : List Of People
let people = ["Greg", "Mary", "Devon", "James"];
people.shift();
console.log(people);
people.splice(2, 1, "jason");
console.log(people);
people.push("ido");
console.log(people);

for(i = 0; i < people.length; i++){
    console.log(people[i]);
}

for (let i = 0; i < people.indexOf("jason")+1; i++) {
    console.log(people[i]);
}

// [mary, devon, jason, ido]

let newPeople = people.slice(1,3);
console.log(newPeople);

console.log(people.indexOf("Mary"));

console.log(people.indexOf("Foo"));// returns -1 because Foo does not exist in the Array people

let last = people[people.length -1];
console.log(last);

// Exercise 3 : Repeat The Question
let userNum;
do {
    userNum = parseInt(prompt("Enter a number: "));
}
while (userNum < 10);
    

// Exercise 4 : Attendance
let guestList = {
    randy: "Germany",
    karla: "France",
    wendy: "Japan",
    norman: "England",
    sam: "Argentina"
  };

let studentName = prompt("Enter your name: ").toLowerCase();

if(studentName in guestList){
    console.log(`Hi! I'm ${studentName}, and I'm from ${guestList[studentName]}.`)
}else {
    console.log("Hi! I'm a guest.");
}

// Exercise 5 : Family

let family = {
    dad : "John",
    mom : "Jane",
    son : "Doe"

};

for(let i in family){
    console.log(i, family[i]);
}

// Exercise 6
let details = {
    my: 'name',
    is: 'Rudolf',
    the: 'raindeer'
  };


let a = Object.keys(details)
let b = Object.values(details)
console.log(`${a[0]} ${b[0]} ${a[1]} ${b[1]} ${a[2]} ${b[2]}`)

// Exercise 7 : Secret Group
let names = ["Jack", "Philip", "Sarah", "Amanda", "Bernard", "Kyle"]
let secret = [];
for(i in names){
    let x = names[i][0];
    secret.push(x);
    
    
}
let a = secret.join("")
console.log(a.toString());