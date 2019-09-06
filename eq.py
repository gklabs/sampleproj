# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""
import numpy as np
import random
eq= ["(","-","C","*","U","C_inv","-","V",")","*","r_fdt","+","(","-","C","*","U","*","Cinv","*","V","+","C","*","L",")","*","r"]
r1=["r","p","s","x","lambda"] #,"rdiff","pdiff","sdiff","xdiff"]
r2= ["L","V","U","C","M"]
r3=["+","-","*"]
r5= ["fd","sd"]
r4= ["inv","tp"]

ddx= ["fd","sd","",""] #for equal probabilities
#Separate code block for generating differential, inv,transpose operators with vars
def genmatxop(ch):
    matxop = ["inv","tp",""] 
    re= ch +"_"+ matxop[random.randint(0,2)]
    return re
     
#
def genddx(ch):
     re= ch + "_"+ ddx[random.randint(0,3)]
     return re 
     
    
def removeunary(ch):
     unary= ["fd","sd","inv","tp"]
     for cc in unary:
         if cc in ch:
             return ch.split("_")[0]
    
     
eq1= eq

ling=random.sample(range(0,len(eq)-1),5)
print(ling)


for i in ling:
    print(eq[i])
    #check for unary operators
    cleanterm= removeunary(eq[i])
    if cleanterm in r1:
        rep1= random.randint(0,len(r1)-1)
        eq1[i]=genddx(r1[rep1])
    
    if cleanterm in r2:
        rep1= random.randint(0,len(r2)-1)
        eq1[i]=genmatxop(r2[rep1])
    
    if cleanterm in r3:
        eq1[i]=r3[random.randint(0,len(r3)-1)]
    
    print(eq1[i])
        
print(eq1)
print(eq)