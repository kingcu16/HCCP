# -*- coding: utf-8 -*-
"""

@author: CopperWang
@email: kingcu16@163.com

"""

import requests
from bs4 import BeautifulSoup

class CityData:
	def __init__(self):
		self.urls='http://lishi.tianqi.com'
		self.CityData={}
		self.H={
		       'User-Agent':'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/64.0.3282.140 Safari/537.36'}
	def Init(self):
		try:
			r=requests.get(self.urls, headers=self.H)
			r.raise_for_status()
			uls=BeautifulSoup(r.text,'html.parser').find_all('ul','bcity')
			for ul in uls:
				lis=ul.find_all('a')
				#self.Alpha.append(str(lis[0].string))
				lis=lis[1:]
				tempData=[]
				for l in lis:
					self.CityData[str(l.string)]=str(l['href'])
		except Exception as e:
			#print("SHIT!")
			print(e)
	def Save(self,Path='../data/citys.txt'):
		with open(Path,'w',encoding='utf-8') as f:
			#for i in range(len(self.Alpha)):
			for j in self.CityData:
				f.write(j+'\t'+self.CityData[j]+'\n')
	def getData(self):
		return self.CityData

if __name__ == '__main__':
	I=CityData()
	I.Init()
	I.Save()