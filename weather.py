import pandas as pd
import matplotlib.pyplot as plt

data = {
    "Date": [
        "2026-10-01", "2026-10-02", "2026-10-03",
        "2026-10-04", "2026-10-05", "2026-10-06",
        "2026-10-07", "2026-10-08", "2026-10-09",
        "2026-10-10"
    ],
    "City": [
        "Islamabad", "Lahore", "Karachi", "Islamabad",
        "Lahore", "Karachi", "Islamabad", "Lahore",
        "Karachi", "Islamabad"
    ],
    "Temperature": [28, 32, 34, 27, None, 33, 29, 31, 35, 28],
    "Humidity": [60, 55, 70, None, 65, 72, 58, 62, 68, 61],
    "Condition": [
        "Sunny", "Cloudy", "Sunny", "Rainy", "Cloudy",
        "Sunny", "Rainy", "Cloudy", "Sunny", "Rainy"
    ]
}

df = pd.DataFrame(data)
df["Date"] = pd.to_datetime(df["Date"])
df["Temperature"] = df["Temperature"].fillna(df["Temperature"].mean())
df["Humidity"] = df["Humidity"].fillna(df["Humidity"].mean())
df["Condition"] = df["Condition"].str.strip().str.title()

print("Cleaned Weather Data:")
print(df)

daily_temp = df.groupby("Date")["Temperature"].mean()
city_temp = df.groupby("City")["Temperature"].mean()
condition_count = df["Condition"].value_counts()

fig, axes = plt.subplots(1, 3, figsize=(15, 5))

axes[0].plot(daily_temp.index, daily_temp.values, marker="o")
axes[0].set_title("Daily Temperature")
axes[0].set_xlabel("Date")
axes[0].set_ylabel("Temperature (°C)")
axes[0].tick_params(axis="x", rotation=45)

axes[1].bar(city_temp.index, city_temp.values)
axes[1].set_title("Average Temperature by City")
axes[1].set_xlabel("City")
axes[1].set_ylabel("Temperature (°C)")

axes[2].pie(
    condition_count.values,
    labels=condition_count.index,
    autopct="%1.1f%%",
    startangle=90
)
axes[2].set_title("Weather Conditions")

plt.tight_layout()
plt.savefig("weather_dashboard.png")
plt.show()

print("Saved weather_dashboard.png")
