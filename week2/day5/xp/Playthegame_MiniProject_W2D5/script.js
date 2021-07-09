
let userName;
let changeHeader = document.getElementById("name");
function getPlayerName() {
    let isWord = true;
    while(isWord){
        userName = prompt("What is your Username? ");
        if(!isNaN(userName)){
            alert("Please do not enter numbers before your name")
        }else if(userName.length < 3){
            alert("Please enter a username with at least 3 characters!")
        }else{
            isWord = false
        }
    }
}


function playTheGame(){
    let computerNum;
    let userNum;
    let play = confirm("Hello, would you like to play? ")
    if(play == false){
        alert("No problem, Goodbye")
    }else{
        let isNum = true;
        getPlayerName();
        while (isNum) {
            userNum = parseInt(prompt(`Ok ${userName}, enter a number between 0 and 10: `))
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
    for(let times = 3; times >= 1; times--){
        if(userNumber != undefined){
            if(userNumber === computerNumber){
                alert("Winner!")
                changeHeader.innerText = `${userName} won!!`;
                changeHeader.style.color = "green";
                document.querySelector(".a").style.display = "block"
                break
            }else if(userNumber > computerNumber){
                alert("Your number is bigger then the computer’s, guess again");
                let isNum = true;
                while (isNum) {
                    userNumber = parseInt(prompt("Enter a new number between 0 and 10: "))
                    if(isNaN(userNumber) ){
                        alert("Sorry Not a number, try again")
                    }else if(userNumber >= 10 || userNumber == 0){
                        alert("Invalid number")
                    }else{
                        isNum = false;
                    }
                }     
                
            }else{
                alert("Your number is less then the computer’s, guess again");
                let isNum = true;
                while (isNum) {
                    userNumber = parseInt(prompt("Enter a new number between 0 and 10: "))
                    if(isNaN(userNumber) ){
                        alert("Sorry Not a number, try again")
                    }else if(userNumber >= 10 || userNumber == 0){
                        alert("Invalid number")
                    }else{
                        isNum = false;
                    }
                }   
            }
            if(times == 1){
                alert("Out of chances!")
                changeHeader.innerText = `${userName} lost!\n Computer : 1\n humans: 0 `;
                changeHeader.style.color = "red";
                document.querySelector(".b").style.display = "block"
    
            }
        }
        
    }
}

function play() {
    let a = playTheGame()
    test(a.userNum1, a.computerNum1)
}