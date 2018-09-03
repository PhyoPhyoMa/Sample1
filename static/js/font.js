$(document).ready(function(){

$('input[type=radio][name=input]').change(function(){
		if (this.value == 'zawgyi') {
			$('#source').css("font-family", "Zawgyi-One");
		}
		if (this.value == 'unicode') {
			$('#source').css("font-family", "Pyidaungsu");
		}
		if (this.value == 'winmyanmar') {
			$('#source').css("font-family", "win_innwaregular");
		}
	});

$('input[type=radio][name=output]').change(function(){
	if (this.value == 'zawgyi') {
		$("#destination").css("font-family" , "Zawgyi-One");
	}
	if (this.value == 'unicode') {
		$("#destination").css("font-family", "Pyidaungsu");
	}
	if (this.value == 'winmyanmar'){
		$('#destination').css("font-family", "win_innwaregular");
	}
});
});
