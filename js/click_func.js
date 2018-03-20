$(function(){

	$('.menu-1').click(function(){
		$(this).next().fadeToggle();
	})
	var ff=$('.menu-1');
	for(var i=0;i<ff.length;i++)
	{
		var tt=ff[i].getElementsByClassName('menu-2');
		for(var j=0;j<tt.length;j++)
		{
			tt[i].click(function(){
				
			})
		}
	}
})