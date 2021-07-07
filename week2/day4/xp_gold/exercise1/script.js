// Exercise 1 : Is_Blank

function is_Blank(str){
    let con = /[abc]/g;
    let result = str.match(con);
    if(result){
        console.log(false);
    }else{
        console.log(true)
    }
}

is_Blank("")