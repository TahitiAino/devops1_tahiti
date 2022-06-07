from requests import Request, Session, Response

from dotenv import load_dotenv

load_dotenv()
mykey = os.environ['APIKEY'] 
latitude = os.environ['LAT']  
longitude = os.environ['LONG'] 

response = requests.get("https://api.openweathermap.org/data/2.5/weather?lat=" + latitude + "&lon=" + longitude + "&appid=" + mykey + "&units=metric")

print(response)