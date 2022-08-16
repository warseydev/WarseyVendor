import json
import glob
from datetime import datetime
import csv, os
import pandas as pd

src = "appdata/invitecodes/"

def hideit(text):
    halftext = len(text)//2
    text = text[:halftext]
    for i in range(halftext):
        text += "*"
    return text

def updatedata():
    files = glob.glob('appdata/invitecodes/*', recursive=True)
    date = datetime.now()
    data = []
    for single_file in files:
        with open(single_file, 'r') as f:
            try:
                json_file = json.load(f)    
                data.append([
                    json_file['vendor'],
                    json_file['firstname'],
                    json_file['lastname'],
                    hideit(json_file['email']),
                    hideit(json_file['phonenumber']),
                    json_file['model'],
                    json_file['size'],
                    json_file['moreinfo'],
                    json_file['date']
                ])
            except KeyError:
                print(f'DataHandler - Skipping {single_file}')
    data.sort()
    data.insert(0, ['Vendor', 'First Name', 'Last Name', 'Email', 'Phone Number', 'Model', 'Size', 'More Info', 'Date'])
    csv_filename = f'/tmp/{str(date)}.csv'
    with open(csv_filename, "w", newline="") as f:
        writer = csv.writer(f)
        writer.writerows(data)
    a = pd.read_csv(csv_filename)
    a.to_html("templates/data.html", border=0)
    os.remove(csv_filename)