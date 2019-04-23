document.getElementById("btn").addEventListener("click", function() {
    var array = arrayBuild();
    var count = 0;

    for(var i = 0; i < array.length; i++) {
        if(array[i] == 1) {
            count++;
        } else {
            count--;
        }
    }

    var answer = count > 0
    document.getElementById("resultOne").innerText = `${array}\nAnswer is: ${answer}`;
})

function arrayBuild() {
    var array = [];
    for (var i = 0; i < 5; i++) {
        array.push(Math.floor(Math.random() * 2));
    }
    return array;
}
