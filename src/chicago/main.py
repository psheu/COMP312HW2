'''
Created on Jun 12, 2016

@author: Jace Sheu
'''

import csv


#read CPS report
CPSReport = open('Chicago_Public_Schools___High_School_Progress_Report_Card__2012-2013_.csv')
csv_CPSReport = csv.reader(CPSReport)

#extract school name, zip code, and student performance level
school = []
school_zip = []
school_performance = []
for row in csv_CPSReport: 
    school.append(row[2])
    school_zip.append(row[6])
    school_performance.append(row[19])

#check for correct data
#print (school)
#print (school_zip)
#print (school_performance)
    
#read parks report
parksReport = open('Parks_-_Map.csv')
csv_parksReport = csv.reader(parksReport)
park = []
park_zip = []
park_class = []

for row in csv_parksReport:
    park.append(row[1])
    park_zip.append(row[3])
    park_class.append(row[6])
    
#check for correct data
#print (park)
#print (park_zip)
#print (park_class)

    
#writing school data to file
with open("school_data.txt", "w") as f:
    f.writelines(map("{}, {}, {}\n".format, school, school_zip, school_performance))
f.close()

#write park data to file
with open("park_data.txt", "w") as f1:
    f1.writelines(map("{}, {}, {}\n".format, park, park_zip, park_class))
f1.close()
  
