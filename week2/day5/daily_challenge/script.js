let bottles = 99
let counter = 1;
for(let i = 99; i >= 0; i--){
    let FirstSentenceBottle = `${bottles} of beer on the wall`;
    let secondSentence = `${bottles} of beer`;
    let SentenceFor1Bottle = `take ${counter} down pass it around`;
    let SentenceBottles = `take ${counter} down pass them around`;
    if(bottles >= 9){
        if(bottles === 99){
            bottles -= counter
            console.log(FirstSentenceBottle)
            console.log(SentenceFor1Bottle)
            counter+=1
        }else{
            bottles -= counter
            console.log(FirstSentenceBottle)
            console.log(FirstSentenceBottle)
            console.log(secondSentence)
            counter +=1
            console.log(SentenceBottles)
        }

    }else if(bottles == 8){
        counter = 7
        console.log(FirstSentenceBottle)
        console.log(FirstSentenceBottle)
        console.log()
        bottles -= 7
        console.log(`take 7 down pass them around`)

        console.log(`${bottles} bottle of beer on the wall..`)
    }

}