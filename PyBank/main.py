import csv
import os

csvpath = os.path.join('C:/Users/rajka/Desktop/UofT/Assignments/Instructions/PyBank/Resources/budget_data.csv')

with open (csvpath,'r',newline='') as cvsfile:
    csvreader = csv.reader(cvsfile,delimiter=',')

    csvheader = next(csvreader)
    
    listcsv = list(csvreader)

    totalprofit = []
    averagechange = 0.00
    net_sum = 0

    total_months = len(listcsv)

    for row in listcsv:
        net_sum = net_sum + int(row[1])

    for i in range(len(listcsv)-1):
        curline = int(listcsv[i][1])
        nextline= int(listcsv[i+1][1])
        totalprofit.append(nextline -curline)
    
    averagechange = round(sum(totalprofit)/len(totalprofit),2)


print("Fianancial Analysis")
print("------------------------------")
print(f"Total Months: {total_months}")
print(f"Total: ${net_sum}")
print(f"Average Change: ${averagechange}")
print(f"Greatest Increase in Profits: {max(listcsv, key = lambda x: float(x[1]))[0]} (${max(totalprofit)})")
print(f"Greatest Decrease in Profits: {min(listcsv, key = lambda x: float(x[1]))[0]} (${min(totalprofit)})")

output_file = os.path.join('C:/Users/rajka/Desktop/UofT/Assignments/Instructions/PyBank/Output/Financial Analysis.txt')

with open(output_file,'w') as report:
    report.write("Fianancial Report\n")
    report.write("-----------------------------\n")
    report.write(str(f"Total Months: {total_months}\n"))
    report.write(str(f"Total: ${net_sum}\n"))
    report.write(str(f"Average Change: ${averagechange}\n"))
    report.write(str(f"Greatest Increase in Profits: {max(listcsv, key = lambda x: float(x[1]))[0]} (${max(totalprofit)})\n"))
    report.write(str(f"Greatest Decrease in Profits: {min(listcsv, key = lambda x: float(x[1]))[0]} (${min(totalprofit)})\n"))