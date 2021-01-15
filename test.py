import pandas as pd
import numpy as np
#with open('282A20-25 Column 1 Process 001.csv',newline='') as csvfile:
a=pd.read_csv('282A20-25 Column 1 Process 001.csv',sep='\t',encoding='utf16',skiprows=2)

b=[max(a[min]),max(a['min.1']),max(a['min.2']),max(a['min.3']),max(a['min.4']),max(a['min.5']),max(a['min.6']),max(a['min.7']),max(a['min.8']),max(a['min.9']),max(a['min.10'])]
res=1/150
myRange=range(0,int(np.int(max(b))),np.int(np.ceil((max(b)-3))/res))

print(a)
#mAU sample =8/1000+1/3000
array=np.array[a[mAU][0]]



#a.combine(a.[min])
#b=pd.concat(a[min],a['min.1'],a['min.2'],a['min.3'],a['min.4'],a['min.5'],a['min.6'],a['min.7'],a['min.8'],a['min.9'])#,a['min.10'])
#=a[min]+a['min.1']+a['min.2']+a['min.3']+a['min.4']+a['min.5']+a['min.6']+a['min.7']+a['min.8']+a['min.9']+a['min.10']

#print(max(b))
#zipped=zip(a[min])
#print(max(a[min],a['min.1']))




#for i in range(1,10):
#    string='min.'+str(i)
#    print(max(a[str]))
