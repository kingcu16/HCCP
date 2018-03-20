# -*- coding: utf-8 -*-
"""

@author: CopperWang
@email: kingcu16@163.com

"""

import requests
from bs4 import BeautifulSoup

class CityData:
	self.urls='http://lishi.tianqi.com'
	self.Alpha=[]
	self.Data=[]
	self.H={
	       'Upgrade-Insecure-Requests':'1',
	       'User-Agent':'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/64.0.3282.140 Safari/537.36'}
	def Init(self):
		try:
			r=requests.get(self.urls, headers=self.H)
			r.raise_for_status()
			uls=BeautifulSoup(r.text,'html.parser').find_all('ul','bcity')
			for ul in uls:
				lis=ul.find_all('a')
				self.Alpha.append(str(lis[0].string))
				lis=lis[1:]
				tempData=[]
				for l in lis:
					tempDict=[str(l.string),str(l['href'])]
					tempData.append(tempDict)
				self.Data.append(tempData)
		except Exception as e:
			#print("SHIT!")
			print(e)
	def Save(self,Path='../data/citys.txt'):
		with open(Path,'w') as f:
			for i in range(len(self.Alpha)):
				for j in self.Data[i]:
					f.write(j[0]+'\t'+j[1]+'\n')
	def GetData(self):
		return self.Data

if __name__ == '__main__':
	I=CityData()
	I.Init()
	I.Save()