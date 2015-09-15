import csv
import json

dat_out = {}

with open('ProvG2G2012_2013.txt','r') as fwS:
	for row in fwS:
		row.split("|")[3]