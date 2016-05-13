# -*- coding: utf-8 -*-
"""
Created on Wed May 04 23:19:22 2016
Practice Object
@author: aminm
"""

class Practice:
    def __init__ (self, name,add,number, website = "", list_docs = []):
        self.name = name
        self.website = website
        self.add = add
        self.list_doc = list_docs
        self.number = number
    def __str__(self):
        s = "Name: " + str(self.name) + "\n"   
        s += "Website: " + str(self.website) + "\n"
        add = "Address: " + self.add.getStreet() + ", " + self.add.getCity() + ", " + self.add.getZipCode()        
        s += add + "\n"
        s += "Has " + str(len(self.list_doc)) + " doctors."
        s += "Phone number: " + self.number
        return s         
        
    def getName(self):
        return self.name
        
    def getWebsite(self):
        return self.website
        
    def getAdd(self):
        return self.add
        
    def getListDoc(self):
        return self.list_docs
    
    def getNumber(self):
        return self.getNumber
