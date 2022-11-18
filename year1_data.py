import pandas as pd




def avg_data(start_year, end_year):
    
    year_wise_average=[] 
    
    for year in range(start_year, end_year+1):
        
        average=[] 
        
        for rows in pd.read_csv(f'Data/AQI/aqi{year}.csv',chunksize=24):
            data=[]
            add_var=0
            avg=0

            df=pd.DataFrame(data=rows)
            for _,row in df.iterrows():
                data.append(row['PM2.5'])

            for i in data:
                if type(i) is float or type(i) is int:
                    add_var+=i

                elif type(i) is str:
                    if i!='NoData' and  i!='PwrFail' and  i!='---' and i!='InVld':
                        temp=float(i)
                        add_var+=temp

            avg=add_var/24
            average.append(avg)
        
        year_wise_average.append(average)    
    return(year_wise_average)