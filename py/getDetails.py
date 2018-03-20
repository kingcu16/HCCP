# -*- coding: utf-8 -*-
"""

@author: CopperWang
@email: kingcu16@163.com

"""

import requests
from bs4 import BeautifulSoup
import re
urls='http://lishi.tianqi.com/acheng/index.html'
H={
	       'User-Agent':'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/64.0.3282.140 Safari/537.36'}

details=[]
'''
details=[
	{
		'where':
		'from':
		'to':
	}
	{
		'qing':
		'yu':
		'duoyun':
		'yu':
		'xue':
		'yin':
		'other'
	}
	,
	{
		''
		#风向
	}
	,
	{
		''
		#风力
	}
	{
		'time':'url'
		#具体
	}
]
'''
try:
	r=requests.get(urls,headers=H)
	r.raise_for_status()
	bcon=BeautifulSoup(r.text,'html.parser')
	dataall=bcon.find_all('div','tqtongji')
	data1=dataall[1].find_all('p')[0]
	temp=re.findall(r'\d{4}-\d{2}-\d{2}', str(data1))
	details={}
	detail1['from']=temp[0]
	detail1['to']=temp[1]
except Exception as e:
	raise e