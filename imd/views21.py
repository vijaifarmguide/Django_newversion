from __future__ import unicode_literals
from django.shortcuts import render

# Create your views here.
    
from django.http import HttpResponse,JsonResponse
import math
import os, json
import numpy as np


# # In[4]:


#create two sql databases IP
try:
    import pymysql
    pymysql.install_as_MySQLdb()
except ImportError:
    pass

import json
import pandas as pd
import MySQLdb

import pandas as pd
from sqlalchemy import create_engine



#engine1 = create_engine('mysql+mysqldb://farmguideIP:ImageProcessing!@imageprocessing.cp7riswp4tg3.us-east-1.rds.amazonaws.com/image_processing')#, encoding='utf-8')
#engine=engine1.connect()


import datetime
month12 = datetime.datetime.now().strftime("%B")

def station_district_mapping(df):

    filename = datetime.date.today().strftime('%m-%d-%Y')+'_2.csv'
    import os.path
    # cache this in redis thats all instead of file
    if(os.path.isfile(filename)):
        print('yipeee')
        df3 = pd.read_csv(filename)
        return df3


    print(221,datetime.datetime.now())
    pf=pd.read_csv('/home/vijai_farmguide/Desktop/my_codes/weather1/district_mapped_weather_station123_prcp.csv')
    df[['Maximum Temp(Celsius)','Maximum Temp Departure from Normal(Celsius)', 'Minimum Temp(Celsius)','Minimum Temp Departure from Normal(Celsius)', '24 Hours Rainfall (mm)','Relative Humidity at 0830 hrs (%)','Relative Humidity at 1730 hrs (%)']] =df[['Maximum Temp(Celsius)','Maximum Temp Departure from Normal(Celsius)', 'Minimum Temp(Celsius)','Minimum Temp Departure from Normal(Celsius)', '24 Hours Rainfall (mm)','Relative Humidity at 0830 hrs (%)','Relative Humidity at 1730 hrs (%)']].apply(pd.to_numeric,errors='coerce')
    df[['Todays Sunset (IST)','Tommorows Sunrise (IST)', 'Moonset (IST)', 'Moonrise (IST)']] = df[['Todays Sunset (IST)','Tommorows Sunrise (IST)', 'Moonset (IST)', 'Moonrise (IST)']].apply(pd.to_timedelta,errors='coerce')
    print(222,datetime.datetime.now())
    df3=pd.DataFrame()
    for i in range(0,len(pf)): #327 iterations
        #print('hi',pf.loc[i,'district'])
        df1=pd.DataFrame()
        if((pf.loc[i,'dist1']==0)&(pf.loc[i,'dist2']==0)&(pf.loc[i,'dist3']==0)):
            #print('hiiiiiii',pf.loc[i,'district'])
            df1=df1.append(df[df['Weather Stations']==pf.loc[i,'closest_weather_station1']], ignore_index=True)
            df1=df1.append(df[df['Weather Stations']==pf.loc[i,'closest_weather_station2']], ignore_index=True)
            df1=df1.append(df[df['Weather Stations']==pf.loc[i,'closest_weather_station3']], ignore_index=True)
        elif((pf.loc[i,'dist1']==0)&(pf.loc[i,'dist2']==0)):
            #print('hi',pf.loc[i,'district'])
            df1=df1.append(df[df['Weather Stations']==pf.loc[i,'closest_weather_station1']], ignore_index=True)
            df1=df1.append(df[df['Weather Stations']==pf.loc[i,'closest_weather_station2']], ignore_index=True)
        else:
            #print('yo')
            if(df[df['Weather Stations']==pf.loc[i,'closest_weather_station1']].empty):
                df1=df1.append(df[df['Weather Stations']==pf.loc[i,'closest_weather_station2']], ignore_index=True)
            else:      
                df1=df1.append(df[df['Weather Stations']==pf.loc[i,'closest_weather_station1']], ignore_index=True)
        df1a=pd.DataFrame()
        df1a=df1a.append(df1[['Maximum Temp(Celsius)',
           'Maximum Temp Departure from Normal(Celsius)', 'Minimum Temp(Celsius)',
           'Minimum Temp Departure from Normal(Celsius)', '24 Hours Rainfall (mm)',
           'Relative Humidity at 0830 hrs (%)',
           'Relative Humidity at 1730 hrs (%)', 'Todays Sunset (IST)',
           'Tommorows Sunrise (IST)', 'Moonset (IST)', 'Moonrise (IST)']].mean(axis=0),ignore_index=True)
        df1a['State']=pf.loc[i,'state']
        df1a['District']=pf.loc[i,'district']
        df1a['Date']=df1.loc[0,'Date']

        df3=df3.append(df1a,ignore_index=True)
    print(223,datetime.datetime.now())
    df3=df3[['Date','State','District','Maximum Temp(Celsius)',
       'Maximum Temp Departure from Normal(Celsius)', 'Minimum Temp(Celsius)',
       'Minimum Temp Departure from Normal(Celsius)', '24 Hours Rainfall (mm)',
       'Relative Humidity at 0830 hrs (%)',
       'Relative Humidity at 1730 hrs (%)', 'Todays Sunset (IST)',
       'Tommorows Sunrise (IST)', 'Moonset (IST)', 'Moonrise (IST)']]
    df3.to_csv(filename)       
    return df3

