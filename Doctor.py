# -*- coding: utf-8 -*-
"""
Created on Wed May 04 23:24:20 2016
Doctor Object
@author: aminm
"""

class Doctor:
    
    def __init__(self,f_name, l_name,list_ins):
        
        self.f_name = f_name
        self.l_name = l_name
        self.list_ins = list_ins
        
    def __str__(self):
        ins = ""        
        for i in self.list_ins:
            insurance, plan = i
            ins +=str(insurance)+":"+str(plan)+"\n"
            
        return self.f_name + " " + self.l_name + " accepts: " + ins        
        
    def getF_name(self):
        return self.f_name
        
    def getL_name(self):
        return self.l_name
        
    def getListIns(self):
        return self.list_ins
