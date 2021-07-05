
            
function pattern() {
    let x = '*';
    let y = [];
    for(i = 0; i < 6; i++){
        y.push(x)
        let li = y.join(" ")
        console.log(li.toString());
    }
    
}

pattern();

function pattern2() {
    let line = " ";
    for(i in line){     
        for(let i = 0; i < 6; i++){
            line += '* ';
            console.log(line)
        }
    }   
}
pattern2();