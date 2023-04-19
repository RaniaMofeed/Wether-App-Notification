# import required libraries
import requests
from bs4 import BeautifulSoup
from win10toast import ToastNotifier

# create an object to ToastNotifier class
n = ToastNotifier()


# define a function
def getdata(url):
    r = requests.get(url)
    return r.text


#htmldata = getdata("https://weather.com/en-IN/weather/today/l/25.59,85.14?par=google&temp=c/")
htmldata = getdata("https://weather.com/en-IN/weather/today/")

soup = BeautifulSoup(htmldata, 'html.parser')

#current_temp = soup.find_all("span", class_="_-_-components-src-organism-CurrentConditions-CurrentConditions--tempValue--MHmYY")
current_temp = soup.find_all("span", class_="CurrentConditions--tempValue--MHmYY")
#print(current_temp)

#chances_rain = soup.find_all("div", class_="_-_-components-src-organism-CurrentConditions-CurrentConditions--precipValue--2aJSf")
chances_rain = soup.find_all("div", class_="CurrentConditions--phraseValue--mZC_p")
#print(chances_rain)
print(chances_rain[0].text)

temp = str(current_temp)
#print(len(temp)) #93
#print(temp[-11:-8])
#print(temp[93:-8])
temp_rain = str(chances_rain)
# print(len(temp_rain))
# print(temp_rain[-11:-7])

# result = "current_temp " + temp[128:-9] + " in patna bihar" + "\n" + temp_rain[131:-14]
# n.show_toast("live Weather update", result, duration=10)
# result = "current_temp " + temp[1:9] + " in patna bihar" + "\n" + temp_rain[1:9]
# n.show_toast("live Weather update", result, duration=10)