let users = ["Lea123", "Princess45", "cat&doglovers", "helooo@000"];
let usersLen = users.length;
if(usersLen < 1){
    console.log("no one is online");
}else if(usersLen == 1) {
    console.log(`${users[0]} is online`);
}else if(usersLen == 2){
    console.log(`${users[0]} and ${users[1]} are online`);
}else {
    console.log(`${users[0]}, ${users[1]} and ${usersLen - 2} more are online`);
}