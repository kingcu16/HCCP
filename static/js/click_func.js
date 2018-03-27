$(function(){
	document.Flag={
		'区域':'全国',
		'地方':'中国',
		'维度':'统计',
		'内容':'天气',
		'Class':'map',
		'时间':'2018-2'
	};
	var TimeFlag;
	$("#tongjiData,#detailData,#choiceData,#quyuChoice,#Class").click(function(){
		$(this).next().fadeToggle();
	});
	$('#date').change(function (){
		document.Flag['时间']=$(this).val();
	})
	$("#quyu").click(function(){
		if($(this).find("option:selected").text()=="地方"){
			$(this).parent().next().fadeToggle();
			$(this).parent().next().next().fadeToggle();
			document.Flag['区域']='地方';
			document.Flag['时间']='2018-2';
		}
		else{
			document.Flag['区域']='全国';
			document.Flag['地方']='中国'
		}
	});
	$("#sf").click(function(){
		document.Flag['地方']=$(this).find("option:selected").text();
	});
	$("#tongjiData").click(function(){
		document.Flag['维度']="统计";
	});
	$("#detailData").click(function(){
		document.Flag['维度']="详细";
	});
	$("#tongjiData").next().find('li').click(function(){
		if(this.F)
		{
			this.F=false;
			$(this).parent().find('li').attr('style','');
			document.Flag['维度']="统计";
			document.Flag['内容']="";
		}
		else{
			this.F=true;
			$(this).parent().find('li').attr('style','');
			$(this).attr('style','background-color: #72bab5;');
			document.Flag['维度']="统计";
			document.Flag['内容']=$(this).text();
		}		
	});
	$("#detailData").next().find('li').click(function(){

		if(this.F)
		{
			this.F=false;
			$(this).parent().find('li').attr('style','');
			document.Flag['维度']="详细";
			document.Flag['内容']='';
		}
		else{
			this.F=true;
			$(this).parent().find('li').attr('style','');
			$(this).attr('style','background-color: #72bab5;');
			document.Flag['维度']="详细";
			document.Flag['内容']=$(this).text();
		}
	});
	$("#Class").next().find('li').click(function(){
		
		if(this.F)
		{
			this.F=false;
			$(this).parent().find('li').attr('style','');
			document.Flag['Class']='';
		}
		else{
			this.F=true;
			$(this).parent().find('li').attr('style','');
			$(this).attr('style','background-color: #72bab5;');
			document.Flag['Class']=$(this).attr('id');
		}
	});
	$('#tjiao').click(function(){
		var Data=DataInit(document.Flag);
		//alert(Data);
		var title={
			text:document.Flag['区域']+document.Flag['维度']+document.Flag['内容']+'信息',
			left: 'center',
		    textStyle: {
		            color: '#fff'
		        }
		}

		EchartInit(document.getElementById('dituContent'),Data,title,document.Flag['Class'],document.Flag);
	})
})