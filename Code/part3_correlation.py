# Importing libraries
import numpy as np
import pandas as pd
from scipy import stats
import plotly.express as px
import matplotlib.pyplot as plt


# Reading CSV files into a DataFrame
data_full = pd.read_csv("../Dataset/updated_data_FULL.csv")

# Moving selected columns to new DataFrame
data_short = data_full[["Alert", "EpochHH", "VehicleID", "Speed", "Lat3F", "Long3F"]]

# Deleting redundant variables
del data_full

data_short = data_short[data_short["Alert"].str.contains("cas_")].reset_index()

# Plotting lat-longs alerts ##################################################
fig_3 = px.scatter(data_short, x="Long3F", y="Lat3F", color="Alert",
                   marginal_x="violin", marginal_y="violin")
fig_3.update_layout(
    autosize=False,
    width=1920,
    height=1920,
    font=dict(
        size=20
    ),
    margin=dict(
        l=0, r=0, b=0, t=0
    ),
    legend=dict(
        yanchor="top",
        y=0.95,
        xanchor="right",
        x=0.875,
        bgcolor="rgba(0,0,0,0)"
    )
)
fig_3.write_image("../Plots/cas_ax_lat_long_alert.png", scale=3)


# Plotting lat-longs vehicles ##################################################
fig_4 = px.scatter(data_short, x="Long3F", y="Lat3F", color="VehicleID")
fig_4.update_layout(
    autosize=False,
    width=1920,
    height=1920,
    font=dict(
        size=20
    ),
    margin=dict(
        l=0, r=0, b=0, t=0
    )
)
fig_4.write_image("../Plots/cas_ax_lat_long_vehicle.png", scale=3)


# Plotting speed vs vehicles ##################################################
fig_5 = px.scatter(data_short, x="Speed", y="VehicleID", color="Alert",
                   marginal_x="violin", marginal_y="violin")
fig_5.update_layout(
    autosize=False,
    width=1920,
    height=1920,
    font=dict(
        size=20
    ),
    margin=dict(
        l=0, r=0, b=0, t=0
    ),
    legend=dict(
        yanchor="top",
        y=0.95,
        xanchor="right",
        x=0.875,
        bgcolor="rgba(0,0,0,0)"
    )
)
fig_5.write_image("../Plots/cas_ax_speed_vehicle_alert.png", scale=3)


# Plotting speed vs datetime ##################################################
fig_6 = px.scatter(data_short, x="Speed", y="EpochHH", color="Alert",
                   marginal_x="violin", marginal_y="violin")
fig_6.update_layout(
    autosize=False,
    width=1920,
    height=1920,
    font=dict(
        size=20
    ),
    margin=dict(
        l=0, r=0, b=0, t=0
    ),
    legend=dict(
        yanchor="top",
        y=0.95,
        xanchor="right",
        x=0.875,
        bgcolor="rgba(0,0,0,0)"
    )
)
fig_6.write_image("../Plots/cas_ax_speed_datetime_alert.png", scale=3)


# Plotting speed vs datetime ##################################################
fig_7 = px.scatter(data_short, x="EpochHH", y="VehicleID", color="Alert",
                   marginal_x="violin", marginal_y="violin")
fig_7.update_layout(
    autosize=False,
    width=1920,
    height=1920,
    font=dict(
        size=20
    ),
    margin=dict(
        l=0, r=0, b=0, t=0
    ),
    legend=dict(
        yanchor="top",
        y=0.95,
        xanchor="right",
        x=0.875,
        bgcolor="rgba(0,0,0,0)"
    )
)
fig_7.write_image("../Plots/cas_ax_datetime_vehicle_alert.png", scale=3)

print("\n!!!TASK COMPLETE!!!")
