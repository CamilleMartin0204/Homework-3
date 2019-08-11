import csv
filename = "C:/Users/camil/PythonChallenge/PyBank/budget_data.csv"
rowcount = 0
total = 0

previousmonth = 0 
currentmonth = 0
diff = 0
maxdiff = 0
mindiff = 0

with open(filename, 'r') as csvfile:
    csvreader = csv.reader(csvfile,delimiter=',')
    for row in csvreader:
        rowcount = rowcount +1
        if rowcount>1:
            previousmonth = currentmonth
            currentmonth = int(row[1])
            diff = currentmonth - previousmonth
            if diff < mindiff:
                mindiff = diff
            if diff > maxdiff:
                maxdiff = diff
            total = total + int(row[1])
            print (row[1])

rowcount = rowcount - 1
average =(total/rowcount)

print("Financial Analysis")
print("----------------------------")
print("total months:", int(rowcount))
print("total profit: $", total)
print("average", average)
print("mindiff", mindiff)
print("maxdiff", maxdiff)

f=open("PyBank/PyChallenge.txt","w+")
f.write("Financial Analysis")
f.write("\n")
f.write("----------------------------")
f.write("\n")
f.write("total months:"+ str(rowcount))
f.write("\n")
f.write("total profit: $"+ str(total))
f.write("\n")
f.write("average"+str(average))
f.write("\n")
f.write("mindiff"+str(mindiff))
f.write("\n")
f.write("maxdiff"+str(maxdiff))