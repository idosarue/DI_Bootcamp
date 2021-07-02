/*Exercise 2 : Mixup
Instructions
Create 2 variables. The values should be strings. For example:
let str1 = "mix" let str2 = "pod"
Slice out and swap the first 2 characters of the 2 strings from part 1.
Create a third variable where the value is the concatenation of the two strings from the part 1 (separated by a space).
Finally console.log the new concatenated string.*/
let str1 = "mix";
let str2 = "pod";
let newStr1 = str1.replace('mi', 'ri');
let newSrt2 = str2.replace('po', 'rl')
let srt3 = `${newStr1} ${newSrt2}`
console.log(srt3);
