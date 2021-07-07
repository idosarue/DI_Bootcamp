


function frame() {
    let space = ' ',hasComma = true;
    while(hasComma){
        let words = prompt("enter strings seperated with comma: ");
        if(!words.includes(",")){
            alert("missing comma!!")
        }else{
            alert("Finally..")
            hasComma = false;
            let newWords = words.replaceAll(/\s/g, '').split(",")
            console.log(words.replaceAll(/\s/g, ''))
            let star = '*', dif, longest = 0,wordLen;
            for(let i = 0; i< newWords.length; i++){
                if(newWords[i].length > longest){
                    longest = newWords[i].length
                }       
            }
            
            console.log(star.repeat(longest+4));
        
            for(let i = 0; i < newWords.length ; i++){ 
                wordLen = newWords[i].length;
                dif = longest - wordLen;
                console.log(`${star}${space}${newWords[i]}${space.repeat(dif)}${space}${star}`);
            }
                console.log(star.repeat(longest+4))
            
        }
    }

}

frame()



// Hello, World, in, as, frame