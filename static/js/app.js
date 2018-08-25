$(document).ready(function () {
    $('#convert').bind('click', function (event) {
        $.ajax({
            type: "POST",
            url: "/_convert",
            data: {
                from_text: $('textarea[name="from_text"]').val(),
                to_encoding: $('input[name="to"]:checked').val(),
                from_encoding: $("input[name='from']:checked").val()
            }
        }).done(function (data) {
            if (data.error) {
                //  show error message
            } else {
                $("#to_text").val(data.result).show();
                $("#to_text_hint").hide();
            }
        });
        event.preventDefault();
    });

    $('input[type=radio][name=from]').change(function () {
        if (this.value === 'from_zawgyi') {
            $("#from_text").css("font-family", "Zawgyi-One");
        } else if (this.value === 'from_unicode') {
            $("#from_text").css("font-family", "Padauk");
        } else if (this.value === 'from_win') {
            $("#from_text").css("font-family", "WinInnwa");
        }
    });
    $('input[type=radio][name=to]').change(function () {
        if (this.value === 'to_zawgyi') {
            $("#to_text").css("font-family", "Zawgyi-One");
        } else if (this.value === 'to_unicode') {
            $("#to_text").css("font-family", "Padauk");
        } else if (this.value === 'to_win') {
            $("#to_text").css("font-family", "WinInnwa");
        }
    });
});

