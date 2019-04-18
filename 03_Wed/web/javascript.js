document.getElementById("btn").addEventListener("click", function() {
    var one = document.getElementById("stringOne").value;
    var two = document.getElementById("stringTwo").value;

    var num = Math.min(one.length, two.length);
    var string = "";
    document.getElementById("resultOne").innerText = string;

    for(var i = 0; i < num; i++) {
        console.log(one[i] + " " + two[i])
        if (one[i].toLowerCase() == two[i].toLowerCase()) {
            string += one[i];
        } else {
            string += ".";
        }
    }
    string += ".".repeat((Math.max(one.length, two.length) - num));
    document.getElementById("resultOne").innerText = string;
})
