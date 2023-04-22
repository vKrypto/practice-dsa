from datetime import datetime
import pandas as pd
import jovian

# Read in the invoice data as a dataframe
df = pd.read_csv("invoice.csv")

# Loop through each row of the dataframe
for i in range(len(df) - 1):
    try:
        current_invoice = df.iloc[i]
        next_invoice = df.iloc[i + 1]
        current_date = datetime.strptime(current_invoice["talley_invoice_date"], "%d-%b-%Y")
        next_date = datetime.strptime(next_invoice["talley_invoice_date"], "%d-%b-%Y")
        
        # Check if the invoice numbers and dates are in order
        if current_invoice["invoice_number"] > next_invoice["invoice_number"] or \
         current_date >= next_date:
            # Remove the row from the dataframe
            df = df.drop(i)
    except Exception as e:
        print(str(e))

# Output the filtered dataset
df.to_csv("filtered_invoice_data.csv", index=False)
