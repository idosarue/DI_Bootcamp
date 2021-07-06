let stock = { 
    "banana": 6, 
    "apple": 0,
    "pear": 12,
    "orange": 32,
    "blueberry":1
}  

let prices = {    
    "banana": 4, 
    "apple": 2, 
    "pear": 1,
    "orange": 1.5,
    "blueberry":10
} 

let shoppingList = ["banana", "orange", "apple"];
let sum = 0;
function myBill(){
    for(item in shoppingList){
        if(stock[shoppingList[item]] > 0){
            stock[shoppingList[item]] --;
            sum += prices[shoppingList[item]];
        }
    }console.log(`The sum of you shopping list is ${sum}`);
}
myBill()
