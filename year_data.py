import pandas as pd


def avg_data_2013():
    
    average=[]
    for rows in pd.read_csv('Data/AQI/aqi2013.csv', chunksize=24):
        add_var=0
        avg=0
        data=[]
        df=pd.DataFrame(rows)
#         print(df)

        for _,row in df.iterrows():
#             print(row)
            data.append(row["PM2.5"])
#         print(len(data))
#         print(data)
    
        for i in data:
            if type(i) is int or type(i) is float:
                add_var +=i
            elif type(i) is str:
                if i!='NoData' and i!='PwrFail' and i!='---' and i!='InVld' :
                    temp=float(i)
                    add_var += temp
            
        avg=add_var/24
        average.append(avg)
            
    return (average)



def avg_data_2014():
    
    average=[]
    for rows in pd.read_csv('Data/AQI/aqi2014.csv', chunksize=24):
        add_var=0
        avg=0
        data=[]
        df=pd.DataFrame(rows)
#         print(df)

        for _,row in df.iterrows():
#             print(row)
            data.append(row["PM2.5"])
#         print(len(data))
#         print(data)
    
        for i in data:
            if type(i) is int or type(i) is float:
                add_var +=i
            elif type(i) is str:
                if i!='NoData' and i!='PwrFail' and i!='---' and i!='InVld' :
                    temp=float(i)
                    add_var += temp
            
        avg=add_var/24
        average.append(avg)
            
    return (average)



def avg_data_2015():
    
    average=[]
    for rows in pd.read_csv('Data/AQI/aqi2015.csv', chunksize=24):
        add_var=0
        avg=0
        data=[]
        df=pd.DataFrame(rows)
#         print(df)

        for _,row in df.iterrows():
#             print(row)
            data.append(row["PM2.5"])
#         print(len(data))
#         print(data)
    
        for i in data:
            if type(i) is int or type(i) is float:
                add_var +=i
            elif type(i) is str:
                if i!='NoData' and i!='PwrFail' and i!='---' and i!='InVld' :
                    temp=float(i)
                    add_var += temp
            
        avg=add_var/24
        average.append(avg)
            
    return (average)


def avg_data_2016():
    
    average=[]
    for rows in pd.read_csv('Data/AQI/aqi2016.csv', chunksize=24):
        add_var=0
        avg=0
        data=[]
        df=pd.DataFrame(rows)
#         print(df)

        for _,row in df.iterrows():
#             print(row)
            data.append(row["PM2.5"])
#         print(len(data))
#         print(data)
    
        for i in data:
            if type(i) is int or type(i) is float:
                add_var +=i
            elif type(i) is str:
                if i!='NoData' and i!='PwrFail' and i!='---' and i!='InVld' :
                    temp=float(i)
                    add_var += temp
            
        avg=add_var/24
        average.append(avg)
            
    return (average)


def avg_data_2017():
    
    average=[]
    for rows in pd.read_csv('Data/AQI/aqi2017.csv', chunksize=24):
        add_var=0
        avg=0
        data=[]
        df=pd.DataFrame(rows)
#         print(df)

        for _,row in df.iterrows():
#             print(row)
            data.append(row["PM2.5"])
#         print(len(data))
#         print(data)
    
        for i in data:
            if type(i) is int or type(i) is float:
                add_var +=i
            elif type(i) is str:
                if i!='NoData' and i!='PwrFail' and i!='---' and i!='InVld' :
                    temp=float(i)
                    add_var += temp
            
        avg=add_var/24
        average.append(avg)
            
    return (average)



def avg_data_2018():
    
    average=[]
    for rows in pd.read_csv('Data/AQI/aqi2018.csv', chunksize=24):
        add_var=0
        avg=0
        data=[]
        df=pd.DataFrame(rows)
#         print(df)

        for _,row in df.iterrows():
#             print(row)
            data.append(row["PM2.5"])
#         print(len(data))
#         print(data)
    
        for i in data:
            if type(i) is int or type(i) is float:
                add_var +=i
            elif type(i) is str:
                if i!='NoData' and i!='PwrFail' and i!='---' and i!='InVld' :
                    temp=float(i)
                    add_var += temp
            
        avg=add_var/24
        average.append(avg)
            
    return (average)
