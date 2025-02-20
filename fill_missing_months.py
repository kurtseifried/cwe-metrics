#!/usr/bin/env python3

import csv
import sys
from datetime import datetime, timedelta

def read_csv_data(input_file):
    data = []
    with open(input_file, mode='r') as file:
        reader = csv.reader(file)
        next(reader, None)  # Skip header
        for row in reader:
            year, month, count = row
            data.append((int(year), int(month), int(count)))
    return data

def generate_all_months(start, end):
    current = start
    while current <= end:
        yield current
        current += timedelta(days=32)  # Move to the next month
        current = current.replace(day=1)  # Normalize to the first day of the month

def fill_missing_months(data):
    if not data:
        return []

    # Sort data by year and month
    data.sort(key=lambda x: (x[0], x[1]))
    
    # Generate a complete list of year/month tuples between the first and last dates
    start_date = datetime(data[0][0], data[0][1], 1)
    end_date = datetime(data[-1][0], data[-1][1], 1)
    all_months = {(dt.year, dt.month): 0 for dt in generate_all_months(start_date, end_date)}

    # Update the dictionary with the actual counts from the data
    for year, month, count in data:
        all_months[(year, month)] = count

    # Convert the dictionary back to a sorted list of tuples
    filled_data = sorted([(year, month, count) for (year, month), count in all_months.items()])
    return filled_data

def write_csv_data(output_file, data):
    with open(output_file, mode='w', newline='') as file:
        writer = csv.writer(file)
        writer.writerow(["Year", "Month", "Count"])
        for year, month, count in data:
            writer.writerow([year, month, count])

if __name__ == "__main__":
    if len(sys.argv) != 3:
        print("Usage: python fill_missing_months.py input.csv output.csv")
        sys.exit(1)

    input_csv = sys.argv[1]
    output_csv = sys.argv[2]

    data = read_csv_data(input_csv)
    filled_data = fill_missing_months(data)
    write_csv_data(output_csv, filled_data)

    print(f"Output generated: {output_csv}")
