

function frame() {
    let words = prompt("enter words seperated with comma: ");
    let newWords = words.replace(/\s/g, '').split(",")
    console.log(newWords)
    let star = '*';
    let space = ' ';
    let dif;
    let longest = 0;
    let wordLen ;
    for(let i = 0; i< newWords.length; i++){
        console.log(longest);
        if(newWords[i].length > longest){
            longest = newWords[i].length
        }
        console.log(longest)
        
    }console.log(longest);

    console.log(star.repeat(longest+5));

    for(let i = 0; i < newWords.length ; i++){ 
        wordLen = newWords[i].length;
        dif = longest - wordLen;
        console.log(star, newWords[i],space.repeat(dif), star);
    }
        console.log(star.repeat(longest+5))
}
frame();


// Hello, World, in, as, frame