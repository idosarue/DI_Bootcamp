/*Exercise 3 : Calculator
Instructions
Make a Calculator. Follow the instructions:

Prompt the user for the first number.
Store the first number in a variable called num1.
Prompt the user for the second number.
Store the second number in a variable called num2.
Create an Alert where the value is the SUM of num1 and num2.
BONUS: Make a program that can subtract, multiply, and also divide!*/
function calc() {
    let num1 = parseFloat(prompt('Enter a number: '));
    if (isNaN(num1)) {
        alert('not a number')
    }else {
        let user_oper = prompt('enter operator');
        let num2 = parseFloat(prompt('Enter another number: '));
        if (user_oper == '+'){
            alert(num1 + num2)       
        } else if (user_oper == '-'){
            alert(num1 - num2)       
        } else if (user_oper == '*'){
            alert(num1 * num2)
        } else if (user_oper == '/'){
            alert(num1 / num2)
        }
    }

}

calc();