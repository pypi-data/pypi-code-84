import numpy as np
import os
import datetime
import argparse


def degMinSectoDeg(a):
    deg = int(a.split("°")[0])
    sec = int(a.split("'")[-1][:-1])
    min = int(a.replace(f"{deg}°","").replace(f"'{sec}\"",""))
    return deg+min/60+sec/3600

def normal(data, min=None, max=None):
    if max is None:
        max = np.max(data)
    if min is None:
        min = np.min(data)
    rangeLat = max-min
    dataB = (data - min) / rangeLat
    return dataB

def mkDir(path):
    if "." in path:
        os.makedirs(os.path.dirname(path),exist_ok=True)
    else:
        os.makedirs(path, exist_ok=True)

def options():
    parser = argparse.ArgumentParser(description='hjn')
    parser.add_argument('--times', type=str, default='2018060700,2018060700')
    parser.add_argument('--isDebug',action='store_true',default=False)
    config= parser.parse_args()
    config.times = config.times.split(",")
    if len(config.times) == 1:
        config.times = [config.times[0], config.times[0]]
    config.times = [datetime.datetime.strptime(config.times[0], "%Y%m%d%H%M"),
                    datetime.datetime.strptime(config.times[1], "%Y%m%d%H%M")]

    return config


def totalTimes(delta,second):
    return (delta.days*24*3600+delta.seconds)//second

def timeSeq(start,end,secInter,endPoint=True):
    times=totalTimes((end-start),secInter)
    end = 1 if endPoint else 0
    return list(map(lambda x:start+relativedelta(seconds=x*secInter),range(times+end)))

def normalNC(data):
    mx=np.nanmax(data)
    mn = np.nanmin(data)
    rangeV=mx-mn
    scale = rangeV/254
    offset = (mx+mn)/2
    data1=(data - offset)/scale
    data1[np.isnan(data1)] = -128
    return data1,scale,offset


def expend(data,latArr,lonArr,dim=2):
    latOffset = int((LeftTopCornerPairArr[0]["evn"].n - latArr[0]) / 0.01)
    latOffsetDown = int((latArr[-1] - LeftTopCornerPairArr[3]["evn"].s) / 0.01)
    lonOffset = int((lonArr[0] - LeftTopCornerPairArr[6]["evn"].w) / 0.01)
    lonOffsetRight = int((LeftTopCornerPairArr[0]["evn"].e - lonArr[-1]) / 0.01)
    appendLat = np.asarray(list(map(lambda x: latArr[0] + x * 0.01, range(1, latOffset + 2)))[::-1])
    appendLatDown = np.asarray(list(map(lambda x: latArr[-1] - x * 0.01, range(1, latOffsetDown + 2))))
    latArr = np.r_[appendLat, latArr]
    latArr = np.r_[latArr, appendLatDown]
    appendLon = np.asarray(list(map(lambda x: lonArr[0] - x * 0.01, range(1, lonOffset + 2)))[::-1])
    appendLonRight = np.asarray(list(map(lambda x: lonArr[-1] + x * 0.01, range(1, lonOffsetRight + 2))))
    lonArr = np.r_[appendLon, lonArr]
    lonArr = np.r_[lonArr, appendLonRight]

    if latOffset<0:
        latOffset=0
    if latOffsetDown < 0:
        latOffsetDown = 0
    if lonOffset < 0:
        lonOffset = 0
    if lonOffsetRight < 0:
        lonOffsetRight = 0

    if dim==2:
        data = np.pad(data, ((latOffset+1 , latOffsetDown+1 ), (lonOffset+1 , lonOffsetRight+1)),constant_values=np.nan)
    elif dim==3:
        data = np.pad(data, ((0, 0), (latOffset+1, latOffsetDown+1), (lonOffset+1, lonOffsetRight+1)), constant_values=np.nan)
    elif dim==4:
        data = np.pad(data, ((0, 0),(0, 0), (latOffset+1, latOffsetDown+1), (lonOffset+1, lonOffsetRight+1)), constant_values=np.nan)
    return data,latArr,lonArr

def UV2WSWD(U,V):
    ws = np.sqrt(np.square(U) + np.square(V))
    wd = (np.degrees(np.arctan2(-U, -V))+ 360)%360
    return ws,wd

def WSWD2UV(ws,wd):
    u=- ws*np.sin(np.radians(wd))
    v=- ws*np.cos(np.radians(wd))
    return u,v





