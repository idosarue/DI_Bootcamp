function infoAboutMe(){
    console.log("My name is Ido, I'm 23 and I like to play guitar")
}
infoAboutMe();

function infoAboutPerson(personName, personAge, personFavoriteColor, personHobbies){
    console.log(`Your name is ${personName}, you are ${personAge} years old, your favorite color is ${personFavoriteColor}`);
    for(let i = 0; i < personHobbies.length; i++){
        console.log(personHobbies[i]);
    }
}

infoAboutPerson("David", 45, "blue", ["tennis", "painting"])
infoAboutPerson("Josh", 12, "yellow", ["videoGame", "hanging out with friends", "playing cards"])