let x = document.getElementById('x')
let y = document.getElementById('y')
let speed = document.getElementById('speed')
let alt = document.getElementById('alt')
let task = document.getElementById('task')

setInterval(updateData, 300);

function updateData() {
    var xhttp = new XMLHttpRequest();
    console.log("b")
    xhttp.onreadystatechange = function() {
        if (this.readyState == 4 && this.status == 200) {
            var data = JSON.parse(this.responseText);
            x.innerHTML = `X-pos:<br>${data.x_pos}`
            y.innerHTML = `Y-pos:<br>${data.y_pos}`
            speed.innerHTML = `Speed:<br>${data.speed} km/t`
            alt.innerHTML = `Alt:<br>${data.altimeter} m`
            task.innerHTML = `Current task:<br>${data.task}`
        }
    
    };
    xhttp.open("GET", "/drone-data/Drone1", true);
    xhttp.send();

}   
