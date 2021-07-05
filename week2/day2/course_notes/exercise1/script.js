let myObject = {
    username : "ido",
    password : "1234"
};

let dataBase = [myObject];

let newsFeed = [
    {
        username : "hey",
        timeline : 1
    },
    {
        username : "asd",
        timeline : 5
    },
    {
        username : "dude",
        timeline : 7
    }
];

console.log(newsFeed[1]["timeline"]);