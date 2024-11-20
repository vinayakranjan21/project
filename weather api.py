import tkinter as tk
import requests


def get_weather(city):
    api_key = "your_api_key_here"  # Replace with your API key
    base_url = f"http://api.openweathermap.org/data/2.5/weather?q={city}&appid={api_key}"
    response = requests.get(base_url)
    data = response.json()
    if data["cod"] == 200:
        temp = data["main"]["temp"] - 273.15  # Convert from Kelvin to Celsius
        result_label.config(text=f"Temperature: {temp:.2f}°C")
    else:
        result_label.config(text="City not found")

# Tkinter GUI setup
root = tk.Tk()
root.title("Weather App")

city_entry = tk.Entry(root)
city_entry.pack()

search_btn = tk.Button(root, text="Get Weather", command=lambda: get_weather(city_entry.get()))
search_btn.pack()

result_label = tk.Label(root, text="")
result_label.pack()

root.mainloop()
