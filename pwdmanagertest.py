import csv
with open("<path>",'w') as csvFile:
    fieldnames = ['site_name', 'user_name', 'user_password']
    fileWriter = csv.DictWriter(csvFile, fieldnames=fieldnames)

    fileWriter.writeheader()
    fileWriter.writerow({'site_name': 'nsu.edu', 'user_name': 'royos', 'user_password': 'itssec'})