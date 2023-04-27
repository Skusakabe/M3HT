// //Team Ringbearers :: Brianna Tieu, Shinji Kusakabe
// SoftDev pd08
// K31 -- canvas based JS animation
// 2023-04-25t

var c = document.getElementById("playground");
var dotButton = document.getElementById("buttonCircle");
var dvdButton = document.getElementById("bouncyLogo");
var stopButton = document.getElementById("buttonStop");

var ctx = c.getContext("2d");

ctx.fillStyle = "#ADD8E6";

var requestID; //init global var for use with animation frames

var clear = (e) => {
    // e.preventDefault(); Seems to stop the circle animation as e.preventDefault is not a function.
    // it will also break the dvdLogo button if the dvdLogo function has e as a parameter, but it will not
    // break that button if only the dvdLogoSetup has e as a parameter.
    ctx.clearRect(0, 0,c.width,c.height);
};

var radius = 0;
var growing = true;

var drawDot = (e) => {
    //clear the slate or playground
    clear(e);
    //check if the circle is meant to grow AND diameter is larger than canvas
    if (growing === true && radius >= c.width / 2) {
        growing = false;
    } else if (growing === false && radius <= 0){
        growing = true;
    }
    //check if the circle is meant to grow and adjust radius accordingly
    if (growing === true) {
        radius = radius + 2;
    } else {
        radius = radius - 2;
    }

    ctx.beginPath();
    ctx.arc(250, 250,radius,0,2*Math.PI,false); //negative radius will cause an error with this method
    ctx.fill();
    ctx.closePath();

    //cancel must go before request, otherwise the button must be clicked
    //each time to grow the circle (but porque?). (Shinji): I did some testing and it seems like if you remove
    //the cancel entirely, it will work like normal on the first click, but you will get that issue Mykolyk mentioned
    //in class about how the animation will begin speeding up if you keep pressing the button. I think this means that
    //drawDot is called with window.requestAnimationframe(drawDot) and it will get compounded if there is no cancelAnimationFrame(requestID)
    //(like there will be multiple instances of these continuous calls of drawdot, so it goes faster). window.cancelAnimationFrame(requestID)
    //will close the latest called loop of this function, stopping it from repeating. Therefore, if the cancel goes after the request, it will
    //close the function call/animation that is requested (that would maybe be executed on the next tick? IDK how exactly it all works), thus preventing it from
    //repeating and only updating/going to the next frame once.
    window.cancelAnimationFrame(requestID);
    requestID = window.requestAnimationFrame(drawDot);
}

var dvdLogoSetup = function (e) {
    window.cancelAnimationFrame(requestID);
    var rectWidth = 60;
    var rectHeight = 40;

    var rectX = Math.floor(Math.random() * (c.width - rectWidth));
    var rectY = Math.floor(Math.random() * (c.height - rectHeight));

    // If you wanted the speed to always be the same, but the angle to be random, you could make a speed variable that stays constant and find a random angle.
    // Then set xVel and yVel equal to that speed value multiplied by the cos(angle) or sin(angle) respectively.
    var xVel = Math.random() * 2 + 1;
    var yVel = Math.random() * 2 + 1;

    var logo = new Image();
    logo.src = "logo_dvd.jpg";
    var dvdLogo = function () {
        console.log(rectX);
        clear(e);
        ctx.fillRect(rectX,rectY,rectWidth,rectHeight);
        ctx.drawImage(logo, rectX, rectY, rectWidth, rectHeight);
        if (rectX < 0 || rectX > c.width - rectWidth) {
            xVel = xVel * -1;
        }
        if (rectY < 0 || rectY > c.height - rectHeight) {
            yVel = yVel * -1;
        }   
        rectX = rectX + xVel;
        rectY = rectY + yVel;
        requestID = window.requestAnimationFrame(dvdLogo);
    }
    dvdLogo();
}

var stopIt = () => {
    console.log(requestID);
    window.cancelAnimationFrame(requestID);
}

dotButton.addEventListener("click", drawDot);
stopButton.addEventListener("click", stopIt);
dvdButton.addEventListener("click", dvdLogoSetup);