# -*- coding: utf-8 -*-
"""
Created on Tue Feb 27 16:38:51 2018

@author: CopperWang
@email: kingcu16@163.com

"""

import requests
from bs4 import BeautifulSoup

class IPagent:
    self.urls='http://www.xicidaili.com/nn/'
    self.Stop=100
    self.IpListAll=[]
    self.http=[]
    self.IpListUse=[]
    self.H={
       'Upgrade-Insecure-Requests':'1',
       'User-Agent':'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/64.0.3282.140 Safari/537.36'}
    def StartGet(self):
        for i in range(1,self.Stop):
            try:
                r=requests.get(self.urls+str(i),headers=self.H)
                r.raise_for_status()
                r.encoding=r.apparent_encoding
                t=BeautifulSoup(r.text,'html.parser').find_all('table')[0].find_all('tr')[1:]
                s=''
                for j in t:
                    temp=j.find_all('td')
                    s=str(temp[1].string)+':'+str(temp[2].string)
                    self.IpListAll.append(s)
                    #print(s)
                    s=str(temp[5].string)
                    self.http.append(s.lower())
                    #(s.lower())
            except:
                pass
        for i in range(len(self.http)):
            proxy={self.http[i]:self.http[i]+'://'+self.IpListAll[i]}
            try:
                r=requests.get('http://httpbin.org/get',proxies=proxy,timeout=1,headers=self.H)
                r.raise_for_status()
                IpListUse.append((self.http[i],self.IpListAll[i]))
                #print(r.text[:10])
            except:
                pass
    def Save(self,Path='IP.txt'):
        with open(Path,'w') as f:
            for h,i in IpListUse:
                f.write(h+','+i+'\n')

if __name__ == '__main__':
    I=IPagent();
    I.StartGet();
    I.Save();