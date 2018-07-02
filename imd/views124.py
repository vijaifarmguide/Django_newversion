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



engine1 = create_engine('mysql+mysqldb://farmguideIP:ImageProcessing!@imageprocessing.cp7riswp4tg3.us-east-1.rds.amazonaws.com/image_processing', encoding='utf-8')
engine=engine1.connect()


def past_7_days_data(station1,filter1='None'):
    query = 'select * from IMD_weather1 WHERE `Weather Stations`="{}" ORDER BY `Date` DESC limit 7'.format(station1)
    df = pd.read_sql_query(query,con=engine)
    #df = df.replace('\n','', regex=True)
    #df =df.astype(str).replace('\n','')
    #print(df.head())
    #features=['Date', 'State', 'Weather Stations',filter1]
    #print(features)
    #data=df[features].set_index('Date').T.to_dict()
    #filter1='Maximum Temp(Celsius)'
    data=[]
    for i in range(0,df.shape[0]):
        inst={}
        if(filter1=='None'):
            inst['Date']=df.iloc[i,1]
            inst['State']=df.iloc[i,2]
            inst['Stations']=df.iloc[i,3]
            inst['Maximum Temp(Celsius)']=df.iloc[i,4]
            inst['Maximum Temp Departure from Normal(Celsius)']=df.iloc[i,5]
            inst['Minimum Temp(Celsius)']=df.iloc[i,6]
            inst['Minimum Temp Departure from Normal(Celsius)']=df.iloc[i,7]
            inst['24 Hours Rainfall (mm)']=df.iloc[i,8]
            inst['Relative Humidity at 0830 hrs (%)']=df.iloc[i,9]
            inst['Relative Humidity at 1730 hrs (%)']=df.iloc[i,10]
            inst['Todays Sunset (IST)']=df.iloc[i,11]
            inst['Tommorows Sunrise (IST)']=df.iloc[i,12]
            inst['Moonset (IST)']=df.iloc[i,13]
            inst['Moonrise (IST)']=df.iloc[i,14]
            data.append(inst)
        else:
            feature=df.columns[df.columns.str.startswith(filter1)]
            inst['Date']=df.iloc[i,1]
            inst['State']=df.iloc[i,2]
            inst['Stations']=df.iloc[i,3]
            inst[feature[0]]=df.loc[i,feature[0]]
            data.append(inst)

    #data    
    return data


# In[336]:


def next_7_days_data(station1):

    print('hi_5')
    query = 'select * from IMD_Weather_Prediction_Data1 WHERE `Weather Stations`="{}"  ORDER BY `Date` DESC limit 1;'.format(station1)
    #print(query)
    df = pd.read_sql_query(query,con=engine)
    #df = df.replace('\n','', regex=True)
    #df =df.astype(str).replace('\n','')
    


    dates=list(df.columns[df.columns.str.startswith('Date')])
    mintemp=list(df.columns[df.columns.str.startswith('Min_Temp_Date')])
    maxtemp=list(df.columns[df.columns.str.startswith('Max_Temp_Date')])
    weather=list(df.columns[df.columns.str.startswith('Weather_Date')])
    data=[]
    print('hi_6')
    for i in range(0,7):
        inst={}
        inst['Date']=df.loc[0,dates[i]]
        inst['Min_Temp_Date']=df.loc[0,mintemp[i]]
        inst['Max_Temp_Date']=df.loc[0,maxtemp[i]]
        inst['Weather_info']=df.loc[0,weather[i]]
        data.append(inst)
    #print(data)

    return data





# In[338]:


