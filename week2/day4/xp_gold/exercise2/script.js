// Exercise 2 : Abbrev_name console.log(abbrevName("Robin Singh")); --> "Robin S."
// Write a JavaScript function to convert a string into an abbreviated form.
// console.log(abbrevName("Robin Singh")); --> "Robin S."

function Abbrev_name(str){
    let word = str.split(" "),secondWordFirst = word[1][0].toUpperCase(),  firstWord = word[0], firstWordFirst = firstWord[0].toUpperCase();
    let firstWordRest = firstWord.slice(1, ).toLowerCase();// change all chars of first to lowercase
    let x = `${firstWordFirst}${firstWordRest} ${secondWordFirst}.`
    return x;
}
console.log(Abbrev_name("heSlo world"));