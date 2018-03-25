#!/usr/bin/python3 python3
# -*- coding: utf-8 -*-
"""

@author: CopperWang
@email: kingcu16@163.com

"""
from flask import Flask,request,render_template
from flask import json
import re
app=Flask(__name__)

@app.route('/HCCP/html/index.html')
def index():
    return render_template("index.html")

@app.route("/HCCP/html/getData")
def getData():
    ReturnData=None
    flag=json.loads(request.form.get('data'))
    if flag['维度']=='统计':
        if flag['区域']=='全国':
            if flag['内容']=='风向':
                return json.dumps(ReturnData)
            if flag['内容']=='风力':
                return json.dumps(ReturnData)
            if flag['内容']=='天气':
                if flag['Class']!='map':
                    return json.dumps(ReturnData)
                return getWeatherDataTjCH()
        if flag['区域']=='地方':
            if flag['Class']=='map':
                return json.dumps(ReturnData)
            if flag['Class']=='line':
                return json.dumps(ReturnData)
            return getSomeWhereDataTj(flag['地方'],flag['内容'])
    if flag['维度']=='详细':
        if flag['内容']=='温度':
            if flag['Class']!='line':
                return json.dumps(ReturnData)
            return getTempData(flag['地方'],flag['时间'])
        else:
            if flag['Class']=='map':
                return json.dumps(ReturnData)
            return getDetailData(flag['地方'],flag['时间'],flag['内容'])
    return json.dumps(ReturnData)

def getWeatherDataTjCH():
    ReturnData=None
    if len(CityData)==0:
        return json.dumps(ReturnData)
    ReturnData={}
    for c in CityData:
        with open('../data/'+c+'tj.txt') as f:
            for s in f.readlines():
                Info=s.split(':')
                if(Info[0]=='晴'):
                    ReturnData['value'].append(int(Info[1]))
    return json.dumps(ReturnData)
def getSomeWhereDataTj(city,con):
    if not city in CityData:
        return json.dumps(None)
    C={
        '天气':['晴','雨','多云','雪','阴','沙尘'],
        '风力':['微风','1级','2级','3级','4级','5级','6级','7级','7级以上'],
        '风向':['东风','西风','北风','南风','东北风','西北风','东南风','西南风']
    }
    ReturnData={}
    if not con in C.keys:
        return json.dumps(None)
    else:
        ReturnData['name']=C[con]
        ReturnData['x']=C[con]
    ReturnData['value']=[0]*len(C[con])
    with open('../data/'+city+'tj.txt') as f:
        for s in f.readlines():
            Info=s.split(':')
            for i in range(len(C[con])):
                if re.match(C[con][i],Info[0]):
                    ReturnData['value'][i]+=int(Info[1]);
    return json.dumps(ReturnData)
def getDetailData(city,date,con):
    if not city in CityData:
        return json.dumps(None)
    C={
        '天气':['晴','雨','多云','雪','阴','沙尘'],
        '风力':['微风','1级','2级','3级','4级','5级','6级','7级','7级以上'],
        '风向':['东风','西风','北风','南风','东北风','西北风','东南风','西南风']
    }
    ReturnData={}
    if not con in C.keys:
        return json.dumps(None)
    else:
        ReturnData['name']=C[con]
        ReturnData['x']=C[con]
    ReturnData['value']=[0]*len(C[con])
    with open('../data/'+city+date+'d.txt') as f:
        for s in f.readlines():
            Info=s.split(':')
            for i in range(len(C[con])):
                if re.match(con,Info[0]):
                    if re.match(C[con][i], Info[1]):
                        ReturnData['value'][i]+=1;
    return json.dumps(ReturnData)
def getTempData(city,date):
    if not city in CityData:
        return json.dumps(None)
    ReturnData={
    'data':[['最高温'],['最低温']],
    'x':[]
    }
    with open('../data/'+city+date+'d.txt') as f:
        for s in f.readlines():
            Info=s.split('\t')
            if Info[0]=='日期':
                ReturnData['x'].append(Info[1][:-1])
            if Info[0]=='最高温':
                ReturnData['data'][0].append(int(Info[1]))
            if Info[0]=='最低温':
                ReturnData['data'][1].append(int(Info[1]))
    return json.dumps(ReturnData)
if __name__ == '__main__':
    CityData=[
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
    app.run()