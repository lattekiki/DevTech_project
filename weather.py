import pandas as pd
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt


content = pd.read_csv("weather_data.csv")
content["Row"] = range(1, len(content) + 1)
content.to_csv('updated_file.txt', index=False)
temperature = content["Temperature"].dropna()
def main():
    print("The Average temperature is", temperature.mean())
    print("The Hottest day is", temperature.max())
    print("The Coldest day is", temperature.min())
    plt.plot(content["Date"], content["Temperature"], marker='o', linestyle='-')
    plt.title("Temperature Over Time")
    plt.xlabel("Date")
    plt.ylabel("Temperature")
    plt.xticks(rotation=45)  # Rotate x-axis labels if needed
    plt.tight_layout()
    plt.savefig("plot.png")

main()