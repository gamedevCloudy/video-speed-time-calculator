def TimeInSeconds(time):
    time=time.split(":")
    temp=[]
    for i in time:
        temp.append(int(i))
    return temp[0]*3600+temp[1]*60+temp[2]

def TimeInHMS(timeInSeconds):
    h=timeInSeconds//3600
    m=(timeInSeconds-(h*3600))//60
    s=(timeInSeconds-(m*60)-(h*3600))
    return (h,m,s)

def TimeRequiredToWatch(videoLength, rate):
    time = TimeInSeconds(videoLength)
    time//=rate
    t=TimeInHMS(time)
    return("%d:%d:%d"%(t[0],t[1],t[2]))
