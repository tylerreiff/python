import requests, json 

api_key = "8a3f0d1e3c2c87883fde85d074507d3b"
base_url = "http://api.openweathermap.org/data/2.5/weather?"


def extract_data(data):
	try :
		city = data['name']
		print("City: " + city)
		print("Temperature: "  + str(round(data['main']['temp'] - 273.15, 1)) + " Celcius")
		print("Minimum Temperature: " + str(round(data['main']['temp_min'] - 273.15, 1)) + " Celcius")
		print("Maxmum Temperature: " + str(round(data['main']['temp_max'] - 273.15, 1)) + " Celcius")
		print("Feels like: " +  str(round(data['main']['feels_like'] - 273.15, 1)) + " Celcius")

	except:
		print("Data not found.")


def main():

	while True:
		city_data = input("Enter zip code or city name to obtain weather forecast (Type EXIT to exit):")
		if city_data == "EXIT":
			break
		url = base_url + "appid=" + api_key + "&q=" + city_data

		response = requests.get(url) 

		json_data = response.json()
		extract_data(json_data)

main()