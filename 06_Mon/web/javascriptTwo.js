document.getElementById("btn").addEventListener("click", function() {
    var array = arrayBuild();
    var min = array[0];
    var max = array[0];
    var i = 0

    while(i < array.length) {
        if(array[i] < min) {
            min = array[i];
        } else if (array[i] > max) {
            max = array[i];
        } else {
            i++
            continue;
        }

        i++
    }

    var answer = max - min;
    document.getElementById("resultTwo").innerText = `${array}\nAnswer is: ${answer}`;
})

function arrayBuild() {
    var array = [];
    for (var i = 0; i < 5; i++) {
        array.push(Math.ceil(Math.random() * 21));
    }
    return array;
}
