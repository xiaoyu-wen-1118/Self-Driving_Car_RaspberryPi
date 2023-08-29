document.onkeydown = updateKey;
document.onkeyup = resetKey;

var server_port = 65432;
var server_addr = "192.168.0.180";   // the IP address of your Raspberry PI
var DELAY = 200

function client(){
    
    const net = require('net');
    var input = document.getElementById("message").value;

    const client = net.createConnection({ port: server_port, host: server_addr }, () => {
        // 'connect' listener.
        console.log('connected to server!');
        // send the message
        client.write(`${input}`);
    });
    
    // get the data from the server
    client.on('data', (data) => {
        const obj = JSON.parse(data)
        document.getElementById("direction").innerHTML = obj.direction;
        document.getElementById("temperature").innerHTML = obj.temperature;
        document.getElementById("speed").innerHTML = obj.speed;
        document.getElementById("distance").innerHTML = obj.distance;
        console.log(data.toString());
        client.end();
        client.destroy();
    });

    client.on('end', () => {
        console.log('disconnected from server');
    });


}

function send_data(input){
    const net = require('net');
    const client = net.createConnection({ port: server_port, host: server_addr }, () => {
        // 'connect' listener.
        console.log('connected to server!');
        // send the message
        client.write(`${input}`);
    });
    
    // get the data from the server
    client.on('data', (data) => {
        const obj = JSON.parse(data)
        document.getElementById("direction").innerHTML = obj.direction;
        client.end();
        client.destroy();
    });

    client.on('end', () => {
        console.log('disconnected from server');
    });    
}
// for detecting which key is been pressed w,a,s,d
function updateKey(e) {
    
    e = e || window.event;

    if (e.keyCode == '87') {
        // up (w)
        document.getElementById("upArrow").style.color = "green";
        send_data("Forward");
    }
    else if (e.keyCode == '83') {
        // down (s)
        document.getElementById("downArrow").style.color = "green";
        send_data("Backward");
    }
    else if (e.keyCode == '65') {
        // left (a)
        document.getElementById("leftArrow").style.color = "green";
        send_data("Left");
    }
    else if (e.keyCode == '68') {
        // right (d)
        document.getElementById("rightArrow").style.color = "green";
        send_data("Right");
    }
}

// reset the key to the start state 
function resetKey(e) {

    e = e || window.event;
    if (e.keyCode == '87' || e.keyCode == '83' || e.keyCode == '65' || e.keyCode == '68')
    send_data("Stop");
    document.getElementById("upArrow").style.color = "grey";
    document.getElementById("downArrow").style.color = "grey";
    document.getElementById("leftArrow").style.color = "grey";
    document.getElementById("rightArrow").style.color = "grey";
}

// update data for every 50ms
function update_data(){
    setInterval(function(){
        // get image from python server
        client();
    }, DELAY);
}
