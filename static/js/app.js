$(document).ready(function(){
	$('form').on('submit', function (event){
		$.ajax({
			type: "POST",
			url: "/convert",
			data: {
				myinput: $('#myinput').val()
			}
		});
		
		.don(function(data){
			if(data.error){
				//Do something

			}
			else {
				$("#output").val(data.output).show();
			}

