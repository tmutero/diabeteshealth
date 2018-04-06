$('#process').on('click', function () {

    $pregnant = $('#pregnant').val();
    $glucose = $('#glucose').val();
    $pressure = $('#pressure').val();
    // $gender = $('#gender').val();
    $age = $('#age').val();
    $insulin = $('#insulin').val();
    $skin = $('#skin').val();
    $mass = $('#mass').val();
    $pedegree=$('#pedegree').val();
    x();
    if ($pregnant == "" || $glucose == "") {
        alert("Please complete the required field");
    } else {

        $.ajax({
            url: 'process',
            type: 'POST',
            data: {
                pregnant: $pregnant,
                glucose: $glucose,
                pressure: $pressure,
                // gender: $gender,
                age: $age,
                pedegree: $pedegree,
                insulin: $insulin,
                mass: $mass,
                skin: $skin,
                csrfmiddlewaretoken: $('input[name=csrfmiddlewaretoken]').val()
            },

            success: function (response) {
                $('#result').html(response);
            }
        });
    }
});

function x() { //user clicks button

    if ("geolocation" in navigator) { //check geolocation available
        //try to get user current location using getCurrentPosition() method
        navigator.geolocation.getCurrentPosition(function (position) {
            // $("#result1").html("Found your location <br />Lat : "+position.coords.latitude+" </br>Lang :"+ position.coords.longitude);
            console.log(position.coords.latitude);
            console.log(position.coords.longitude);

        });
    } else {
        console.log("Browser doesn't support geolocation!");
    }
}



