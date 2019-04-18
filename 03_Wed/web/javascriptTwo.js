document.getElementById("btn").addEventListener("click", function() {
    var one = document.getElementById("stringOne").value;
    var two = document.getElementById("stringTwo").value;

    var num = Math.min(one.length, two.length);
    var string = "";
    document.getElementById("resultTwo").innerText = string;
    var x = 0

    while(x < num) {
        if (one[x].toLowerCase() == two[x].toLowerCase()) {
            string += one[x];
        } else {
            string += ".";
        }
        x++
    }
    string += ".".repeat((Math.max(one.length, two.length) - num));
    document.getElementById("resultTwo").innerText = string;
})
