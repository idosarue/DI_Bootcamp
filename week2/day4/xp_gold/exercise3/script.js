/*Exercise 3 : SwapCase
Instructions
Write a JavaScript function which takes a string as an argument and swaps the case of each character.
For example :

if you input 'The Quick Brown Fox' 
the output should be 'tHE qUICK bROWN fOX'.*/

function upperRest(str) {
    let wordFirst, wordRest, x, arr = [], word = str.split(" ");
    for(let char = 0; char < word.length; char++){
        wordRest = word[char].slice(1, ).toUpperCase()
        wordFirst = word[char][0].toLowerCase()
        x = `${wordFirst}${wordRest}`
        arr.push(x)
        
    }
    return arr.join(' ')
    

}
console.log(upperRest("hey im ido Helasd"))