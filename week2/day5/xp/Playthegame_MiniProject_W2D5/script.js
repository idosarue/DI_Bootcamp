function playTheGame(){
    let computerNum;
    let userNum;
    let play = confirm("Would you like to play? ")
    if(play == false){
        alert("No problem, Goodbye")
    }else{
        let isNum = true;
        while (isNum) {
            userNum = parseInt(prompt("Enter a number between 0 and 10: "))
            if(isNaN(userNum) ){
                alert("Sorry Not a number, try again")
            }else if(userNum >= 10 || userNum == 0){
                alert("Invalid number")
            }else{
                isNum = false;
                computerNum = Math.floor(Math.random() * 9) + 1;
            }   
        }           
    }
  let obj = {
    computerNum1 : computerNum,
    userNum1 : userNum
  }
  return obj;
}

let a;
function test(userNumber = a.userNum1, computerNumber = a.computerNum1) {
    let a = playTheGame();
    console.log(userNumber)
    console.log(computerNumber)
    if(userNumber == computerNumber){
        alert("Winner")
    }else if(userNumber > computerNumber){
        alert("Your number is bigger then the computer’s, guess again");
        let newNum = parseInt(prompt("Enter a new number: "))
        userNumber = newNum
    }
}
test(a.userNum1, a.computerNum1)