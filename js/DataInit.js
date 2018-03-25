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
    $.post("123.206.208.213/HCCP/html/getData",
        flag,
        function(data)
        {
            DataForReturn=data;
        });
}