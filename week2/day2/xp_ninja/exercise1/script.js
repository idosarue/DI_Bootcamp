/*Given the years two people were born, find the date when the younger one is exactly half the age of the older.
Notes: The dates are given in the format YYYY*/
let x = 1998;
let y = 1997;

let end = 2020;

function range() {
    var olderAge = [];
    var youngerAge = [];   

    for (let i = y; i <= end; i++) {
        olderAge.push(i-y);
    }
    for (let i = x; i <= end; i++) {
        youngerAge.push(i-x);
    }

    console.log(olderAge)
    console.log(youngerAge)

    

}
range()