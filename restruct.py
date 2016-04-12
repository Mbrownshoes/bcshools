# loads data from O3_hourly.csv and create daily average max and min values for
# each day and all stations. Saves as json file.


import csv
import json
from datetime import datetime

with open('build/O3_hourly.csv', 'rb') as f:
    reader = csv.reader(f)
    fields = reader.next()

    subset = {} # put data in a dict
    # StaName = ""
    for row in reader:
        for i, val in enumerate(row):
            if i == 0:
                i = 1
            if i == 1:
                StaName = val
                continue

            if StaName not in subset:
                subset[StaName] = {}

            column_name = fields[i]

            #set up dictionary keys
            if column_name not in subset[StaName]:
                subset[StaName][column_name] = []

            #store all the data
            subset[StaName][column_name].append(val)

    # new dict to store mean, min and max values
    newDict = {}

    for sta_name, sta_data in sorted(subset.iteritems()):
        if sta_name not in newDict:
            print(sta_name)
            newDict[sta_name] = {}
            for col_name, col_vals in sta_data.iteritems():

                d = [] #unique dates list

                if col_name == 'date_time':
                    alldates = [0]
                    dayMeas=[0]
                    count = 0 # find number of measurements each day
                    for j, tm in enumerate(col_vals):
                        if datetime.strptime(tm, "%Y-%m-%d %H:%M:%S").date() > datetime.strptime('2005-01-1',"%Y-%m-%d").date():
                        # find unique dates for each station
                            if str(datetime.strptime(tm, "%Y-%m-%d %H:%M:%S").date()) not in d:
                                d.append(str(datetime.strptime(tm, "%Y-%m-%d %H:%M:%S").date()))

                                count = 0 # restart at 0 with each new day
                            else:
                                count += 1

                                if (count - alldates[-1]) != 1:
                                    dayMeas.append((alldates[-1]+1))
                                else:
                                    dayMeas[-1] = count+1

                                alldates.append(count)

                        # add unique dates list
                    newDict[sta_name][col_name] =d
                    # newDict[sta_name]['count'] =dayMeas
                # v = []
                elif col_name == "value":
                    build = 0
                    avg=[]
                    mx=[]
                    mn=[]
                    # for ind, v in enumerate(newDict[sta_name]['count']):
                    for ind, v in enumerate(dayMeas):
                        # print(v)
                        m = col_vals[build:v+build]

                        m = [-999 if x == 'NA' else x for x in m]
                        numlist = [float(x) for x in m]
                        # print('num list: ' + str(numlist))

                        # save avg, max and min vals to dict
                        try:
                            avg.append(round(sum(numlist)/len(numlist),2))
                            mn.append(min(numlist))
                            mx.append(max(numlist))
                        except:
                            print(m)
                            print(build)
                            # print(col_vals)
                            print(v)
                            break

                        build+=v
                    newDict[sta_name]['O3_Avg'] = avg
                    newDict[sta_name]['O3_Max'] = mx
                    # newDict[sta_name]['O3_Min'] = mn
    # print(newDict)

    json.dump(newDict, open('subset.json', 'wb'))
