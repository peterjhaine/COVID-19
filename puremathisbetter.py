import numpy as np
from pathlib import Path
import pandas as pd
import kmapper
from sklearn import datasets
from datetime import date, timedelta, datetime
from sklearn.preprocessing import normalize
import networkx as nx
import IPython
import tkinter

data_folder = Path("csse_covid_19_data/csse_covid_19_time_series/")

pandemic_start = date(2020, 1, 22)

start_date = date(2020, 3, 22)
end_date = date(2020, 3, 25)

delete_location = True
delete_unassigned = True
normalize_data = True
sort_by_location = False

delta = end_date - start_date

day_file = "time_series_covid19_confirmed_US.csv"

file_to_open = data_folder / day_file
columns = ["Lat", "Long_", "Combined_Key"]
dates = []

for day in range(delta.days + 1):
    date = start_date + timedelta(days=day)
    dates.append(date.strftime("%-m/%-d/%y"))

columns = columns + dates

print(columns)

raw_data = pd.read_csv(file_to_open, header=0,
                       delimiter=',', encoding=None, usecols=columns)

# COMBINED_KEY, LAT, LONG, CASES, DAY


derek = []

days_since_start = start_date - pandemic_start

for place in raw_data.itertuples():
   # print(place)
    for i in range(delta.days + 1):
        # yeet = "_" + str(i + 4)

        # yeet = str(i)
        print(type(days_since_start))
        row = [place.Combined_Key, place.Lat,
               place.Long_, place[i + 4], days_since_start.days + i, (start_date + timedelta(days=i)).strftime("%-m/%-d/%y")]

        derek.append(row)

dr_fauci = pd.DataFrame(
    derek, columns=["Combined_Key", "Lat", "Long_", "Cases", "Days since start of pandemic", "Date"])

print(dr_fauci)

# make indices: combined_key, date

temp = dr_fauci.to_numpy()

indices = np.empty(len(temp), dtype=object)

for i in range(len(temp)):
    indices[i] = str(temp[i, 0]) + ", " + str(temp[i, -1])

print(indices)

dr_fauci = dr_fauci.drop(
    columns=["Combined_Key", "Date"])

final_array = dr_fauci.to_numpy()

print(final_array)

data = normalize(final_array, axis=0, norm='l2')

print(data)


# LAT, LONG, CASES, DAY
