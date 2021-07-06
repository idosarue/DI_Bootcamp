let amazonBasket = {
    glasses: 1,
    books: 2,
    floss: 100
}



function checkBasket() {
    let userItem = prompt("Enter an item: ").toLowerCase();
    if(userItem in amazonBasket){
        console.log("in basket")
    }else{
        console.log("not in basket")
    }
}
checkBasket()