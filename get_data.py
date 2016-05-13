# -*- coding: utf-8 -*-
"""
Created on Wed May 04 19:21:48 2016

Python script to get data using Better Doctor API.

@author: aminm
"""

import requests
import json
import pprint as pp
import time
from Doctor import Doctor
from Practice import Practice
from Practice_Address import Practice_Address

USER_KEY = "Your User Key Here"
URL = "https://api.betterdoctor.com/2016-03-01/practices?"

def getData(loc, user_loc, limit = ""):
    """
        Returns a Json object with all the required fields. Alternately, can 
        save the json content in a file.
    """
    start = time.time()
    longi,lati,rnge = loc
    location = "location=" + longi + "%2C" + lati + "%2C" + rnge
    u_long, u_lat = user_loc
    user_location = "&user_location=" + u_long + "%2C" + u_lat
    skip = "&skip=0"
    limit = "&limit=" + limit
    
    #Our required fields. Any change has to be hardcoded.
    fields = "&fields=name%2Cwebsite%2Cinsurance_uids%2Cvisit_address%2Cphones\
    %2C%20doctors(profile%20(first_name%2Clast_name)%2Cinsurances)"
    
    url = URL +location + user_location + fields + skip + limit + USER_KEY

    resp = requests.get(url)
    resp_json = resp.json()

    if resp.status_code == 200:
#==============================================================================
# IF YOU WANT TO WRITE THE DATA TO A FILE.    
#         print "Writing to a file..."
#         with open("json_response.json","w") as f:
#              json.dump(resp_json,f)
#==============================================================================

        end = time.time()
        time_taken = end - start
        print "This execution took" ,time_taken,"seconds."
        return resp_json
    else:
        print resp.status_code


def parseInfo():
    """
        Reads in the master Json object and returns a list of Practice objects.
        Each practice object can parsed with simple getters to get all the 
        individual data. Look at Practice.py for all the fields and methods.
    """    
    
    # Reading from a file for faster debugging. Will change it to take a json obj as a
    # parameter.    
    with open('json_response.json') as data_file:    
        data = json.load(data_file)    
    #data =  json_data
    data = data["data"]
    list_pracs = []
    for item in data:
        website = item["website"]
        name = item["name"]
        add = item["visit_address"]
        address = parseAddress(add)
        doctors = item["doctors"]
        list_docs = parseDoctors(doctors)
        number = item["phones"][0]["number"]
        prac = Practice(name,address, number,website,list_docs)
        list_pracs.append(prac)
        
    return list_pracs
    
def parseDoctors(doctors):
    """
        Takes in a list of doctors in json format and returns a list of 
        Doctor objects which can easily parsed with simple getters. Look at 
        Doctor.py for all the fields and methods.
    """
    list_docs = []
    for doc in doctors:
        ins =[]
        f_name = doc["profile"]["first_name"]
        l_name = doc["profile"]["last_name"]
        try:
            ins = doc["insurances"]
            ins_dec = [(i["insurance_provider"]["name"],i["insurance_plan"]["name"])for i in ins]
        except KeyError:
            ins_dec = []
        doc = Doctor(f_name,l_name,ins_dec)
        list_docs.append(doc)

    return list_docs
def parseAddress(add):
    """
        Takes in an address in json format and returns a Practice
        object which can easily parsed with simple getters. Look at the Practice_Address.py
        for all the fields and methods.
    """
    city = add["city"]
    street = add["street"]
    zip_code = add["zip"]
    return Practice_Address(street, city, zip_code)
def main():
    json_data = getData(("37.773","-122.413","20"),("37.773","-122.413"),"100")
    p = parseInfo()
    for prac in p:
        print prac
        print len(p)
if __name__ == "__main__":
    main()
