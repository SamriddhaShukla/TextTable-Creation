# -*- coding: utf-8 -*-
"""
Created on Thu Nov 21 19:50:35 2019

@author: samri
"""

from zipfile import ZipFile
import os
file_name="names.zip"
from texttable import Texttable
t=Texttable()

file=""


with ZipFile(file_name,'r') as zip:
	zip.printdir()
	print("Extracting all files now....")
	zip.extractall(r"C:\Users\samri\Project")
	print("Done!")


 
filenames=os.listdir(r"C:\Users\samri\Project")
t.header(filenames)
fileName=""
d={}
w=0
for fileName in filenames:
	#print(fileName)
	path_of_file=r"C:\Users\samri\Project\{}".format(fileName)
	x=open(path_of_file,"r")

	d[w]=x.readlines()
	w=w+1
	
	
l=len(d)
number_items_data=[]
for i in d:
	number_items_data+=[len(d[i])]
#print(number_items_data)
max_number_elemnets=max(number_items_data)



for i in range(max_number_elemnets):
	elemets_ki_list=[]
	j=0
	while(10>2):
		#print(i,j)
		#print(d[j][i])
		if(i>=(len(d[j])-1)):
			elemets_ki_list+=["-----"]
		else:
			elemets_ki_list+=[d[j][i]]
		#print(elemets_ki_list)
		if(j==(len(d)-1)):
			break
		j=j+1
	t.add_row(elemets_ki_list)		
print(t.draw())

all_elements_list=[]
for i in range(len(d)):
	all_elements_list+=d[i]
repeated=[]
for i in all_elements_list:
	x=all_elements_list.count(i)
	if(x==len(d)):
		if(i not in repeated):
			repeated.append(i)
#print(repeated)
tt=Texttable()
tt.header(["REPEATED STATES"])
for i in repeated:
	tt.add_row([i])
print(tt.draw())
#print(all_elements_list)