def daily_data_all(district="None",filter1="None"):#or particular date data
    query = 'select * from IMD_weather1  Where Date <> "None" AND `Date`= (select max(`Date`) as maxdate from IMD_Weather_Prediction_Data1 WHERE Date <> "None");'
    df = pd.read_sql_query(query,con=engine)
    #df = df.replace('\n','', regex=True)    
    print(21,datetime.datetime.now())
    df=station_district_mapping(df)
    print(22,datetime.datetime.now())
    #filter1='Maximum Temp(Celsius)'
    #district='Mahendragarh'
    data=[]
    #print('yo')
    if(district=="None"): #gives all districts
        for i in range(0,df.shape[0]): #667 iterations
            inst={}
            if(filter1=='None'):
                inst['date']=df.iloc[i,0]
                inst['state']=df.iloc[i,1]
                inst['district']=df.iloc[i,2]
                inst['maxtemp']=df.iloc[i,3]
                inst['maxtemp_diff']=df.iloc[i,4]
                inst['mintemp']=df.iloc[i,5]
                inst['mintemp_diff']=df.iloc[i,6]
                inst['rainfall']=df.iloc[i,7]
                inst['rh_0830']=df.iloc[i,8]
                inst['rh_1730']=df.iloc[i,9]
                inst['todays_sunset']=str(df.iloc[i,10])[7:]
                inst['tommorows_sunrise']=str(df.iloc[i,11])[7:]
                inst['moonset']=str(df.iloc[i,12])[7:]
                inst['moonrise']=str(df.iloc[i,13])[7:]
                data.append(inst)
            else:
                feature=df.columns[df.columns.str.startswith(filter1)]
                inst['date']=df.iloc[i,0]
                inst['state']=df.iloc[i,1]
                inst['district']=df.iloc[i,2]
                inst[feature[0]]=df.loc[i,feature[0]]
                data.append(inst)
    else:
        #print('yo1')
        i=df[df['District']==district].index.values[0]
        inst={}
        if(filter1=='None'):
            inst['date']=df.iloc[i,0]
            inst['state']=df.iloc[i,1]
            inst['district']=df.iloc[i,2]
            inst['maxtemp']=df.iloc[i,3]
            inst['maxtemp_diff']=df.iloc[i,4]
            inst['mintemp']=df.iloc[i,5]
            inst['mintemp_diff']=df.iloc[i,6]
            inst['rainfall']=df.iloc[i,7]
            inst['rh_0830']=df.iloc[i,8]
            inst['rh_1730']=df.iloc[i,9]
            inst['todays_sunset']=str(df.iloc[i,10])[7:]
            inst['tommorows_sunrise']=str(df.iloc[i,11])[7:]
            inst['moonset']=str(df.iloc[i,12])[7:]
            inst['moonrise']=str(df.iloc[i,13])[7:]
            data.append(inst)
        else:
            feature=df.columns[df.columns.str.startswith(filter1)]
            inst['date']=df.iloc[i,0]
            inst['state']=df.iloc[i,1]
            inst['district']=df.iloc[i,2]
            inst[feature[0]]=df.loc[i,feature[0]]
            data.append(inst)
    print(23,datetime.datetime.now())            
    return data

