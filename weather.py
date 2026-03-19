import requests
import matplotlib.pyplot as plt

plt.style.use("Solarize_Light2")
fig,ax=plt.subplots(2,2)

API_KEY="your-api-key"
cities=["Lahore","Karachi","Islamabad","Peshawar","Sialkot","Multan"]

Temperature=[]
Humidity=[]
Wind=[]
Clouds=[]

for i in cities:
    url=f"https://api.openweathermap.org/data/2.5/weather?q={i}&appid={API_KEY}&units=metric"
    request=requests.get(url)
    data=request.json()
    # print(data)
    Temperature.append(data["main"]["temp"])
    Humidity.append(data["main"]["humidity"])
    Wind.append(data["wind"]["speed"])
    Clouds.append(data['clouds']['all'])    
  
ax[0,0].bar(cities,Temperature,color='r')
ax[0,0].set_title("Pakistan Cities Temperature")
ax[0,0].set_xticklabels(cities,rotation=45)
ax[0,0].set_ylabel("Temperature")
# fig.set_size_inches([5,5])

ax[0,1].bar(cities,Humidity,color='b')
ax[0,1].set_title("Pakistan Cities Humidity")
ax[0,1].set_xticklabels(cities,rotation=45)
ax[0,1].set_ylabel("Humidity")

ax[1,0].scatter(cities,Wind,color='g')
ax[1,0].set_title("Pakistan Cities Wind")
ax[1,0].set_xticklabels(cities,rotation=45)
ax[1,0].set_ylabel("Wind")

ax[1,1].bar(cities,Clouds,color='black')
ax[1,1].set_title("Pakistan Cities Clouds")
ax[1,1].set_xticklabels(cities,rotation=45)
ax[1,1].set_ylabel("Clouds")

fig.set_size_inches([7,7])
plt.tight_layout()
fig.savefig("Weather_dashboard.jpg")
plt.show()
    
