document.getElementById("btn").addEventListener("click", function() {
    var value = document.getElementById("input").value;
    var string = "";

    for(var i = 0; i < value.length; i++) {
        if(value[i].toLowerCase() in abc) {
            string +=  value[i].repeat(abc[value[i]]) + "\n";
        } else {
            string += `${value[i]}\n`
        }
    }
    document.getElementById("resultOne").innerText = string;
})

var abc = {
    "a": 1,
    "b": 2,
    "c": 3,
    "d": 4,
    "e": 5,
    "f": 6,
    "g": 7,
    "h": 8,
    "i": 9,
    "j": 10,
    "k": 11,
    "l": 12,
    "m": 13,
    "n": 14,
    "o": 15,
    "p": 16,
    "q": 17,
    "r": 18,
    "s": 19,
    "t": 20,
    "u": 21,
    "v": 22,
    "w": 23,
    "x": 24,
    "y": 25,
    "z": 26
}
