from datetime import datetime
import pandas as pd
import json
from pprint import pprint

# Read in the invoice data as a dataframe
df = pd.read_csv("invoice.csv")

map_invoices = {}
last_invoice_number = 0
last_invoice_date = None
mapping_disorder = []
d_pattern =  "%d-%b-%Y"

# Loop through each row of the dataframe
for i in range(len(df) - 1):
    current_row = df.iloc[i]
    next_row = df.iloc[i+1]

    current_date = datetime.strptime(current_row["talley_invoice_date"], d_pattern)
    next_date = datetime.strptime(next_row["talley_invoice_date"], d_pattern)
    
    label = current_date.strftime("01-%m-%y")
    current_invoice_number = int(current_row["invoice_number"])
    if map_invoices.get(label) is None:
        map_invoices[label] = []
    map_invoices[label].append(current_invoice_number)

    # if next invoice date is greator than current drop it, and not it.
    if next_date > current_date:
        mapping_disorder.append([int(current_row["invoice_number"]), next_date.strftime(d_pattern)])
        df.drop(i+1)


# Output the filtered dataset
df.to_csv("filtered_invoice_data.csv", index=False)

# dump group mapping
with open('data.json', 'w', encoding='utf-8') as f:
    json.dump(map_invoices, f, ensure_ascii=False, indent=4)


# dump map_invoices.
with open("map_invoices.log", 'w',encoding='utf-8') as f:
    f.write(",".join(["invoice_month", "from", "to", "total", "missing", "missing_invoices"]) + "\n")
    for date_label, obj in map_invoices.items():
        min_in = min(obj)
        max_in = max(obj)
        # assume all missing
        missing_invoices = {i: True for i in range(min_in, max_in+1)}
        # loop and mark as not missing..
        for i in obj:
            missing_invoices[i] = None
        missing_invoices_list = [str(i) for i, value in missing_invoices.items() if value is True]

        line_data = [
            date_label, str(min_in), str(max_in), str(len(obj)), 
            str(len(missing_invoices_list)), 
            " ".join(missing_invoices_list)
        ]
        f.write(",".join(line_data) + "\n")

# dump mapping_disorder.
with open("mapping_disorder.log", 'w',encoding='utf-8') as f:
    f.write("invoice_number,invoice_date \n")
    for value in mapping_disorder:
        f.write(",".join([str(i) for i in value]) + "\n")