//retrieve node in DOM via ID
var c = document.getElementById("slate");
var wipe = document.getElementById("buttonClear");
var modeToggle = document.getElementById("buttonToggle");
const xOffset = 8;
const yOffset = 132;

//instantiate a CanvasRenderingContext2D object
var ctx = c.getContext("2d");

//init globar state var
var mode = "rect";

//var toggleMode = function(e){
var toggleMode = (e) => {
    console.log("toggling...");
    if (mode === "rect") {
        mode = "circ";
        modeToggle.innerHTML = "circ";
    }
    else {
        mode = "rect";
        modeToggle.innerHTML = "rect";
    }
}

var drawRect = (e) => {
    var mouseX = e.offsetX; //gets X-coor of mouse when event is fired
    var mouseY = e.offsetY;//gets Y-coor of mouse when event is fired
    console.log("mouseclick registered at ", mouseX, mouseY);
    ctx.beginPath();
    ctx.fillRect(mouseX, mouseY, 10, 20);
    ctx.closePath();
}

var drawCirc = (e) => {
    var mouseX = e.offsetX;
    var mouseY = e.offsetY;
    console.log("mouseclick registered at ", mouseX, mouseY);
    ctx.beginPath();
    ctx.arc(mouseX, mouseY, 8, 0, 2 * Math.PI);
    ctx.fill();
    ctx.closePath();
}

var draw = (e) => {
    if (mode === "rect") {
        drawRect(e);
    }
    else {
        drawCirc(e);
    }
}

c.addEventListener("click", draw); //passes the mouse event as parameter for the function
wipe.addEventListener("click", function() {
    ctx.clearRect(0,0,600,600);
});
modeToggle.addEventListener("click", toggleMode);