def station_district_mapping2(df):
    filename = datetime.date.today().strftime('%m-%d-%Y')+'_1.csv'
    import os.path
    # cache this in redis thats all instead of file
    if(os.path.isfile(filename)):
        df3 = pd.read_csv(filename)
        return df3

    pf=pd.read_csv('/home/vijai_farmguide/Desktop/my_codes/weather1/district_mapped_weather_station123_prcp.csv')

    dates=list(df.columns[df.columns.str.startswith('Date')])
    mintemp=list(df.columns[df.columns.str.startswith('Min_Temp_Date')])
    maxtemp=list(df.columns[df.columns.str.startswith('Max_Temp_Date')])
    weather=list(df.columns[df.columns.str.startswith('Weather_Date')])

    df[mintemp]=df[mintemp].apply(pd.to_numeric,errors='coerce')
    df[maxtemp]=df[maxtemp].apply(pd.to_numeric,errors='coerce')

    df3=pd.DataFrame()
    for i in range(0,len(pf)):
        #print('hi',pf.loc[i,'district'])
        df1=pd.DataFrame()
        if((pf.loc[i,'dist1']==0)&(pf.loc[i,'dist2']==0)&(pf.loc[i,'dist3']==0)):
            #print('hiiiiiii',pf.loc[i,'district'])
            df1=df1.append(df[df['Weather Stations']==pf.loc[i,'closest_weather_station1']], ignore_index=True)
            df1=df1.append(df[df['Weather Stations']==pf.loc[i,'closest_weather_station2']], ignore_index=True)
            df1=df1.append(df[df['Weather Stations']==pf.loc[i,'closest_weather_station3']], ignore_index=True)
        elif((pf.loc[i,'dist1']==0)&(pf.loc[i,'dist2']==0)):
            #print('hi',pf.loc[i,'district'])
            df1=df1.append(df[df['Weather Stations']==pf.loc[i,'closest_weather_station1']], ignore_index=True)
            df1=df1.append(df[df['Weather Stations']==pf.loc[i,'closest_weather_station2']], ignore_index=True)
        else:
            #print('yo')
            if(df[df['Weather Stations']==pf.loc[i,'closest_weather_station1']].empty):
                df1=df1.append(df[df['Weather Stations']==pf.loc[i,'closest_weather_station2']], ignore_index=True)
            else:      
                df1=df1.append(df[df['Weather Stations']==pf.loc[i,'closest_weather_station1']], ignore_index=True)

        df1a=pd.DataFrame()
        df1a=df1a.append(df1[mintemp+maxtemp].mean(axis=0),ignore_index=True)
        df1a['State']=pf.loc[i,'state']
        df1a['District']=pf.loc[i,'district']
        df1a[dates]=df1[dates]     #check again  
        df1a[weather]=df1[weather]

        df3=df3.append(df1a,ignore_index=True)

        #break
    df3=df3[['Date', 'State', 'District', 'Date1', 'Min_Temp_Date1',
           'Max_Temp_Date1', 'Weather_Date1', 'Date2', 'Min_Temp_Date2',
           'Max_Temp_Date2', 'Weather_Date2', 'Date3', 'Min_Temp_Date3',
           'Max_Temp_Date3', 'Weather_Date3', 'Date4', 'Min_Temp_Date4',
           'Max_Temp_Date4', 'Weather_Date4', 'Date5', 'Min_Temp_Date5',
           'Max_Temp_Date5', 'Weather_Date5', 'Date6', 'Min_Temp_Date6',
           'Max_Temp_Date6', 'Weather_Date6', 'Date7', 'Min_Temp_Date7',
           'Max_Temp_Date7', 'Weather_Date7']]
    df3.to_csv(filename)
    #print('hi123')
    return df3    

