
function boom(){
    let x = "boom"[1];
    let num = parseInt(prompt("Enter a number: "));
    x = x.repeat(num);
    let y = "b" + x + "m";
    if(num < 2){
        return "boom";
    } else if (num > 2 && num % 2 == 0 && num % 5 == 0){
        return y.toUpperCase();
    }else if(num > 2 && num % 2 == 0){
        return y + '!'
    }else if(num > 2){
        return y;
    }
}

boom();