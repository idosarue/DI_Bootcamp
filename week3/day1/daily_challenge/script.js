let names = ["Mercury", "Venus", "Earth","Mars", "Jupiter", "Saturn", "Uranus", "Neptune", "Pluto"];
let colors = ["red", "blue", "yellow", "pink", "white", "lightblue", "salmon", "brown", "grey"]

let planets;

for(let i = 0; i<names.length;  i++){
    planets = document.createElement('div');
    planets.classList.add("planet", names[i])
    planets.style.backgroundColor = colors[i];
    document.body.firstElementChild.appendChild(planets)
}
