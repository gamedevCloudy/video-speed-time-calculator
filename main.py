import vidspeedtime as vst


def main():
    opt=1
    while(opt !=0):
        print("\n\nCalculate time required to watch a video at any rate: ")
        opt= int(input("\n1. Use \n0. Exit \nChoice:"))
        if opt==1:
            time=input("\nTime(HH:MM:SS): ")
            rate=float(input("\nVideo Rate: "))
            timeReq= (vst.TimeRequiredToWatch(time,rate))
    
            print("\n\nIt will take you %s to watch this video at %fx."%(timeReq,round(rate,2)))
        else: exit


main()