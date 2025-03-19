import pandas as pd
import matplotlib.pyplot as plt

import json

data = []
with open("./lte_am_pdu_data_demo2.json") as fp:
    data = json.load(fp)

df = pd.DataFrame(data)

# Convert timestamp to datetime for easy plotting and grouping
df["timestamp"] = pd.to_datetime(df["timestamp"])

# Resample data over 10-second intervals and sum traffic size for UL and DL
traffic_summary = (
    df.groupby(["UL/DL"])
    .resample("10S", on="timestamp")
    .sum(numeric_only=True)
    .reset_index()
)

# Plot uplink and downlink traffic over time
plt.figure(figsize=(12, 6))
for ul_dl in traffic_summary["UL/DL"].unique():
    subset = traffic_summary[traffic_summary["UL/DL"] == ul_dl]
    plt.plot(subset["timestamp"], subset["size"], marker="o", label=f"{ul_dl} Traffic")

# Formatting the plot
plt.title("Uplink vs Downlink Traffic Over Time")
plt.xlabel("Time")
plt.ylabel("Traffic Size (bits)")
plt.legend()
plt.grid(True)

# Show plot
plt.show()
