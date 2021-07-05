let lang = prompt("What language do you speak? ");
lang = lang.toLowerCase();

switch(lang){
    case "english":
        console.log("Hello");
        break;
    case "french":
        console.log("Bonjour");
        break;
    case "hebrew":
        console.log("Shalom")
        break;
    default:
        console.log("01110011 01101111 01110010 01110010 01111001");   
}