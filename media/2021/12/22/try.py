import requests

url = "https://contentapi.tradermade.com/api/v1/hilo_alerts"

querystring = {"HwMGnlwVczNjVIbz5jF2":"HwMGnlwVczNjVIbz5jF2"}

response = requests.get(url, params=querystring)

print(response.json())
