$(document).ready(function () {
    $(".btn_class").on("click", function () {
        var btn_proparty = $(this)
        var row = $(this).closest("tr");
        var roll = row.find(".std_roll").text();
        var cls = row.find(".std_cls").text();
        var api_url = 'http://127.0.0.1:8000/api/attendance/' + cls + '/' + roll
        $.ajax({

            url: api_url,
            method: 'get',
            success: function (data) {
                btn_proparty.addClass("btn btn-success")

                //  console.log(data)
            },
            error: function (error) {
                btn_proparty.addClass("btn btn-danger", alert("This user already atend"))
                // console.log("error", error)
            }
            // ajax end
        });
        // onclick funrtion end
    })
    // document end
})