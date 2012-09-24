function on_load() {
	
	
	$(window).scroll(function(){
		if  ($(window).scrollTop() >= 229){
			$('#main_table').css({position:'relative',top:46});
		} else {
			$('#main_table').css({top:0});
        }
        
        if  ($(window).scrollTop() >= 229) {
			$('#navigation_table').css({position:'fixed',top:0,left:'50%',margin:'0 0 0 -487.5px'});
		}
	});
}

//$(document).ready(on_load)
