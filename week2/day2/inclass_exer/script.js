let userCart = {
	username : "John",
	password: 1234,
	isUserSignedIn : true,
	cart : {
		apple : 2,
		banana : 1,
		pear : 5
	},
	prices : {
		apple : 0.5,
		banana : 0.8,
		pear : 0.2
	}
};
// userCart["username"] = "Josh";
// console.log(userCart);
// console.log(userCart["cart"]["pear"]);
// console.log(userCart["prices"]["pear"]);
let numberPear = userCart["cart"]["pear"];
let pricePerPear = userCart["prices"]["pear"];
let totalPricePear = numberPear * pricePerPear;
// alert(`The pears cost ${totalPricePear} shekels to ${userCart["username"]}`)

// let newPearPrice = pricePerPear * 0.17 + pricePerPear;//1
// userCart["prices"]["pear"] = newPearPrice;
// let userFruit = prompt("Choose a fruit: Apple/Banana/Pear? ").toLowerCase();//2
// let userFruitPrice = userCart["prices"][userFruit];
// console.log(userFruitPrice)


if(userCart["isUserSignedIn"]){
    console.log(userCart["username"], userCart["password"]);
}else {
    console.log("YOu need to sign in")
}

userCart["password"] = 123456;

if(userCart["username"] == "John" && userCart["password"] == "123456"){
    console.log("Signed in");
}else if(userCart["username"]== "John" || userCart["password"] == "123456"){
    console.log("one credential is false");
}else {
    console.log("you need to sign in");
}