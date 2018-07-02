import csv
fp = open('../files/test.csv','w+') 
writer = csv.writer(fp) 
writer.writerow(('id','name'))
writer.writerow(('id','name'))
writer.writerow(('id','name'))
writer.writerow(('id','name'))
