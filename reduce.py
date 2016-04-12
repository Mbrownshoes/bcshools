__author__ = 'Gregory'


#read in the file
#create separate district, provincial and school summmaries with smaller fields

#open the file
# fr = open('g2g_files/GrToGrTransition2012_2013.txt','r')
# i = 0
# year = {}
''' for exploration before recoding
for i in range(0,900000):
    redline = fr.readline()
    if i == 0:
        print redline
    newlist = []
    newlist = redline.split("\t")
    if newlist[8] == 'SPECIAL NEEDS NO GIFTED':
        print newlist


    year[newlist[0]] = year.get(newlist[0],0)+1
'''

from pprint import pprint
import json
newlist = []
year = {}
data_level = {}

# group dictionary used to encode provincial file
groups = {'ALL STUDENTS':'ALL',
         'FEMALE':'FEM',
         'MALE':'MAL',
         'ABORIGINAL':'AB',
         'SPECIAL NEEDS NO GIFTED':'SN',
         'ELL':'ELL'}

pprint (groups)

# create a file @ for the province by school
# go through entire file to accumulate all the years then write these to a file
with open('g2g_files/Examinations_2013_2014.txt','r') as fr:
    print "\n Provincial file written with following columns"
    print fr.readline()

    with open('SkulEx2014.csv','w') as fwS:
        fwD = open('DistEx2014.csv','w')
        fwP = open('ProvEx2014.txt','w')
        for row in fr:
            newlist = row.split("\t")

            newlist[2] = newlist[2][2:5]+newlist[2][7:9]#shrink year 2014/2015 > 14/15
            # print(newlist[9])
            newlist[9] = groups[newlist[9]] # assign group codes based on group found in

            year[newlist[2]] = year.get(newlist[2],0)+1 # keep track of number of rows in a year

            data_level[newlist[0]] = data_level.get(newlist[0],0)+1 # keep track of number of rows in a data level

            #if newlist[1] == 'SCHOOL LEVEL' and newlist[11] != 'Msk' and newlist[12].rstrip()!='100' and newlist[8] != 'SN':
            #output  school level records that are not masked
            if newlist[0] == 'SCHOOL LEVEL' and newlist[12] != 'Msk' :
                #year,distschool,grade,group, mark type, avg grade
                printstring = newlist[2]+","+ newlist[6]+","+ newlist[8]+","+newlist[9]+","+newlist[11]+","+newlist[13].rstrip()
                print >> fwS, printstring
            #output  district level records that are not masked
            elif newlist[0] == 'DISTRICT LEVEL' and newlist[12] != 'Msk' :
                #year,dists,grade,group,total in group, total transition, pct transistioning
                print(newlist[7])
                printstring = newlist[2]+","+ newlist[4]+","+ newlist[7]+","+ newlist[8]+","+newlist[9]+","+newlist[11]+","+newlist[13].rstrip()
                print >> fwD, printstring
            # # changed to only output Provincial totals (not for each school type)                
            # elif newlist[0] == 'PROVINCE - Total' and newlist[12] != 'Msk' :
            #     #year,grade,group,total in group, total transition, pct transistioning
            #     printstring = newlist[0]+"| Prov |"+ newlist[7]+"|"+newlist[8]+"|"+newlist[10]+"|"+newlist[11]+"|"+newlist[12].rstrip()
            #     print >> fwP, printstring
        #json.dump(year,fw)

        pprint(year)
        pprint(data_level)






'''

    if newlist[1] == 'SCHOOL LEVEL':
    #substitutions

            print i, newlist
            i++1

'''
'''
    #look for each break?
    if newlist[1] == 'PROVINCE LEVEL': #199 rows
        #print i,newlist
        print ""
    elif newlist[1] == 'DISTRICT LEVEL':   #9217 rows
        #print i, newlist
        print ""
    elif newlist[1] == 'SCHOOL LEVEL':   # rows
        print i, newlist
        print ""
        i++1
'''
