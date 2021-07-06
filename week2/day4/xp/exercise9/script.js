

function hotelCost() {
    let isNum = true; 
    let pricePerNight = 140;
    while (isNum) {
        let nightNum = parseInt(prompt("How many nights? "));
        if(isNaN(nightNum)){
            alert("not a number");
        }else{
            isNum = false;
            return nightNum * pricePerNight;
        }
    }
}


function planeRideCost() {
    let isStr= true; 
    let london = 183;
    let paris = 220;
    let other = 300;
    while (isStr) {
        let destination = prompt("What is your destination? ").toLowerCase();
        if(!isNaN(destination)){
            alert("not a word..");
        }else{
            isStr = false;
            if(destination == "paris"){
                return paris;
            }else if(destination == "london"){
                return london;
            }else{
                return other;
            }
        }
    }
}


function rentalCarCost() {
    let isNum = true; 
    let carCost = 40;
    let sum;
    while (isNum) {
        let numOfDays = parseInt(prompt("How many days do you want ther rent the car for?  "));
        if(isNaN(numOfDays)){
            alert("not a number");
        }else{
            isNum = false
            sum = numOfDays * carCost;
            if(numOfDays < 10){
                return sum
            }else{
                return sum -= sum * 0.05
            }
        }
    }
}
function totalVacationCost(){
    let total = hotelCost() + planeRideCost() + rentalCarCost();
    return `your total is $${total}`
}

console.log(totalVacationCost())