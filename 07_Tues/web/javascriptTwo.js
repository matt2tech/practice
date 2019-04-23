document.getElementById("btn").addEventListener("click", function() {
    var array = arrayBuild();
    var count = 0;
    var i = 0

    while(i < array.length) {
        if(array[i] == 1) {
            count++
        } else {
            count--
        }
        i++
    }

    var answer = count > 0;
    document.getElementById("resultTwo").innerText = `${array}\nAnswer is: ${answer}`;
})

function arrayBuild() {
    var array = [];
    for (var i = 0; i < 5; i++) {
        array.push(Math.floor(Math.random() * 2));
    }
    return array;
}
