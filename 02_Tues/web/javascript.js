document.getElementById("buttonOne").addEventListener("click", function() {
    var array = ""
    var value = document.getElementById("inputOne").value

    for(var i = 1; i < value; i++) {
        if (value % i == 0) {
            array += `${i}: is a factor of ${value}\n`
        } else {
            array += `${i}: is a not factor of ${value}\n`
        }
    }
    document.getElementById("resultOne").innerText = array
})
