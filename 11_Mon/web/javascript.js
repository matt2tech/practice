var bill = [9.50, 11.75, 18.50, 3.00, 3.00];

document.getElementById("btn").addEventListener("click", function() {
    var allergy = document.getElementById("allergy").value;
    var pay = document.getElementById("pay").value;
    var total = 0;


    for(var i = 0; i < bill.length; i++) {
        if(bill[i] != bill[allergy]) {
            total += bill[i];
        } else {
            continue
        }
    }
    document.getElementById("resultOne").innerText = `Give back: ${pay - (total / 2)}`;
})


function list() {
    document.getElementById("bill").innerText = bill;
}

list();

