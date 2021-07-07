


function frame(){
    let words = prompt("enter words seperated with comma: ");
    let newWords = words.replace(/\s+/g, '').split(",")
    console.log(newWords)
    let wordLen = newWords.length + 1;
    let star = '*'
    let space = ' '
    let dif;
    let long;
    console.log(star.repeat(long+5))
    for(let i in newWords){
        long = Math.max(newWords[i].length)
        dif = wordLen - long
        console.log(star, newWords[i],space.repeat(dif), star);
    }

        console.log(star.repeat(long+5))
}

frame();

// Hello, World, in, a, frames