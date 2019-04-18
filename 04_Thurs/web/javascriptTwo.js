document.getElementById("btn").addEventListener("click", function() {
    var one = parseInt(document.getElementById("numOne").value);
    var two = parseInt(document.getElementById("numTwo").value);

    document.getElementById("resultTwo").innerText = string;
    var string = "";
    var x = 0;

    while(x < two + 1) {
        string += `${one} * ${x} = ${one * x}\n`;
        x++;
    }
    document.getElementById("resultTwo").innerText = string;
})
