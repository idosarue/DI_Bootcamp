
let words = prompt("enter words seperated with comma: ");
let newWords = words.replace(/\s+/g, '').split(",")
let star = '*'
let space = ' '
let dif;
let longest;

function frame(){

    for(let i = 0; i< newWords.length; i++){
        longest = Math.max(newWords[i].length) 
    }
    console.log(star.repeat(longest+5))

    for(let i in newWords){ 
        let wordLen = newWords[i].length;
        dif = longest - wordLen;
        console.log(star, newWords[i],space.repeat(dif), star);
    }
        console.log(star.repeat(longest+5))
}
frame();


// Hello, World, indd, aasd, frames