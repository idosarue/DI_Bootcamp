let id;
let pos = 0;
function myMove() {
  let box = document.getElementById("myAnimation");   
  id = setInterval(frame, 10);
  function frame() {
    if (pos == 350) {
      clearInterval(id);
    } else {
      pos++; 
      box.style.top = pos +"px"
      box.style.left = pos + 'px'; 
    }
  }
}

function stop() {
  clearInterval(id);
    
}