def next_7_days_data1(district='None'):
    query ='select * from IMD_Weather_Prediction_Data1 WHERE Date <> "None" AND `Date`= (select max(`Date`) as maxdate from IMD_Weather_Prediction_Data1 WHERE Date <> "None");'
    df = pd.read_sql_query(query,con=engine) #1.97 s
    ##print(df.sample())
    ##df = df.replace('\n','', regex=True)
    #df =df.astype(str).replace('\n','')

    dates=list(df.columns[df.columns.str.startswith('Date')])
    mintemp=list(df.columns[df.columns.str.startswith('Min_Temp_Date')])
    maxtemp=list(df.columns[df.columns.str.startswith('Max_Temp_Date')])
    weather=list(df.columns[df.columns.str.startswith('Weather_Date')])
    df=station_district_mapping2(df) #7.11 s
    #district='Nalbari'
    #district="None"
    if(district!="None"):
        data=[]
        df1=df[df['District']==district]
        #print(df1.sample())
        df1.reset_index(inplace=True,drop=True)
        #print(df1.head())
        for i in range(0,7):
            inst={}
            inst['date']=df1.loc[0,dates[i]]
            inst['state']=df1.iloc[0,1]
            inst['district']=df1.iloc[0,2]
            inst['mintemp']=df1.loc[0,mintemp[i]]
            inst['maxtemp']=df1.loc[0,maxtemp[i]]
            inst['weather_info']=df1.loc[0,weather[i]]
            data.append(inst)
        #print(data)            
        return data
    else:
        alldata=[]
        for j in range(0,df.shape[0]):
            data=[]
            df1=df.iloc[j,:]
            #df1.reset_index(inplace=True,drop=True)
            for i in range(0,7):
                inst={}
                inst['date']=df1.loc[dates[i]]
                inst['state']=df1.loc['State']
                inst['district']=df1.loc['District']
                inst['mintemp']=df1.loc[mintemp[i]]
                inst['maxtemp']=df1.loc[maxtemp[i]]
                inst['weather_info']=df1.loc[weather[i]]
                data.append(inst)
            alldata.append(data)
        return alldata




all_filters=['Maximum Temp(Celsius)',
       'Maximum Temp Departure from Normal(Celsius)', 'Minimum Temp(Celsius)',
       'Minimum Temp Departure from Normal(Celsius)', '24 Hours Rainfall (mm)',
       'Relative Humidity at 0830 hrs (%)',
       'Relative Humidity at 1730 hrs (%)', 'Todays Sunset (IST)',
       'Tommorows Sunrise (IST)', 'Moonset (IST)', 'Moonrise (IST)']

all_filters2=['State', 'Weather Stations', 'Average Minimum Temp(Celsius)',
       'Average Maximum Temp(Celsius)', 'Cumalative Rainfall',
       'Average difference from Normal Minimum temperature(4 months)',
       'Average difference from Normal Maximum temperature(4 months)', 'Month',
       'Date', 'Year']

engine1 = create_engine('mysql+mysqldb://farmguideIP:ImageProcessing!@imageprocessing.cp7riswp4tg3.us-east-1.rds.amazonaws.com/image_processing')#, encoding='utf-8')
engine=engine1.connect()    
# In[344]:
def weather_data(district,filter1):
    #set of all the functions
    print(1,datetime.datetime.now())
    #engine=engine1.connect()
    print(2,datetime.datetime.now())
    print(district,filter1)
    dailydata=daily_data_all(district,filter1)
    print(3,datetime.datetime.now())
    #print('hola1',dailydata[0])
    #print(len(dailydata))
    next7=next_7_days_data1(district)
    print(4,datetime.datetime.now())
    #print('hola1',next7[0])
    #print(len(next7))
    all1=[dailydata,next7]
    #print(all1)
    print(5,datetime.datetime.now())

    return all1
    


# In[345]:


#main_func()


# In[346]:


def test(request):
   return HttpResponse('server is running')

def index(request):
    #return HttpResponse('hello is running')
    dataout={}
    statusVal = "False"
    errorVal = "None"
    print('hi_1')
    type=str(request.GET.get('type')) #census or weather

    try:
        district =str(request.GET.get('district'))
        filter1 = str(request.GET.get('filter1'))
        #month1=str(request.GET.get('month1'))

    except Exception as e:
        print("Some argument missing: "+str(e))
        statusVal = "False"
        errorVal = str(e)
        response = {
            "status": statusVal,
            "data": dataout,
            "error": errorVal
        }
        return JsonResponse(response)
    #print('hi_2')


    try:
        if(type=='census'):
            print('later')
        else:
            print('ha ha')
            alldata=weather_data(district,filter1)
            dataout =alldata
            statusVal = "True"
            errorVal = "None"
    except Exception as e:
        print("Error during code execution: "+str(e))
        statusVal = "False"
        errorVal = str(e)
        response = {
            "status": statusVal,
            "data": dataout,
            "error": errorVal
        }
        return JsonResponse(response)
    #print('hi_4')
    response = {
        "status": statusVal,
        "data": dataout,
        "error": errorVal
    }

    return JsonResponse(response)


