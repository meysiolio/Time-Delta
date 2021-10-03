from datetime import datetime as dt

date_list = []
fmt = '%a %d %b %Y %H:%M:%S %z'

for date in range(int(input())):
    date_list.append(int(abs((dt.strptime(input(), fmt) -
                   dt.strptime(input(), fmt)).total_seconds())))                                          
for j in date_list:
    print(j)