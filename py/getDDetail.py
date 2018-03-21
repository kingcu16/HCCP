# -*- coding: utf-8 -*-
"""

@author: CopperWang
@email: kingcu16@163.com

"""
import requests
from bs4 import BeautifulSoup

class getMouthData(object):
	"""docstring for getMouthData"""	
	def __init__(self):	
		self.urls='http://lishi.tianqi.com/arongqi/201802.html'
		self.H={
				'User-Agent':'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/64.0.3282.140 Safari/537.36'}
		self.detailData=[]
		'''{
			日期：
			最高温：
			最低温：
			天气：
			风向：
			风力:
		}'''
		self.proxy={}
	def Init(self):
		self.detailData=[]
		try:
			r=requests.get(self.urls,headers=self.H,proxies=self.proxy)
			r.raise_for_status()
			bcon=BeautifulSoup(r.text,'html.parser')
			d=bcon.find_all('div','tqtongji2')[0].find_all('ul')[1:]
			for cols in d:
				row=cols.find_all('li')
				temprow={}
				if len(row[0].find_all('a'))==0:
					temprow['日期']=str(row[0].string)
				else:
					temprow['日期']=str(row[0].find_all('a')[0].string)
				temprow['最高温']=str(row[1].string)
				temprow['最低温']=str(row[2].string)
				temprow['天气']=str(row[3].string)
				temprow['风向']=str(row[4].string)
				temprow['风力']=str(row[5].string)
				self.detailData.append(temprow)
		except Exception as e:
			print(e)
			print(self.urls)
	def Save(self,Path='detailData.txt'):
		with open(Path,'w') as f:
				for i in self.detailData:
					for key in i:
						f.write(i[key]+'\t')
					f.write('\n')
	def getData(self):
		return self.detailData