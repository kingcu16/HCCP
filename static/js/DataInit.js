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
    $.ajaxSetup({
        async: false
    });
    $.post("getData",
        flag,
        function(data)
        {
            DataForReturn=$.parseJSON(data);
            //alert(data['value']);
        });
    return DataForReturn;
}