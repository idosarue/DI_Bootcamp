

function tipCalc(){
    let billAmnt = parseInt(prompt("Enter you bill amount: "));
    if(billAmnt < 50 ){
        let tip = Math.round(billAmnt * 0.2)
        console.log("the tip is: ", tip);
        console.log("the final bill is: ", billAmnt + tip);
    }else if(billAmnt <= 200){
        let tip = Math.round(billAmnt * 0.15)
        console.log("the tip is: ", tip);
        console.log("the final bill is: ", billAmnt + tip); 
    }else if(billAmnt > 200){
        let tip = Math.round(billAmnt * 0.1)
        console.log("the tip is: ", tip);
        console.log("the final bill is: ", billAmnt + tip);
    }
}

tipCalc()