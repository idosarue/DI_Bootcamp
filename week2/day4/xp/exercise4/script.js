let sum = 0;
function isDivisible(divisor) {
    for(let i = 0; i <= 500 ; i++ ){
        if(i % divisor == 0){
            console.log(i);
            sum += i;
        }
    }console.log(sum);
}
isDivisible(23);