function checkNumber(){
    for(let num = 0; num <= 100; num++){
        if(num % 2 == 0){
            console.log(`the number ${num} is even`);
        }else{
            console.log(`the number ${num} is odd`);
        }
    }  
}

checkNumber();