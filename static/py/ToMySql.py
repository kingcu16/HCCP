# -*- coding: utf-8 -*-
"""

@author: CopperWang
@email: kingcu16@163.com

"""

import os
import re
import pymysql
import pymysql.cursors
import threading

class ToMysql(threading.Thread):
    """docstring for ToMysql"""
    def __init__(self, tid,tname,ff):
        super(ToMysql, self).__init__()
        self.tid = tid
        self.tname=tname
        self.config={'host':'123.206.208.213','user':'for_insert','password':'king','db':'HCCP','port':3306,'charset':'utf8'}
        self.source_dir='../data/'
        self.cityParten=re.compile(r'.*tj.txt')
        self.cityParten1=re.compile(r'[^0-9A-Za-z\-\.]*')
        self.files=ff
    def run(self):
        InToSql(self.config,self.files,self.source_dir,self.cityParten,self.cityParten1,self.tname)

def InToSql(config,files,source_dir,cityParten,cityParten1,tname):
    print(tname+'正在启动')
    print(tname+'连接至数据库')
    conn=pymysql.connect(**config)
    cursor=conn.cursor()
    print(tname+'连接成功！')
    print(tname+'正在存储...')
    errorFile=[]
    try:
        for spf in files:
            try:
                if re.match(cityParten, spf):
                        city=spf[:-6]
                        with open(os.path.join(source_dir,spf),encoding='utf8') as f:
                            from_t=f.readline()[5:-1]
                            to_t=f.readline()[3:-1]
                            for s in f.readlines():
                                info=s.split(':')
                                if info[0]=='from' or info[0]=='to' or len(info[1])>10 or len(info[0])==0 or info[1][0]=='h':
                                    continue
                                I_string='insert into tqtongji values("'+city+'","'+from_t+'","'+to_t+'","'+info[0]+'",'+info[1][:-1]+');'
                                cursor.execute(I_string)
                                conn.commit()
                else:
                    city=re.findall(cityParten1,spf)[0]
                    with open(os.path.join(source_dir,spf),encoding='utf8') as f:
                        date='2018-03'
                        max_t='20'
                        min_t='10'
                        wind_p='1级'
                        wind_d='东风'
                        for s in f.readlines():
                            info=s.split('\t')
                            if info[0]=='日期':
                                date=info[1][:-1]
                            elif info[0]=='最高温':
                                max_t=info[1][:-1]
                            elif info[0]=='最低温':
                                min_t=info[1][:-1]
                            elif info[0]=='风力':
                                wind_p=info[1][:-1]
                            elif info[0]=='风向':
                                wind_d=info[1][:-1]
                            else:
                                I_string='insert into tqdetail values("'+city+'","'+date+'",'+max_t+','+min_t+',"'+wind_p+'","'+wind_d+'");'
                                cursor.execute(I_string)
                                conn.commit()
                global count
                lock.acquire()
                try:
                    count+=1
                    print(spf+'--%.3f%%'%(count/allFile*100))
                except Exception as e:
                    print(tname+':'+spf+'存储成功！')
                finally:
                    lock.release()
            except Exception as e:
                print(spf+'--error\n')
                errorFile.append(spf)
    finally:
        cursor.close()
        conn.close()
        print(tname+'存储完毕！')
        with open(tname,'w') as f:
            for i in errorFile:
                f.write(i+'\n')
if __name__ == '__main__':
    count=0
    allFile=1
    print('正在连接至数据库...')
    config={'host':'123.206.208.213','user':'for_insert','password':'king','db':'HCCP','port':3306,'charset':'utf8'}
    conn=pymysql.connect(**config)
    cursor=conn.cursor()
    cursor.execute('delete from tqdetail;')
    conn.commit()
    cursor.execute('delete from tqtongji;')
    conn.commit()
    cursor.close()
    conn.close()
    print('清除表数据成功！')
    print('正在进行存储...')
    lock=threading.Lock()
    for root,subdir,files in os.walk('../data/'):
        setup=300
        start=0
        ends=start+setup
        allFile=len(files)
        num=0
        t=[]
        while True:
            if start>=allFile:
                break
            t.append(ToMysql(num, 'Thread-'+str(num), files[start:ends]))
            print('正在启动线程'+str(num)+'...')
            t[num].start()
            print('线程'+str(num)+'已启动')
            num+=1
            start=ends
            ends+=setup
        for i in t:
            i.join()