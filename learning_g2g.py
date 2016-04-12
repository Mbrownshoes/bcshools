__author__ = 'Gregory'
limiter = 0
with open('GrToGrTransition2012_2013.txt','r') as fr:
    print "\n Provincial file written with following columns"
    print fr.readline()
    for row in fr:
        newlist = row.split("\t")
        limiter = limiter + 1
        if limiter > 100
