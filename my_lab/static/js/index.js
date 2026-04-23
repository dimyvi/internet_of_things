setInterval(getData, 1000);

function getData() {
    $.ajax({
        type: "GET",
        url: "/connect/3",
        dataType: "json",
        success: function(data) {
            document.getElementById("value").value = data.value;
        }
    });
}
