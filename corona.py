from tkinter import *
import tkinter
import requests
import datetime
def getCovidData():
    api = "https://disease.sh/v3/covid-19/all"
    json_data = requests.get(api).json()
    total_cases = str(json_data['cases'])
    total_deaths = str(json_data['deaths'])
    total_recovered = str(json_data['recovered'])
    today_cases = str(json_data['todayCases'])
    today_deaths = str(json_data['todayDeaths'])
    today_recovered = str(json_data['todayRecovered'])
    active_cases = str(json_data['active'])
    critical_cases = str(json_data['critical'])
    affected_countries = str(json_data['affectedCountries'])
    updated_at = json_data['updated']
    date = datetime.datetime.fromtimestamp(updated_at/1e3)
    label.config(text = 'Total Case : '+total_cases+'\n'+'Total Deaths : '+total_deaths+'\n'+'Total Recovered : '+total_recovered+'\n'+'Today Cases : '+today_cases+'\n'+'Today Deaths : '+today_deaths+'\n'+'Today Recovered : '+today_recovered+'\n'+'Active Cases : '+active_cases+'\n'+'Critical Cases : '+critical_cases+'\n'+'Affected Countries : '+affected_countries)
    label2.config(text = date)
canvas = tkinter.Tk()
canvas.geometry('600x600')
canvas.title("Corona Tracker - by Astin")
f = ("Gayathri Thin", 22, 'bold')
button = tkinter.Button(canvas, font=f, text= 'Refresh', command=getCovidData)
button.pack(pady=20)
label = tkinter.Label(canvas, font = f)
label.pack(pady=20)
label2 = tkinter.Label(canvas, font = 8)
label2.pack()
canvas.mainloop()