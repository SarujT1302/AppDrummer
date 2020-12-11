
import time

list1=[]

def click():
    if len(list1)<2:
        p=time.time()
        list1.append(p)
        BPM=str("please click to count")
        
            
    if len(list1)==2:
        p=time.time()
        list1.append(p)
        period=list1[1]-list1[0]
        BPM= int(60//period)
        list1.clear()

    return list1 , BPM


print(list1)

