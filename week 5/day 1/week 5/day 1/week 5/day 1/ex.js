<!DOCTYPE html>
<html lang="en">
<head>
<meta charset="UTF-8">
<meta name="viewport" content="width=device-width, initial-scale=1.0">
<title>Star Wars AJAX App</title>

<link rel="stylesheet"
href="https://cdnjs.cloudflare.com/ajax/libs/font-awesome/6.1.1/css/all.min.css"/>

<style>
body{
    margin:0;
    font-family:Arial, sans-serif;
    background:black;
    color:#ffe81f;
    display:flex;
    justify-content:center;
    align-items:center;
    height:100vh;
    text-align:center;
}

.container{
    width:500px;
}

#character-box{
    background:#111;
    border:2px solid #ffe81f;
    border-radius:12px;
    padding:30px;
    min-height:250px;
    box-shadow:0 0 20px rgba(255,232,31,0.4);
}

button{
    margin-top:20px;
    padding:15px 25px;
    font-size:18px;
    border:none;
    border-radius:10px;
    background:#ffe81f;
    cursor:pointer;
    font-weight:bold;
}

button:hover{
    background:#fff176;
}

.loader{
    font-size:50px;
    animation:spin 1s linear infinite;
}

.error{
    color:red;
    font-size:20px;
}

@keyframes spin{
    100%{transform:rotate(360deg);}
}
</style>
</head>
<body>

<div class="container">
    <h1>⭐ Star Wars Character Finder</h1>

    <div id="character-box">
        Click the button to find a random Star Wars character
    </div>

    <button id="btn">Find Someone</button>
</div>

<script>
const button = document.getElementById("btn");
const box = document.getElementById("character-box");

function randomId() {
    return Math.floor(Math.random() * 83) + 1;
}

function loading() {
    box.innerHTML = `
        <i class="fa-solid fa-spinner loader"></i>
        <p>Loading...</p>
    `;
}

function errorMessage() {
    box.innerHTML = `
        <p class="error">⚠ Error fetching data. Try again.</p>
    `;
}

async function fetchCharacter() {
    loading();

    try {
        const response = await fetch(
            `https://www.swapi.tech/api/people/${randomId()}`
        );

        if (!response.ok) throw new Error("Character fetch failed");

        const data = await response.json();

        if (!data.result) throw new Error("Invalid character data");

        const character = data.result.properties;

        const homeResponse = await fetch(character.homeworld);

        if (!homeResponse.ok) throw new Error("Homeworld fetch failed");

        const homeData = await homeResponse.json();

        const homeworld =
            homeData.result?.properties?.name || "Unknown";

        box.innerHTML = `
            <h2>${character.name}</h2>
            <p><strong>Height:</strong> ${character.height}</p>
            <p><strong>Gender:</strong> ${character.gender}</p>
            <p><strong>Birth Year:</strong> ${character.birth_year}</p>
            <p><strong>Home World:</strong> ${homeworld}</p>
        `;
    }

    catch(error){
        errorMessage();
        console.error(error);
    }
}

button.addEventListener("click", fetchCharacter);
</script>

</body>
</html>