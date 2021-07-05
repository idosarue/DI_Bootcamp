/*Harder exercise
Hint : This exercise has 2 parts. First, do this exercise without Regular Expressions, then do it using Regular Expressions

While working in a Post Office you must have the clients’ zip code in order to send them their letters.
Ask the client for their zip code and console.log “success” or “error” based on the following rules.
Zip codes consists of 5 numbers
Must only contain numbers
Must not contain any whitespace (spaces)
Must not be greater than 5 digits in length*/

function getZip() {
    let zip = prompt('Enter your zip: ');
    let zipLen = zip.length;
    let inc = zip.includes(" ")
    if (zipLen < 5) {
        console.log("error");


    }else if(zipLen > 5 ){
        zip = parseInt(zip);
        if(isNaN(zip)){
            console.log("error")
        }else if(inc){1 
            console.log("error")
        }
    }else {
        console.log("success")
    }
        

}

getZip()