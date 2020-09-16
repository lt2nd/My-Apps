#  This is the Weather App, not the prettiest but working
#  I know there are similar but this is just an example
#  You need your API key to get this working
# There are several websites for this app but weather one seemed like easiest for me

import tkinter as tk
import requests

root = tk.Tk()
root.title('WeatherApp')

HEIGHT = 600
WIDTH = 800


# def for response ( getting data we want like city name,... ) with try - except in case something went wrong
def formated_response(w):
    try:
        name = w['name']
        wdescription = w['weather'][0]['description']
        temp = w['main']['temp']
        wind = w['wind']['speed']

        final_result = str(name) + '\n' + str(wdescription) \
                       + '\n' + 'Temp = ' + str(temp) + '\n' + 'Wind Speed = ' + str(wind)
    except:
        final_result = ' Problem !!!'
    return final_result


#  def for getting data from url ( metric for celsius )
def get_w(city):
    w_key = 'YOUR API KEY'
    url = 'https://api.openweathermap.org/data/2.5/weather'
    para = {'APPID': w_key, 'q': city, 'units': 'metric'}
    response = requests.get(url, params=para)
    w = response.json()

    label['text'] = formated_response(w)


#  down here are both frames, canvas, label, entry and button
canvas = tk.Canvas(root, height=HEIGHT, width=WIDTH, bg='#49A')
canvas.pack()

frame = tk.Frame(root, bg='#F3FF33', bd=3)
frame.place(relx=0.5, rely=0.1, relwidth=0.75, relheight=0.2, anchor='n')

lowerFrame = tk.Frame(root, bg='#F3FF33', bd=3)
lowerFrame.place(relx=0.5, rely=0.25, relwidth=0.75, relheight=0.6, anchor='n')

label = tk.Label(lowerFrame, font=80)
label.place(relwidth=1, relheight=1)

entry = tk.Entry(frame, font=40)
entry.place(relwidth=1, relheight=0.4)

button = tk.Button(frame, bg='#49A', text="GET", font=40, command=lambda: get_w(entry.get()))
button.place(rely=0.4, relheight=0.3, relwidth=1)

root.mainloop()
