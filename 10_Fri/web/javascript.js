document.getElementById("btn").addEventListener("click", function() {
    var value = document.getElementById("input").value.replace(" ", "");
    var bool = true;

    dict = magazineBuild()

    for(var i = 0; i < value.length; i++) {
        if(dict.hasOwnProperty(value[i]) == true && dict[value[i]] != 0) {
            dict[value[i]] -= 1;
            console.log(value[i])
        } else {
            bool = false;
            break
        }
    }
    document.getElementById("resultOne").innerText = bool;
})

var dict = {}

function magazineBuild() {
    var dict = {}
    var magazine = "Hello World".replace(" ", "");

    for(var i = 0; i < magazine.length; i++) {
        if(dict.hasOwnProperty(magazine[i]) == true) {
            dict[magazine[i]] += 1;
        } else {
            dict[magazine[i]] = 1;
        }
    }
    return dict
}
