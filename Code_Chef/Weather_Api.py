import requests as req
API_key=input()
City=input()


r = req.get(f' https://api.openweathermap.org/data/2.5/weather?q={City}&appid={API_key}')
    
Keynote=r.json()
Weather=Keynote['weather'][0]['main']
Temp=Keynote['main']['temp'],Keynote['main']['humidity']
print(f"The Weather In {City} Is {Weather} And Temprature IS {Temp[0]} With Humidity Of {Temp[1]}")


