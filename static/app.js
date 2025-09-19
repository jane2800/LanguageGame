async function startGame() {
    let response = await fetch("/api/start-game");
    let data = await response.json();
    alert("Game started! Game ID: " + data.game_id);
}

async function continueGame(){
    let response = await fetch("/api/start-game");
    let data = await response.json();
    alert("Game started! Game ID: " + data.game_id);
}

async function getRandomNumber() {
    let response = await fetch("/api/random-number?min=1&max=6");
    let data = await response.json();
    document.getElementById("randomResult").innerText =
        "Random number: " + data.random_number;
}


function pop(id) {
    let box = document.getElementById(id);
    if (box.style.display === "block") {
        box.style.display = "none";
    } else {
        box.style.display = "block";
    }
}

//quiz.html
function getScreenSize() {
    return {
        width: window.innerWidth,
        height: window.innerHeight
    };
}
// Run when page loads
window.onload = showSize;

// Update on window resize
window.onresize = showSize;

function showSize() {
    let size = getScreenSize();
    document.getElementById("screenSize").innerText =
        `Width: ${size.width}, Height: ${size.height}`;
}
