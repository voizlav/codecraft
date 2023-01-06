const year = document.getElementById("year");
const currentTime = Date.now();
year.innerText = new Date(currentTime).getFullYear();