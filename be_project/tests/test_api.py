from cmath import nan
from nturl2path import pathname2url
from uuid import NAMESPACE_URL
import requests
import json
import numpy as np
import pandas as pd
from datetime import datetime
baseUrl = "http://127.0.0.1:8080/"

'''def test_farmer_post_api(data):
    path = "api/farmer"
    response = requests.post(url=baseUrl+path,json=data)
    responseJson =response
    print(responseJson)
    assert response.status_code == 200
    
def test_farmer_put_api(data):
    path = "api/farmer"
    response = requests.put(url=baseUrl+path,json=data)
    responseJson  =response
    print(responseJson)
    assert response.status_code == 200
    
def test_farmer_get_api(id):
    path = "api/farmer/"+str(id)
    response = requests.get(url=baseUrl+path)
    responseJson =response
    print(responseJson)
    assert response.status_code == 200

def test_farmer_delete_api(id):
    path = "api/farmer/"+str(id)
    response = requests.delete(url=baseUrl+path)
    responseJson =response
    print(responseJson)
    assert response.status_code == 200'''
    
def test_data_entry_farmer():
    fpath='./tests/test_data/farm_data.xlsx'    
    fpath2='./tests/test_data/past_data.xlsx'
    data=pd.read_excel(fpath)    
    path = "api/farmer"
    path1 = "api/farm"    
    path2 = "api/past_data"
    names=[]
    for row in data.iterrows():
       name=row[1]["Farmer Name"]
       names.append(name)
    names=list(set(names))
    #print(names)
    ids=dict()
    farm_ids=dict()
    for name in names:
        sname=name.split(' ')  
        #print(sname) 
        fname=sname[0]
        mname="" if len(sname)==2 else sname[1] 
        lname=sname[1] if len(sname)==2 else sname[2] 
        #print(fname,mname,lname,sep='--')
        d1={
            'first_name':fname,
            'last_name':lname,
            'middle_name':mname,
            'state':'Maharashtra'
        }  
        response = requests.post(url=baseUrl+path,json=d1)
        res=response.json()
        #print(res["farmer_id"])
        ids[name]=int(res["farmer_id"])
        assert response.status_code==200
    for row in data.iterrows():
        name=row[1]["Farmer Name"]
        id=ids[name]
        #print(name)
        lat,long,ar="","",0.0
        farm=row[1]["FARM #"]
        #print(row[1]["Farm Cordinates"])
        if str(row[1]["Farm Cordinates"]) != "nan":
            d=row[1]["Farm Cordinates"].split(":")[2].lstrip("[").split("]")[0].split(",")
            lat=float(d[0])
            longt=float(d[1])
            #print(name,lat,long,sep="\n\n")
        if  str(row[1]["Area"]) != "nan":
            ar=row[1]["Area"].rstrip(" R")
            ar=float(ar)
        d2={
            'farmer_id':id,
            'latitude':lat,
            'longitude':longt,
            'area':ar,
            'farm_name':farm
        } 
        response = requests.post(url=baseUrl+path1,json=d2)
        res=response.json() 
        farm_ids[farm]=int(res["farm_id"])
        assert response.status_code==200
    data2=pd.read_excel(fpath2)        
    for row in data2.iterrows():
        #print(row[1])
        farm=row[1]['Farm #']
        sos=row[1]['Start of Season (SOS)'].strftime("%d/%m/%Y, %H:%M:%S") 
        #sos = datetime.strptime(sos, "%d/%m/%Y, %H:%M:%S")
        eos=row[1]['End of Season (EOS)'].strftime("%d/%m/%Y, %H:%M:%S")
        #eos = datetime.strptime(eos, "%d/%m/%Y, %H:%M:%S")
        variety=row[1]['Variety']
        variety=variety if str(variety)!="nan" else ""
        crop_type=row[1]['Crop Type']        
        crop_type=crop_type if str(crop_type)!="nan" else ""
        fid=farm_ids[farm]
        crop_yield=str(row[1]['Yield (T/ACR)'])
        print(fid,sos,eos,variety,crop_type,crop_yield,sep='\n')
        print()
        d3={
            'farm_id':fid,
            'start_of_season':sos,
            'end_of_season':eos,
            'crop_type':crop_type,
            'crop_variety':variety,
            'crop_yield':crop_yield
        } 
        response = requests.post(url=baseUrl+path2,json=d3)
        res=response.json() 
        assert response.status_code==200
    return


#test_data_entry_farmer()
