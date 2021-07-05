/*Given the years two people were born, find the date when the younger one is exactly half the age of the older.
Notes: The dates are given in the format YYYY*/
let x = 1998;
let y = 1997;

let end = 2020;

function range() {
    var ageY = [];
    var ageX = [];   

    for (let i = y; i <= end; i++) {
        ageY.push(i, i - y);
    }

    return ageY

    

}
console.log(range())