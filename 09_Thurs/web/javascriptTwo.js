document.getElementById("btn").addEventListener("click", function() {
    var array = ["blue", "red", "yellow", "green", "yellow", "yellow", "yellow"];
    var count = 0;
    var i = 0;

    while(i < array.length) {
        var x = i + 1
        while (x < array.length) {
            if(array[i] == array[x] && array[i] != null) {
                count++;
                array[i] = null;
                array[x] = null;
                break
            } else {
                x++
                continue
            }
        }
        i++
    }

    var answer = count
    document.getElementById("resultTwo").innerText = `Answer is: ${answer}`;
})
