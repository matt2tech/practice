document.getElementById("btn").addEventListener("click", function() {
    var array = ["blue", "red", "yellow", "green", "yellow", "yellow", "yellow", "blue"];
    var count = 0;

    for(var i = 0; i < array.length; i++) {
        for(var x = i + 1; x < array.length; x++) {
            if(array[i] == array[x] && array[i] != null) {
                count++;
                array[i] = null;
                array[x] = null;
                break
            } else {
                continue
            }
        }
    }

    var answer = count
    document.getElementById("resultOne").innerText = `Answer is: ${answer}`;
})
