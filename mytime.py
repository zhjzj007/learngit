# -*- coding: utf-8 -*-
"""
Created on Sun Apr 26 21:04:06 2020

@author: ZJ
"""

import time
from datetime import datetime
import pandas as pd



def doy(y,m,d):
    y=int(y)
    m=int(m)
    d=int(d)
    t1=datetime(y,m,d)
    t2=time.localtime(t1.timestamp())
    return t2.tm_yday
    
    
def date(y,doy):
    y=str(y)
    doy=str(doy)
    t1=datetime.strptime(y+doy,'%Y%j')
    t2=time.localtime(t1.timestamp())
    return t2.tm_year,t2.tm_mon,t2.tm_mday
    
    
    
def dif_day(d1=[0,0,0],d2=[0,0,0]):
    
    t1=datetime(d1[0],d1[1],d1[2])
    t2=datetime(d2[0],d2[1],d2[2])
    # t1=datetime(y1,m1,d1)
    # t2=datetime(y2,m2,d2)
    delta=t2-t1
    return delta.days


if __name__=='__main__':
    
    df=pd.DataFrame({'年':[2019,2011,2019,2017,2018],
                    '月':[2,3,5,1,12],
                    '日':[11,31,15,7,8]})

    df['doy']=df.apply(lambda x:doy(x['年'],x['月'],x['日']),axis=1)





