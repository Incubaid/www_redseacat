
    // carousel demo

!function ($) {

    $('#myCarousel').carousel()
    
}(window.jQuery)

/*Fady*/
/*
$(document).ready(function(){
	var str=location.href.toLowerCase();
		$('li.active').removeClass("active");
		$('.nav li a').each(function() {
	if (str.indexOf(this.href.toLowerCase()) > -1)
	{
		$(this).parents('li').addClass("active"); 
	}
	}); 
		 
})
*/
$(document).ready(function(){
	var str=location.href.toLowerCase();
		$('li.active').removeClass("active");
	$('.nav li a').filter(function() {return this.href.toLowerCase() == str; }).parents('li').addClass('active');
		 
})


/*Mohamed*/
/*
href = window.location.href;
parts = href.split("/");
currentPage = decodeURI(parts[parts.length -1]);
menuitemsel = "li:has(a[href*='"+ currentPage +"']), li:has(a[href*='" + encodeURI(currentPage) + "'])";
$("li.active").removeClass("active");
$(menuitemsel).addClass("active");
*/