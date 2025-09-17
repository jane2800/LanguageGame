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

