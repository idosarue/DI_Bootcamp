let picture = [
    [0,0,1,1,1,0,0],
    [0,1,0,0,0,1,0],
    [0,1,0,0,0,1,0],
    [0,1,1,1,1,1,0],
    [0,1,0,0,0,1,0],
    [0,1,0,0,0,1,0],   
    [0,1,0,0,0,1,0],

]

let newPicture = []
let regexZero = /0/g
let regexOne = /1/g

for(let line in picture){
    console.log(picture[line].join(' ').replace(regexOne,'*').replace(regexZero, ' '))

}
