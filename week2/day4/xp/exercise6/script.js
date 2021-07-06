let sum;
function changeEnough([quarters, dimes, nickels, pennies], price){
    quarters  = 0.25 * quarters;
    dimes = 0.10 * dimes;
    nickels = 0.05 * nickels;
    pennies = 0.01 * pennies;
    sum = quarters + dimes + nickels + pennies;
    console.log(sum > price)
}

changeEnough([2, 100, 0, 0], 14.11); 