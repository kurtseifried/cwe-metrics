#!/usr/bin/env python3

import csv
import xml.etree.ElementTree as ET
import sys
from datetime import datetime

def process_xml_to_csv(input_xml, output_csv):
    # Parse the XML file
    tree = ET.parse(input_xml)
    root = tree.getroot()

    # Define the namespace to access the elements
    ns = {'default': 'http://cwe.mitre.org/cwe-7'}

    # Open the CSV file for writing
    with open(output_csv, mode='w', newline='') as file:
        writer = csv.writer(file)
        writer.writerow(["Weakness ID", "Name", "Submission_ReleaseDate", "Last Modification_Date"])

        # Iterate through each Weakness element
        for weakness in root.findall('.//default:Weakness', ns):
            weakness_id = weakness.attrib['ID']
            name = weakness.attrib['Name']
            submission_date = weakness.find('.//default:Submission/default:Submission_ReleaseDate', ns).text
            
            # Find all Modification Dates
            modification_dates = weakness.findall('.//default:Modification/default:Modification_Date', ns)
            dates = [datetime.strptime(mod.text, "%Y-%m-%d") for mod in modification_dates if mod.text]
            
            # Determine the most recent Modification Date
            last_modification_date = "NO DATE"
            if dates:
                last_modification_date = max(dates).strftime("%Y-%m-%d")

            # Write to CSV
            writer.writerow([weakness_id, name, submission_date, last_modification_date])

if __name__ == "__main__":
    input_xml_path = sys.argv[1]
    output_csv_path = sys.argv[2]
    process_xml_to_csv(input_xml_path, output_csv_path)

    
