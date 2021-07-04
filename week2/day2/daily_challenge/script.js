let sentence = "The movie is not that bad, I like it";
let wordNot = sentence.indexOf("not");
let wordBad = sentence.indexOf("bad");


if(wordBad > wordNot && wordNot != -1){
    let x = sentence.substring(wordNot, wordBad + 3);
    let newSent = sentence.replace(x, "good");
    console.log(newSent);

}else{
    console.log(sentence)
}

