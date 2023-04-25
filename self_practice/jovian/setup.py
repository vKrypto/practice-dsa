from datetime import datetime
import pandas as pd
import json
from pprint import pprint

# Read in the invoice data as a dataframe
df = pd.read_csv("invoice.csv")

map_invoices = {}
last_invoice_number = 0
last_invoice_date = None
# Loop through each row of the dataframe
for i in range(len(df) - 1):
    try:
        current_invoice = df.iloc[i]

        current_invoice_number = int(current_invoice["invoice_number"])
        current_date = datetime.strptime(current_invoice["talley_invoice_date"], "%d-%b-%Y")
        label = current_date.strftime("01-%m-%y")
        if map_invoices.get(label) is None:
            map_invoices[label] = []
        map_invoices[label].append(current_invoice_number)



        # if last_invoice_date is None:
        #     last_invoice_date = current_date
        # # Check if the invoice numbers and dates are in order
        # if current_invoice_number > last_invoice_number and current_date >= last_invoice_date:
        #     # Remove the row from the dataframe
        #     last_invoice_number = current_invoice_number
        #     last_invoice_date = current_date
        #     df = df.drop(i)
        # else:
        #     print(current_invoice_number, last_invoice_number, current_date, last_invoice_date)
    except Exception as e:
        print(str(e))
        break

# Output the filtered dataset
df.to_csv("filtered_invoice_data.csv", index=False)

with open('data.json', 'w', encoding='utf-8') as f:
    json.dump(map_invoices, f, ensure_ascii=False, indent=4)



new_map_data = {}
for key, obj in map_invoices.items():
    print(key, min(obj), max(obj))