#csvwriting.py #import module
import csv 
import math 

csvfile = open('csvexample.csv', 'w', newline='') #create file

csvwriter = csv.writer(csvfile, delimiter = ',') #create csvwriter

csvwriter.writerow(['a','b','hypotenuse']) #write information
for a in range(1, 101):
    for b in range(1,101):
        hypotenuse = math.sqrt(a ** 2 + b ** 2)
        csvwriter.writerow([a,b,hypotenuse])

file.close() #close file