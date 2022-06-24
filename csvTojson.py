############ Created by Kalyan Yatham #########
import csv
import json

def csvtojson(csv_file,json_file,primaryKey):
    json_dict = {}
    
    with open(csv_file,'r') as csvfile:
        read_csv = csv.DictReader(csvfile)
        for r in read_csv:
            pk = r[primaryKey]
            json_dict[pk] = r
        
            with open(json_file,'w') as jsonfile:
                jsonfile.write(json.dumps(json_dict, indent=4))


csv_file=input("Enter csv filename: ")
json_file = input("Enter json filename: ")
primaryKey = input()
         
csvtojson(csv_file,json_file,primaryKey)
