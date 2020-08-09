#477fc473485374029f0aaad184556560
#477fc473485374029f0aaad184556560
#https://api.openweathermap.org/data/2.5/weather?q={city name}&appid={your api key}
from tkinter import *
import requests
from tkinter import messagebox
from PIL import ImageTk,Image

global img, my_img, img_lbl

#q=London&units=metric
url = 'https://api.openweathermap.org/data/2.5/weather?q={}&units=metric&appid=477fc473485374029f0aaad184556560'

def get_weather(city):
	result = requests.get(url.format(city))
	if result:
		json = result.json()
		city = json['name']
		country = json['sys']['country']
		temp = json['main']['temp']
		icon = json['weather'][0]['icon']
		weather = json['weather'][0]['main']
		final = (city, country, temp, icon, weather)
		return final
	else:
		return None


def search():
	
	city = city_text.get()  
	weather = get_weather(city)
	if weather:

		location_label = Label(app, text =weather[0]+', '+weather[1], font = ('bold', 20))
		location_label.pack()

		img = "C:/Python/Weather/"+weather[3] + ".png"
		my_img = ImageTk.PhotoImage(Image.open(img))
		
		img_lbl = Label(image = my_img)
		img_lbl.image = my_img
		img_lbl.pack()

		temp_lbl = Label(app, text= str(weather[2])+"°C")
		temp_lbl.pack()

		weather_lbl = Label(app, text=weather[4])
		weather_lbl.pack()

		
	else:
		messagebox.showerror('Error', 'Cannot find city {}'.format(city))


app = Tk()
app.title("Weather")
app.geometry("700x350")


city_text = StringVar()
city_entry = Entry(app, textvariable = city_text)
city_entry.pack()

search_btn = Button(app, text = "Search Weather", width = 12, command = search)
search_btn.pack()

app.mainloop()