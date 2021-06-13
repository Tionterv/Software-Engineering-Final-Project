import pandas as pd
import math
from collections import defaultdict



filepath = 'data.csv'



#read from the csv file
def csv_read():
    try:
        df = pd.read_csv(filepath)
        df.reset_index(drop=True, inplace=True)
        csv = df.transpose().to_dict()
        data = csv
        ret = defaultdict()
        #iterates through each index and adds to dictionary
        for x in list(data.values()):
            temp = list(x.values())
            if math.floor(float(temp[0])) not in ret : ret[math.floor(float(temp[0]))] = [temp[1]] * temp[2]
            else : ret[math.floor(float(temp[0]))] += ([temp[1]] * temp[2])
        return ret
    except:
        return {}



#write to the csv file
def csv_write(data):
    write = {}
    #iterate through dictionary
    for x in data:
        num = 0
        unique = list(set(data[x]))
        #for every unique location, add definition to write with location and quantity
        for y in unique:        
            total = 0
            for z in data[x]:
                if z is y : total += 1            
            #print("ID:",num,' Location:',y,' Quantity:',total)
            if int(x)+(num/math.pow(10,len(str(num)))) not in write:
                write[int(x)+(num/math.pow(10,len(str(num))))] = [y,total]
            else:
                num += 1
                write[int(x)+(num/math.pow(10,len(str(num))))] = [y,total]
            num += 1
    df = pd.DataFrame(write,['Location','Quantity'])
    df = df.transpose()
    df.to_csv(filepath, index=True)

    

#emtpies the csv file
def clear_csv():
    df = pd.DataFrame({})
    df.to_csv(filepath)