#wrong query ,req for all data
def heatmap_7_days_data():
    query = 'SELECT a1.State,a1.`Weather Stations`,AVG(a1.mint) as  `Average Minimum Temp(Celsius)`,AVG(a1.maxt) as  `Average Maximum Temp(Celsius)`,SUM(a1.ppt) as `Cumalative Rainfall`, AVG(a1.dmint) as `Average difference from Normal Minimum temperature(7days)`,AVG(a1.dmaxt) as `Average difference from Normal Maximum temperature(7days)` from (select State,`Weather Stations`,`Date`,`Minimum Temp(Celsius)` as mint,`Maximum Temp(Celsius)` as maxt,`24 Hours Rainfall (mm)` as ppt ,`Minimum Temp Departure from Normal(Celsius)` as dmint,`Maximum Temp Departure from Normal(Celsius)`as dmaxt from IMD_weather1  ORDER BY `Date` DESC limit 7) as a1;'
    df = pd.read_sql_query(query,con=engine)
    #df = df.replace('\n','', regex=True)
    #df =df.astype(str).replace('\n','')
    list1=df.columns
    data=[]
    inst={}
    inst[list1[0]]=df.iloc[0,0]
    inst[list1[1]]=df.iloc[0,1]
    inst[list1[2]]=df.iloc[0,2]
    inst[list1[3]]=df.iloc[0,3]
    inst[list1[4]]=df.iloc[0,4]
    inst[list1[5]]=df.iloc[0,5]
    inst[list1[6]]=df.iloc[0,6]
    data.append(inst)
    #print(data)
    return data

def heatmap_30_days_data():
    query = 'SELECT a1.State,a1.`Weather Stations`,AVG(a1.mint) as  `Average Minimum Temp(Celsius)`,AVG(a1.maxt) as  `Average Maximum Temp(Celsius)`,SUM(a1.ppt) as `Cumalative Rainfall`, AVG(a1.dmint) as `Average difference from Normal Minimum temperature(7days)`,AVG(a1.dmaxt) as `Average difference from Normal Maximum temperature(7days)` from (select State,`Weather Stations`,`Date`,`Minimum Temp(Celsius)` as mint,`Maximum Temp(Celsius)` as maxt,`24 Hours Rainfall (mm)` as ppt ,`Minimum Temp Departure from Normal(Celsius)` as dmint,`Maximum Temp Departure from Normal(Celsius)`as dmaxt from IMD_weather1 WHERE `Weather Stations`="{}" ORDER BY `Date` DESC limit 30) as a1;'.format(station1)
    df = pd.read_sql_query(query,con=engine)
    #df = df.replace('\n','', regex=True)
    #df =df.astype(str).replace('\n','')
    list1=df.columns
    data=[]
    inst={}
    inst[list1[0]]=df.iloc[0,0]
    inst[list1[1]]=df.iloc[0,1]
    inst[list1[2]]=df.iloc[0,2]
    inst[list1[3]]=df.iloc[0,3]
    inst[list1[4]]=df.iloc[0,4]
    inst[list1[5]]=df.iloc[0,5]
    inst[list1[6]]=df.iloc[0,6]
    data.append(inst)
    #print(data)
    return data


# In[339]:


import datetime
month12 = datetime.datetime.now().strftime("%B")


# In[340]:


def par_month_data(station1,month=month12,filter1='None'):
    #query = 'select * from IMD_weather1 WHERE `Weather Stations`="{}" ORDER BY `Date` DESC limit 7'.format(station1)
    query = 'select *,MONTHNAME(DATE(`Date`)) as `Month` from IMD_weather1 WHERE `Weather Stations`="{}" AND Date <> "None" AND MONTHNAME(DATE(`Date`)) ="{}" ORDER BY `Date` DESC '.format(station1,month)
    df = pd.read_sql_query(query,con=engine)
    #df = df.replace('\n','', regex=True)
    #df =df.astype(str).replace('\n','')
    #print(df.head())
    print(query)
    #filter1='none'
    data=[]
    for i in range(0,df.shape[0]):
        inst={}
        if(filter1=='None'):
            inst['Date']=df.iloc[i,1]
            inst['State']=df.iloc[i,2]
            inst['Stations']=df.iloc[i,3]
            inst['Maximum Temp(Celsius)']=df.iloc[i,4]
            inst['Maximum Temp Departure from Normal(Celsius)']=df.iloc[i,5]
            inst['Minimum Temp(Celsius)']=df.iloc[i,6]
            inst['Minimum Temp Departure from Normal(Celsius)']=df.iloc[i,7]
            inst['24 Hours Rainfall (mm)']=df.iloc[i,8]
            inst['Relative Humidity at 0830 hrs (%)']=df.iloc[i,9]
            inst['Relative Humidity at 1730 hrs (%)']=df.iloc[i,10]
            inst['Todays Sunset (IST)']=df.iloc[i,11]
            inst['Tommorows Sunrise (IST)']=df.iloc[i,12]
            inst['Moonset (IST)']=df.iloc[i,13]
            inst['Moonrise (IST)']=df.iloc[i,14]
            data.append(inst)
        else:
            feature=df.columns[df.columns.str.startswith(filter1)]
            inst['Date']=df.iloc[i,1]
            inst['State']=df.iloc[i,2]
            inst['Stations']=df.iloc[i,3]
            inst[feature[0]]=df.loc[i,feature[0]]
            data.append(inst)
    #data 
    #print(data)   
    return data


