document.getElementById("btn").addEventListener("click", function() {
    var one = parseInt(document.getElementById("numOne").value);
    var two = parseInt(document.getElementById("numTwo").value);

    document.getElementById("resultOne").innerText = string;
    var string = "";

    for(var i = 0; i < two + 1; i++) {
        string += `${one} * ${i} = ${one * i}\n`;
    }
    document.getElementById("resultOne").innerText = string;
})
