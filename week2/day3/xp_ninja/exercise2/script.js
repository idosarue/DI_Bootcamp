// Exercise 2 : Grade Average
let gradesList = [100,65,65,65];
let avg;
let sum = 0;
// function findAvg(gradesList) {
//     for(i in gradesList){
//         sum += gradesList[i]
//     }
//     avg = sum / gradesList.length;
//     if(avg > 65){
//         console.log("pass"); 
//     }else{
//         console.log("fail")      
//     }
// }
// findAvg(gradesList)

// bonus

function findAvg(gradesList) {
    for(i in gradesList){
        sum += gradesList[i];
    }
    return sum
}


function compareAvg(sum){
    avg = sum / gradesList.length;
    if(avg > 65){
        console.log("pass"); 
    }else{
        console.log("fail")      
    }   
}

compareAvg(findAvg(gradesList))