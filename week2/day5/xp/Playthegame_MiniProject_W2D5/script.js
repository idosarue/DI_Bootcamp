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


function test(userNumber, computerNumber) {
    let a = playTheGame();
    for(let times = 0; times < 3; times++){
        times +=1
        userNumber = a.userNum1
        computerNumber = a.computerNum1
        console.log("user", userNumber)
        console.log("Cmputer", computerNumber)
        if(userNumber === computerNumber && userNumber != 0){
            alert("Winner!")
            times += 3
        }else if(userNumber > computerNumber){
            alert("Your number is bigger then the computer’s, guess again");
            userNumber = parseInt(prompt("Enter a new number: "))
        }else {
            alert("Your number is less then the computer’s, guess again");
            userNumber = parseInt(prompt("Enter a new number: "))
        }
        if (times === 3) {
            alert("you lost!")
        }
        console.log("times", times)
    }

}