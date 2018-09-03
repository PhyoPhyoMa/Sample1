$(document).ready(function(){
	$('form').on('submit', function(event){
		$.ajax({
			type: "POST",
			url: "/convert",
			success: function(response){
				
			},
			data: {
				myinput: $('input[name=input]:checked').val(),
				myoutput: $('input[name=output]:checked').val(),
				source: $('#source').val()
			}
		})
		.done(function(data){
			if(data.error){
				// Do something
			}
			else{
				
				$("#destination").val(data.output).show();
			}
		});
		event.preventDefault();
	});
});
