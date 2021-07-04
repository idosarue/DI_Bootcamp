let sentence = prompt("Enter a sentence that contains the word Nemo: ");
sentence = sentence.toLowerCase();
let newSentence = sentence.split(" ");
let x = newSentence.includes("nemo");
if(x) {
    let y = newSentence.indexOf("nemo");
    console.log(`I found Nemo at position ${y}`)
} else {
    console.log("I couldn't find Nemo")
}


