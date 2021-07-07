


function frame() {
    let space = ' ';
    let hasComma = true;
    while(hasComma){
        let words = prompt("enter strings seperated with comma: ");
        if(!words.includes(",")){
            alert("missing comma!!")
        }else{
            alert("Finally..")
            hasComma = false;
            let newWords = words.replace(/\s/g, '').split(",")
            let star = '*';
            let dif;
            let longest = 0;
            let wordLen;
            for(let i = 0; i< newWords.length; i++){
                if(newWords[i].length > longest){
                    longest = newWords[i].length
                }       
            }
        
            console.log(star.repeat(longest+5));
        
            for(let i = 0; i < newWords.length ; i++){ 
                wordLen = newWords[i].length;
                dif = longest - wordLen;
                console.log(star, newWords[i],space.repeat(dif), star);
            }
                console.log(star.repeat(longest+5))
            
        }
    }

}

frame()



// Hello, World, in, as, frame