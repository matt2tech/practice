document.getElementById("btn").addEventListener("click", function() {
    var array = arrayBuild();
    var min = array[0];
    var max = array[0];

    for(var i = 0; i < array.length; i++) {
        if(array[i] < min) {
            min = array[i];
        } else if (array[i] > max) {
            max = array[i];
        } else {
            continue;
        }
    }

    var answer = max - min;
    document.getElementById("resultOne").innerText = `${array}\nAnswer is: ${answer}`;
})

function arrayBuild() {
    var array = [];
    for (var i = 0; i < 5; i++) {
        array.push(Math.ceil(Math.random() * 21));
    }
    return array;
}
