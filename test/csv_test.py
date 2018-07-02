import csv,os
path = os.getcwd()
print(path)
fp = open(path+'/files/test.csv','w+') 
writer = csv.writer(fp) 
writer.writerow(('id','name'))
writer.writerow(('id','name'))
writer.writerow(('id','name'))
writer.writerow(('id','name'))
