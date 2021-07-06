/*Create two objects, each object should hold a persons details. Here are the details:
FullName
Mass
Height
Each object should also have a key which value is a function (ie. A method), that calculates the Body Mass Index (BMI) of each person
Outside of the objects, create a JS function that compares the BMI of both objects.
Display the name of the person who has the largest BMI.*/


let person1 = {
    FullName : "John Doe",
    Mass : 80,
    Height : 1.80,
    bmi : " "
};

let person2 = {
    FullName : "Jane Doe",
    Mass : 60,
    Height : 1.60,
    bmi : " "
    
};

let person1Weight = person1["Mass"];
let person1Height = person1["Height"];
let person2Weight = person2["Mass"];
let person2Height = person2["Height"];


function bmiCalc1(x,y) {
    bmi = x /(y * y);
    person1["bmi"] = bmi
    return bmi
}

function bmiCalc2(x,y) {
    bmi = x /(y * y);
    person2["bmi"] = bmi
    return bmi
}
bmiCalc1(person1Weight, person1Height);
console.log(person1["bmi"]);
bmiCalc2(person2Weight, person2Height);
console.log(person2["bmi"]);

function bigBmi() {
    if(person1["bmi"] > person2["bmi"]){
        console.log(person1["FullName"])
    }else {
        console.log(person2["FullName"])
    }
}
bigBmi();