# Importing libraries
import pandas as pd
import geohash2
from datetime import datetime

# Reading CSV files into a DataFrame
csv1 = pd.read_csv("../Dataset/iraste_nxt_cas.csv")
csv2 = pd.read_csv("../Dataset/iraste_nxt_casdms.csv")


# Function to calculate geohash for each row
def calculate_geohash(row):
    try:
        lat = row["Lat"]  # Reading "Latitude"
        lon = row["Long"]  # Reading "Longitude"
        geohash = geohash2.encode(lat, lon, precision=8)  # Default precision = 8
        # print(geohash)  # Printing geohash
        return geohash
    except Exception as E:
        return None


# Main function
if __name__ == "__main__":
    # Concatenating CSV DataFrames vertically (row-wise)
    print("\nConcatenating CSV data...")
    data_full = pd.concat([csv1, csv2], ignore_index=True)
    # Printing merged DataFrame
    print(data_full.head())
    print("Row count = {}!!!".format(len(data_full)))

    # Rounding lat-long to 3rd decimal
    print("\nRounding lat-long to 3rd decimal...")
    data_full["Lat3F"] = round(data_full["Lat"], 3)
    data_full["Long3F"] = round(data_full["Long"], 3)
    print(data_full.head())
    print("Lat-Long rounding COMPLETE!!!")

    # Converting vehicle to string
    print("\nConverting vehicle ID to string...")
    data_full["VehicleID"] = data_full["Vehicle"].astype(int)
    print(data_full.head())
    print("Vehicle ID processing COMPLETE!!!")

    # Calculating geohash
    print("\nProcessing geohash...")
    data_full["Geohash8P"] = data_full.apply(calculate_geohash, axis=1)
    # Printing merged DataFrame
    print(data_full.head())
    data_full["Geohash6P"] = data_full["Geohash8P"].str[:-2]
    # Printing merged DataFrame
    print(data_full.head())
    print("Geohash processing COMPLETE!!!")

    # Calculating epoch time
    print("\nConverting datetime to epoch time...")
    datetime = pd.to_datetime(data_full["Date"] + " " + data_full["Time"])
    data_full["EpochHHMMSS"] = datetime.apply(lambda x: int(x.timestamp())).astype(str)
    # Printing merged DataFrame
    print(data_full.head())
    data_full["EpochHH"] = data_full["EpochHHMMSS"].str[:-4]
    # Printing merged DataFrame
    print(data_full.head())
    print("Row count = {}!!!".format(len(data_full)))

    # Deleting redundant variables
    del datetime

    # Saving DataFrame to new CSV file
    data_full.to_csv("../Dataset/updated_data_FULL.csv", index=False)

    print("\n!!!TASK COMPLETE!!!")
