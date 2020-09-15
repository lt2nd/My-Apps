import tkinter as tk
import requests

root = tk.Tk()

HEIGHT = 600
WIDTH = 800


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


def get_w(city):
    w_key = 'YOUR API KEY'
    url = 'https://api.openweathermap.org/data/2.5/weather'
    para = {'APPID': w_key, 'q': city, 'units': 'metric'}
    response = requests.get(url, params=para)
    w = response.json()

    label['text'] = formated_response(w)


canvas = tk.Canvas(root, height=HEIGHT, width=WIDTH)
canvas.pack()

frame = tk.Frame(root, bg='#F3FF33', bd=3)
frame.place(relx=0.5, rely=0.1, relwidth=0.75, relheight=0.2, anchor='n')

lowerFrame = tk.Frame(root, bg='#F3FF33', bd=3)
lowerFrame.place(relx=0.5, rely=0.25, relwidth=0.75, relheight=0.6, anchor='n')

label = tk.Label(lowerFrame, font=80)
label.place(relwidth=1, relheight=1)

entry = tk.Entry(frame, font=40)
entry.place(relwidth=1, relheight=0.4)

button = tk.Button(frame, text="GET", font=40, command=lambda: get_w(entry.get()))
button.place(rely=0.4, relheight=0.3, relwidth=1)

root.mainloop()
