import requests

r = requests.get("https://api.ipify.org?format=json", timeout=10)
data = r.json()

print("Your public IP is:", data["ip"])
