let names= ["john", "sarah", 23, "Rudolf",34];

for(let i = 0; i < names.length; i++){
    if(typeof(names[i]) != 'string'){
        continue;//break
    }else{
        let x = names[i][0]
        if(x != x.toUpperCase()){
            let newX = x.toUpperCase();
            console.log(`${names[i].replace(x, newX)}`);
        }
        
    }
}

for(i in names){
    if(typeof(names[i]) != 'string'){
        break
    }else {
        console.log(names[i])
    }
}