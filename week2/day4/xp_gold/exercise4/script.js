/*Exercise 4 : Omnipresent Value
Instructions
Create a function that determines whether an argument is omnipresent for a given array.
A value is omnipresent if it exists in every subarray inside the main array.
To illustrate:

[[3, 4], [8, 3, 2], [3], [9, 3], [5, 3], [4, 3]]
// 3 exists in every element inside this array, so is omnipresent.
Examples

isOmnipresent([[1, 1], [1, 3], [5, 1], [6, 1]], 1) ➞ true
isOmnipresent([[1, 1], [1, 3], [5, 1], [6, 1]], 6) ➞ false*/
function isOmni(array, num) {
    let x= [];
    for(let i=0;i < array.length ; i++){//loop thorugh array
        console.log(array[i])
        if(array[i].includes(num)){// check if num is every sub array
            x.push(true)//if it does add true to array of x
        }else{
            x.push(false)//if not add false to array of x
        }
    }if(x.includes(false)){// if false is in the array of x will return false
        return false
    }else {
        return true

    }
}
console.log(isOmni([[1, 1], [1, 3], [5, 1], [6, 1]], 1))