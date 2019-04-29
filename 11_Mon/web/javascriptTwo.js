var bill = [9.50, 11.75, 18.50, 3.00, 3.00];

document.getElementById("btn").addEventListener("click", function() {
    var allergy = document.getElementById("allergy").value;
    var pay = document.getElementById("pay").value;
    var total = 0;
    var i = 0;


    while(i < bill.length) {
        if(bill[i] != bill[allergy]) {
            total += bill[i];
        } else {
            i++
            continue
        }
        i++
    }
    document.getElementById("resultTwo").innerText = `Give back: ${pay - (total / 2)}`;
})


function list() {
    document.getElementById("bill").innerText = bill;
}

list();
