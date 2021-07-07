// Exercise 1
function ageCalc(MyAge=23){
    if(isNaN(MyAge)){
        console.log("not a number");
    }else{
        let momAge = MyAge *2;
        let dadAge = Math.round(momAge *1.2);    
        console.log(`My dad's age is ${dadAge}`); 
        console.log(`My mom's age is ${momAge}`);
    }


}
ageCalc(24)

// Exercise 2

function ageCalc2(MyAge=23){
    let momAge = MyAge *2;
    return`My mom's age is ${momAge}`;
}
console.log(ageCalc2(24));
