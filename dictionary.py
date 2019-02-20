# -*- coding: utf-8 -*-
"""
Created on Wed Feb 20 09:44:07 2019

@author: sharda
"""
#prgram to create a dictionary when keys will be input by user as string and values will be list of vowels present in that string
x=int(input("Enter the size of dictionary: "))
d={}
for i in range(x):
    key=input("Enter the key: ")
    value=[]
    for i in key:
        if i in "aeiouAEIOU":
            value.append(i)
    d.update({key:value})
print("Dictionary is: ", d)