# -*- coding: utf-8 -*-
"""

@author: CopperWang
@email: kingcu16@163.com

"""

import requests
from bs4 import BeautifulSoup
import re

class  getDetail(object):
	"""docstring for  getDetail"""
	def __init__(self):
		self.urls='http://lishi.tianqi.com/acheng/index.html'
		self.H={
			'User-Agent':'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/64.0.3282.140 Safari/537.36'}
		self.proxy={}
		self.details=[]
		'''
		self.details=[
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
		self.weathername=['晴','雨','多云','雪','阴','沙尘']
	def Init(self):
		self.details=[]
		try:
			r=requests.get(self.urls,headers=self.H,proxies=self.proxy,timeout=2)
			r.raise_for_status()
			bcon=BeautifulSoup(r.text,'html.parser')
			dataall=bcon.find_all('div','tqtongji')
			data1=dataall[1].find_all('p')[0]
			s=str(data1)
			temp=re.findall(r'\d{4}-\d{2}-\d{2}', s)
			detail1={}
			detail1['from']=temp[0]
			detail1['to']=temp[1]
			self.details.append(detail1)
			detail1={}
			#获取天气数据
			for i in self.weathername:
				temp=re.findall(r''+i+r'\d{1,4}', s)
				if len(temp)==0:
					detail1[i]=0
				else:
					detail1[i]=int(temp[0][len(i):])
			self.details.append(detail1)
			#获取风力风向数据
			for  j in [2,3]:
				detail1={}
				data1=dataall[j].find_all('li')
				for i in data1:
					temp=str(i.string).split('（')
					detail1[temp[0]]=int(temp[1][:-2])
				self.details.append(detail1)
			#获取月份信息地址
			detail1={}
			data1=bcon.find_all('div','tqtongji1')[0].find_all('a')
			for i in data1:
				temp=re.findall(r'\d{2,4}', str(i.string))
				year,mm=int(temp[0]),int(temp[1])
				detail1[str(year)+'-'+str(mm)]=i['href']
			self.details.append(detail1)
		except Exception as e:
			self.details=[]
			print(e)
			print(self.urls)
	def Save(self,Path='details.txt'):
		with open(Path,'w',encoding='utf-8') as f:
				for i in self.details:
					for key in i:
						f.write(str(key)+':'+str(i[key])+'\n')
	def getData(self):
		return self.details