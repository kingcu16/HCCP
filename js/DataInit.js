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
document.CityData=[
    '海门',
        '鄂尔多斯',
        '招远',
        '舟山',
        '齐齐哈尔',
        '盐城',
        '赤峰',
        '青岛',
        '乳山',
        '金昌',
        '泉州',
        '莱西',
        '上海',
        '攀枝花',
        '威海',
        '承德',
        '厦门',
        '汕尾',
        '潮州',
        '丹东',
        '太仓',
        '曲靖',
        '烟台',
        '福州',
        '湛江',
        '揭阳',
        '荣成',
        '连云港',
        '葫芦岛',
        '常熟',
        '蓬莱',
        '韶关',
        '嘉峪',
        '广州',
        '延安',
        '太原',
        '清远',
        '中山',
        '昆明',
        '寿光',
        '盘锦',
        '长治',
        '深圳',
        '章丘',
        '肇庆',
        '大连',
        '临汾',
        '吴江',
        '石嘴山',
        '沈阳',
        '苏州',
        '茂名',
        '嘉兴',
        '长春',
        '胶州',
        '银川',
        '张家港',
        '三门峡',
        '锦州',
        '泸州',
        '西宁',
        '宜宾',
        '呼和浩特',
        '成都',
        '大同',
        '镇江',
        '桂林',
        '张家界',
        '宜兴',
        '北海',
        '西安',
        '金坛',
        '东营',
        '牡丹江',
        '台州',
        '南京',
        '滨州',
        '贵阳',
        '无锡',
        '本溪',
        '克拉玛依',
        '渭南',
        '马鞍山',
        '宝鸡',
        '焦作',
        '句容',
        '北京',
        '徐州',
        '衡水',
        '包头',
        '绵阳',
        '乌鲁木齐',
        '枣庄',
        '杭州',
        '淄博',
        '鞍山',
        '溧阳',
        '库尔勒',
        '安阳',
        '开封',
        '济南',
        '德阳',
        '温州',
        '九江',
        '邯郸',
        '临安',
        '兰州',
        '沧州',
        '哈尔滨',
        '聊城',
        '芜湖',
        '唐山',
        '平顶山',
        '邢台',
        '德州',
        '济宁',
        '荆州',
        '宜昌',
        '义乌',
        '金华',
        '岳阳',
        '长沙',
        '衢州',
        '廊坊',
        '菏泽',
        '合肥',
        '武汉',
        '大庆'
        ];
function DataInit(flag){
    if(flag['维度']=='统计'){
        if(flag['区域']=='全国')
        {
            if(flag['内容']=='风向'){
                return null;
            }
            if(flag['内容']=='风力')
            {
                return null;
            }
            if(flag['内容']=='天气'){
                if(flag['Class']!='map')
                {
                    return null;
                }
                return getWeatherDataTjCH();
            }
        }
        if(flag['区域']=='地方'){
            if(flag['Class']=='map'){
                return null;
            }
            if(flag['Class']=='line')
            {
                return null;
            }
            return getSomeWhereDataTj(flag['地方'],flag['内容']);
        }
    }
    if(flag['维度']=='详细')
    {
        if(flag['内容']=='温度'){
            if(flag['Class']!='line')
            {
                return null;
            }
            return getTempData(flag['地方'],flag['时间'])
        }
        else{
            if(flag['Class']=='map')
            {
                return null;
            }
            return getDetailData(flag['地方'],flag['时间'])
        }
    }
}
function getWeatherDataTjCH(){
    if(!document.CityData)
    {
        console.write('No CityData');
        return null;
    }
    var fso, ts, s ; 
    var ForReading = 1; 
    var DataForReturn=new Array();
    fso = new ActiveXObject("Scripting.FileSystemObject"); 
   
    for(var c in document.CityData)
    {
        ts=fso.OpenTextFile("../data/"+c+'tj.txt', ForReading); 
        while(!f.AtEndOfStream)
        {
            var s=f.ReadLine();
            var Info=s.split(':');
            if(Info[0]=='晴'){
                DataForReturn.push(parseInt(Info[1]));
            }
        }
    }
    return DataForReturn;
}
function getSomeWhereDataTj(city,con){
    var C={
        '天气':['晴','雨','多云','雪','阴','沙尘'],
        '风力':['微风','1级','2级','3级','4级','5级','6级','7级','7级以上'],
        '风向':['东风','西风','北风','南风','东北风','西北风','东南风','西南风']
    };
    var DataForReturn={};
    if(!C[con])
    {
        return null;
    }
    else{
        DataForReturn['name']=C[con];
        DataForReturn['x']=C[con];
    }
    DataForReturn['value']=new Array(C[con].length);
    for(var i=0;i<C[con].length;i++)
    {
        DataForReturn['value'][i]=0;
    }
    if($.inArray(city,document.CityData)==-1)
    {
        return null;
    }
    var fso, ts, s ; 
    var ForReading = 1; 
    
    fso = new ActiveXObject("Scripting.FileSystemObject"); 
    ts=fso.OpenTextFile('../data/'+city+'tj.txt',ForReading);
    while(!ts.AtEndOfStream){
        var s=ts.ReadLine();
        var Info=s.split(':');
        for(var i =0;i<C[con].length;i++)
        {
            if(Info[0].search(C[con][i])!=-1)
            {
                DataForReturn['value'][i]+=parseInt(Info[1]);
            }
        }
    }
    return DataForReturn;
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
}
function getTempData(city,date){
    if($.inArray(city,document.CityData)==-1)
    {
        return null;
    }
    var DataForReturn={};
    DataForReturn['data']=[['最高温'],['最低温']];
    DataForReturn['x']=new Array();
    var fso, ts, s ; 
    var ForReading = 1; 
    fso = new ActiveXObject("Scripting.FileSystemObject"); 
    ts=fso.OpenTextFile('../data/'+city+date+'d.txt',ForReading);
    while(!ts.AtEndOfStream)
    {
        var s=ts.ReadLine();
        var Info=s.split('\t');
        if(Info[0].search(/^\d{4}/)!=-1)
        {
            DataForReturn['x'].push(Info[1].slice(5));
        }
        if(Info[0]=='最高温')
        {
            DataForReturn['data'][0].push(parseInt(Info[1]))
        }
        if(Info[0]=='最低温')
        {
            DataForReturn['data'][1].push(parseInt(Info[1]))
        }
    }
    return DataForReturn;
}