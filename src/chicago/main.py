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

#extract park name, park zip code and park class
for row in csv_parksReport:
    park.append(row[1])
    park_zip.append(row[3])
    park_class.append(row[6])
    
#check for correct data
#print (park)
#print (park_zip)
#print (park_class)
    
#writing school data to file
#with open("school_data.txt", "w") as f:
    #f.writelines(map("{}, {}, {}\n".format, school, school_zip, school_performance))
#f.close()

#write park data to file
#with open("park_data.txt", "w") as f1:
    #f1.writelines(map("{}, {}, {}\n".format, park, park_zip, park_class))
#f1.close()


#wrie new file documenting schools performing far below average and type of park
f1 = open("Far_Below_Average.txt", "w")

#extract schools performing far below average
indices = [i for i, x in enumerate(school_performance) if x == "Far Below Average"]
#print (indices)

#compare schools performign far below average and type of park 
cp = 0
mp = 0
np = 0
ui = 0
for i in indices:
    if school_zip[i] in park_zip:
        j = park_zip.index(school_zip[i])
        #print (school[i], ", ", park[j], ", ", park_class[j])
        if park_class[j] == "COMMUNITY PARK":
            cp += 1 
        elif park_class[j] == "MINI-PARK":
            mp += 1
        elif park_class[j] == "NEIGHBORHOOD PARK":
            np += 1
        elif park_class[j] == "UNIMPROVED":
            ui += 1
        line = school[i], ", ", park[j], ", ", park_class[j], "\n"
        f1.writelines(line)
f1.writelines("\nNumber of Each Type of Park:\n")
count = "Community Parks: ", cp, "Mini-Parks: ", mp, "Neighborhood Parks: ", np, "Unimproved: ", ui
f1.writelines(str(count))
f1.close()
        
        
#wrie new file documenting schools performing above average and type of park
f2 = open("Above_Average.txt", "w")

#extract schools performing above average
indices2 = [i for i, x in enumerate(school_performance) if x == "Far Above Average" or  x == "Above Average"]
#print (indices)

cp2 = 0
mp2 = 0
np2 = 0
ui2 = 0
#compare schools performign above average and type of park 
for i in indices2:
    if school_zip[i] in park_zip:
        j = park_zip.index(school_zip[i])
        if park_class[j] == "COMMUNITY PARK":
            cp2 += 1 
        elif park_class[j] == "MINI-PARK":
            mp2 += 1
        elif park_class[j] == "NEIGHBORHOOD PARK":
            np2 += 1
        elif park_class[j] == "UNIMPROVED":
            ui2 += 1
        line = school[i], ", ", park[j], ", ", park_class[j], "\n"
        f2.writelines(line)
f2.writelines("\nNumber of Each Type of Park:\n")
count = "Community Parks: ", cp, "Mini-Parks: ", mp, "Neighborhood Parks: ", np, "Unimproved: ", ui
f2.writelines(str(count))
f2.close()


        