# In[341]:


#get average value of last  4 months #heatmap
def report_4_months_data(station1,filter2='None'):
    query='select State,`Weather Stations`,AVG(`Minimum Temp(Celsius)`) as  `Average Minimum Temp(Celsius)`,AVG(`Maximum Temp(Celsius)`) as  `Average Maximum Temp(Celsius)`,SUM(`24 Hours Rainfall (mm)`) as `Cumalative Rainfall`,AVG(`Minimum Temp Departure from Normal(Celsius)`) as `Average difference from Normal Minimum temperature(4 months)`,AVG(`Maximum Temp Departure from Normal(Celsius)`) as `Average difference from Normal Maximum temperature(4 months)`,MONTH(DATE(`Date`))as `Month`,`Date` , YEAR(DATE(`Date`)) as `Year` from IMD_weather1 Where Date <> "None" AND `Weather Stations`="{}" GROUP BY `Weather Stations`,`Month` ORDER BY `Date` Desc limit 4 OFFSET 1;'.format(station1)
    #query = 'select * from IMD_Weather_Prediction_Data1 WHERE `Weather Stations`="{}"  ORDER BY `Date` DESC limit 1;'.format(station1)
    df = pd.read_sql_query(query,con=engine)
    #df = df.replace('\n','', regex=True)
    #df =df.astype(str).replace('\n','')
    list1=df.columns
    data=[]

    for i in range(0,4):
        inst={}
        if(filter2=='None'):
            inst[list1[0]]=df.iloc[i,0]
            inst[list1[1]]=df.iloc[i,1]
            inst[list1[2]]=df.iloc[i,2]
            inst[list1[3]]=df.iloc[i,3]
            inst[list1[4]]=df.iloc[i,4]
            inst[list1[5]]=df.iloc[i,5]
            inst[list1[6]]=df.iloc[i,6]
            inst[list1[8]]=df.iloc[i,8]
            data.append(inst)
        else:
            feature=df.columns[df.columns.str.startswith(filter2)]
            inst[list1[0]]=df.iloc[i,0]
            inst[list1[1]]=df.iloc[i,1]
            inst[feature[0]]=df.loc[i,feature[0]]
            inst[list1[8]]=df.iloc[i,8]
            data.append(inst)
        #break
    #print(data)
    return data




# In[343]:


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


# In[344]:


def weather_data(station1,filter1,month1):
    #set of all the functions 

    # if(station1=='None' or filter1=='None'):  #or dynamic=='None' 
    #     print('Argument value missing!')
    #     statusVal = "False"
    #     errorVal = 'String Args missing!'
    #     response = {
    #         "status": statusVal,
    #         "data": dataout,
    #         "error": errorVal
    #     }
    #     return JsonResponse(response)
    print(station1,filter1,month1)
    #station1="Ramagundam"
    #filter1='Relative Humidity at 0830 hrs (%)'
    #filter2='Average Minimum Temp(Celsius)'
    #past7=past_7_days_data(station1,filter1)
    past7_all=past_7_days_data(station1)   
    next7=next_7_days_data(station1)
    #past4m=report_4_months_data(station1,filter2)
    past4m_all=report_4_months_data(station1)
    #parmonth=par_month_data(station1,month1,filter1)
    parmonth_all=par_month_data(station1,month1)
    all1=[past7_all,next7,past4m_all,parmonth_all]
    print(all1)
    return all1
    

    engine.close()
    engine1.dispose()


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
        station1 =str(request.GET.get('station1'))
        filter1 = str(request.GET.get('filter1'))
        month1=str(request.GET.get('month1'))

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
    print('hi_2')
    

    try:
        if(type=='census'):
            print('later')
        else:    
            print('ha ha')        
            alldata=weather_data(station1,filter1,month1)
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
    print('hi_4')
    response = {
        "status": statusVal,
        "data": dataout,
        "error": errorVal
    }

    return JsonResponse(response)









