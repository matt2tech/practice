document.getElementById("buttonTwo").addEventListener("click", function() {
    var value = document.getElementById("inputTwo").value
    var array = buildArray(value)

    var result = array.map(i => factor(i, value))
    
    document.getElementById("resultTwo").innerText = result
})

function buildArray(x) {
    var array = []
    for ( var i = 1; i < x; i++) {
        array.push(i);
    }
    return array;
}

function factor(i, x) {
    var array = ""
    if (x % i == 0) {
        array += `${i}: is a factor of ${x}\n`;
    } else {
        array += `${i}: is not a factor of ${x}\n`;
    }
    return array
}
