/*
传入参数：{
    维度：
    内容：
    区域：
    地方：
    Class:
}
*/
/*返回值
{
    name:[],
    value:[]
}*/
function DataInit(flag){
    var DataForReturn;
    $.post("../py/run.py",
        flag,
        function(data)
        {
            DataForReturn=data;
        });
}
function getDetailData(city,date){
    if($.inArray(city,document.CityData)==-1)
    {
        return null;
    }
    var DataForReturn={
        'name':[],
        'value':[],
        'x':[]
    };
    return null;
}