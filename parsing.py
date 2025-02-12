import pandas as pd
import json


# 1. Parsing excel spreadsheet into python object
df = pd.read_excel("Mess Menu Sample.xlsx", skiprows=(0, 12, 22))
dates = df.columns

""" To replace all the "*****" strings with NaN, if this was not done,
    some of strings were not being recognized as NaN"""
df.replace(r"^\*+$", pd.NA, inplace=True, regex=True)
nan_recognizer = df.isna()      # Creates a db of boolean values whether value is NaN or not

parsed_obj = {}                 # Final parsed python object

for date in dates:
    parsed_obj[str(date.date())] = {"BREAKFAST": [], "LUNCH": [], "DINNER": []}

for date in dates:
    for each_row in range(1, 10):
        if not nan_recognizer.at[each_row, date]:   # Verifies whether the value at the place is NaN or not
            parsed_obj[str(date.date())]["BREAKFAST"].append(df.at[each_row, date])

for date in dates:
    for each_row in range(11, 19):
        if not nan_recognizer.at[each_row, date]:
            parsed_obj[str(date.date())]["LUNCH"].append(df.at[each_row, date])

for date in dates:
    for each_row in range(20, 27):
        if not nan_recognizer.at[each_row, date]:
            parsed_obj[str(date.date())]["DINNER"].append(df.at[each_row, date])

# 2. Serializing into a json file


with open("MessMenu.json", "w") as file:
    json.dump(parsed_obj, file, indent=4)