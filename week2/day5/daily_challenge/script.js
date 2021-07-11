let bottles;
function check(){
    bottles = +prompt("enter number of bottles: ")
    while (isNaN(bottles)) {
        bottles = +prompt("not a number, enter number of bottles: ")
    }
}
function countBottles() {
    check()
    let counter = 1;
    for(let i = bottles; i > 0 && bottles >= 0; i--){
        console.log( `${bottles} of beer on the wall\n${bottles} of beer`)
        if(counter < bottles){
            bottles-=counter    
            if(counter == 1){
                console.log(`take ${counter} down pass it around`)
                console.log( `${bottles} bottles of beer on the wall`)
            }else if(counter > 1){
                console.log(`take ${counter} down pass them around`)
                console.log( `${bottles} bottles of beer on the wall`)
            }
        counter+=1
        }else{
            counter = bottles
            if(counter == 1){
                console.log(`take ${counter} down pass it around`)
            }else{
                console.log(`take ${counter} down pass them around`)
            } 
            console.log( `${bottles - counter} bottles of beer on the wall`)
            break
        }

    }
}
countBottles()