import requests

# Function to fetch historical COVID-19 statistics
def fetch_covid_stats():
    url = "https://disease.sh/v3/covid-19/historical/all?lastdays=all"
    response = requests.get(url)
    
    if response.status_code == 200:
        data = response.json()
        return {
            "cases": data["cases"],
            "recoveries": data["recovered"],
            "deaths": data["deaths"]
        }
    else:
        return {"error": "Failed to retrieve data"}

# Function to display COVID-19 statistics
def display_stats(stats):
    if "error" in stats:
        print(stats["error"])
    else:
        print("Historical COVID-19 Statistics:")
        print("Cases:")
        for date, count in stats["cases"].items():
            print(f"{date}: {count}")
        print("\nRecoveries:")
        for date, count in stats["recoveries"].items():
            print(f"{date}: {count}")
        print("\nDeaths:")
        for date, count in stats["deaths"].items():
            print(f"{date}: {count}")

# Main function to interact with the user
def main():
    print("Real-Time COVID-19 Historical Statistics Tracker")
    stats = fetch_covid_stats()
    display_stats(stats)

if __name__ == "__main__":
    main()
