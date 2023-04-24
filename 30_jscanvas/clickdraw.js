//retrieve node in DOM via ID
var c = document.getElementById("slate");
var wipe = document.getElementById("buttonClear");

//instantiate a CanvasRenderingContext2D object
var ctx = c.getContext("2d");

//init globar state var
var mode = "rect";

//var toggleMode = function(e){
var toggleMode = (e) => {
    console.log("toggling...");
    if (mode === "rect") {
        mode = "circ";
    }
    else {
        mode = "rect";
    }
}

var drawRect = function(e) {
    var mouseX = e.clientX - 8; //gets X-coor of mouse when event is fired
    var mouseY = e.clientY - 132;//gets Y-coor of mouse when event is fired
    console.log("mouseclick registered at ", mouseX, mouseY);
    ctx.fillRect(mouseX, mouseY, 10, 20);
}

c.addEventListener("click", function() {
    if (mode === "rect") {
        drawRect();
    }
    else {
        drawCirc();
    }
}); //passes the mouse event as parameter for the function
wipe.addEventListener("click", function() {
    ctx.clearRect(0,0,600,600);
});