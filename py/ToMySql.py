# -*- coding: utf-8 -*-
"""

@author: CopperWang
@email: kingcu16@163.com

"""

import os
import re
import pymysql
import pymysql.cursors
config={'host':'123.206.208.213','user':'root','password':'king','db':'HCCP','port':3306,'charset':'utf8'}
I_string=''
try:
    conn=pymysql.connect(**config)
    cursor=conn.cursor()
    source_dir='../data/'
    cityParten=re.compile(r'.*tj.txt')
    cityParten1=re.compile(r'[^0-9A-Za-z\-\.]*')
    for root,subdir,files in os.walk(source_dir):
        for spf in files:
            if re.match(cityParten, spf):
                city=spf[:-6]
                with open(os.path.join(source_dir,spf)) as f:
                    from_t=f.readline()[5:-1]
                    to_t=f.readline()[3:-1]
                    for s in f.readlines():
                        info=s.split(':')
                        if info[0]=='from' or info[0]=='to' or len(info[1])>10 or len(info[0])==0 or info[0][0]=='h':
                            continue
                        I_string='insert into tqtongji values("'+city+'","'+from_t+'","'+to_t+'","'+info[0]+'",'+info[1][:-1]+');'
                        cursor.execute(I_string)
            else:
                city=re.findall(cityParten1,spf)[0]
                with open(os.path.join(source_dir,spf)) as f:
                    for s in f.readlines():
                        info=s.split('\t')
                        date='2018-03'
                        if info[0]=='日期':
                            date=info[1][:-1]
                        else:
                            I_string='insert into tqdetail values("'+city+'","'+date+'","'+info[0]+'","'+info[1][:-1]+'");'
                            cursor.execute(I_string)
    conn.close()
except Exception as e:
    print(e)
    print(I_string)
finally:
    conn.close()